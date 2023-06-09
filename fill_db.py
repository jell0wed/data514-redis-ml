import redis
from redis.commands.search.field import TextField, NumericField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.json.path import Path
import timeit
import pandas as pd
from tqdm import tqdm

def initialize_redis(host='localhost', port=6379):
    r = redis.Redis(host, port, decode_responses=True)
    print("Connected to redis instance on '%s:%d'" % (host, port))
    r.flushall()
    return r

def initialize_schema(r):
    # design schema for both indexes
    schema_train = (
        TextField("$.id"),
        TextField("$.comment_text"),
        NumericField("$.toxic"),
        NumericField("$.severe_toxic"),
        NumericField("$.obscene"),
        NumericField("$.threat"),
        NumericField("$.insult"),
        NumericField("$.identity_hate")
    )

    schema_test = (
        TextField("$.id"),
        TextField("$.comment_text")
    )

    # create training index
    rs_train = r.ft("idx:train")
    rs_train.create_index(
        schema_train,
        definition=IndexDefinition(
            prefix=["train:"], index_type=IndexType.JSON
        )
    )
    print("Created `idx:train` index")

    # delete any existing entries
    c = 0
    for k in r.scan_iter("train:*"):
        r.delete(k)
        c += 1
    print("Deleted %d `train:*` entries" % c)
        
    # create training index
    rs_train = r.ft("idx:test")
    rs_train.create_index(
        schema_test,
        definition=IndexDefinition(
            prefix=["test:"], index_type=IndexType.JSON
        )
    )
    print("Created `idx:test` index")

    # delete any existing entries
    c = 0
    for k in r.scan_iter("test:*"):
        r.delete(k)
        c += 1
    print("Deleted %d `train:*` entries" % c)

def insert_training_dataset(r):
    # load training dataset
    train_df = pd.read_csv("data/train_cleaned.csv")
    # insert the training dataset entries
    start_timer = timeit.default_timer()
    counter = 0
    print("Currently inserting training examples: ")
    for index, row in tqdm(train_df.iterrows(), total=len(train_df.index)):
        train_obj = row[['id', 'comment_text', 'normal', 'toxic', 'obscene', 'threat', 'insult', 'identity_hate']].to_dict()
        key = "train:%d" % (counter)
        try:
            r.json().set(key, Path.root_path(), train_obj)
            counter += 1
        except:
            print("exception", row)
    print("Inserted %d examples in for index `train:*` in " % (counter), timeit.default_timer() - start_timer)

def insert_testing_dataset(r):
    # load training dataset
    test_df = pd.read_csv("data/test_cleaned.csv")
    # insert the training dataset entries
    start_timer = timeit.default_timer()
    counter = 0
    print("Currently inserting testing examples: ")
    for index, row in tqdm(test_df.iterrows(), total=len(test_df.index)):
        test_obj = row[['id', 'comment_text', 'normal', 'toxic', 'obscene', 'threat', 'insult', 'identity_hate']].to_dict()
        key = "test:%d" % (counter)
        try:
            r.json().set(key, Path.root_path(), test_obj)
            counter += 1
        except:
            print("exception", row)
    print("Inserted %d examples in for index `test:*` in " % (counter), timeit.default_timer() - start_timer)

if __name__ == "__main__":
    r = initialize_redis()
    initialize_schema(r)
    insert_training_dataset(r)
    insert_testing_dataset(r)

    print("Successfully inserted %d total entries into the redis database" % (r.dbsize()))