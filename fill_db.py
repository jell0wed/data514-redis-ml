import redis
from redis.commands.search.field import TextField, NumericField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.json.path import Path
import timeit
import pandas as pd

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
        r.delete(key)
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
        r.delete(key)
        c += 1
    print("Deleted %d `train:*` entries" % c)

def insert_training_dataset(r):
    # load training dataset
    train_df = pd.read_csv("data/train.csv")
    # insert the training dataset entries
    start_timer = timeit.default_timer()
    counter = 0
    for index, row in train_df.iterrows():
        train_obj = row[['id', 'comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].to_dict()
        key = "train:%d" % (index)
        r.json().set(key, Path.root_path(), train_obj)
        counter += 1
        if counter % 10000 == 0:
            print("Inserted %d training examples... still going" % counter)
    print("Inserted %d examples in for index `train:*` in " % (counter), timeit.default_timer() - start_timer)

def insert_testing_dataset(r):
    # load testing dataset
    test_df = pd.read_csv("data/test.csv")
    test_df_labels = pd.read_csv("data/test_labels.csv")

    # merge both datasets
    test_df = pd.merge(test_df, test_df_labels, on='id', how='inner')
    test_df = test_df[['id', 'comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']]

    test_df['toxic'] = test_df['toxic'].apply(lambda x: 0 if x < 0 else x)
    test_df['severe_toxic'] = test_df['severe_toxic'].apply(lambda x: 0 if x < 0 else x)
    test_df['obscene'] = test_df['obscene'].apply(lambda x: 0 if x < 0 else x)
    test_df['threat'] = test_df['threat'].apply(lambda x: 0 if x < 0 else x)
    test_df['insult'] = test_df['insult'].apply(lambda x: 0 if x < 0 else x)
    test_df['identity_hate'] = test_df['identity_hate'].apply(lambda x: 0 if x < 0 else x)

    # insert the testing dataset entries
    start_timer = timeit.default_timer()
    counter = 0
    for index, row in test_df.iterrows():
        test_obj = row[['id', 'comment_text', 'toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']].to_dict()
        key = "test:%d" % (index)
        r.json().set(key, Path.root_path(), test_obj)
        counter += 1
        if counter % 10000 == 0:
            print("Inserted %d testing examples... still going" % counter)
    print("Inserted %d examples in for index `test:*` " % counter, timeit.default_timer() - start_timer)

if __name__ == "__main__":
    r = initialize_redis()
    initialize_schema(r)
    insert_training_dataset(r)
    insert_testing_dataset(r)

    print("Successfully inserted %d total entries into the redis database" % (r.dbsize()))