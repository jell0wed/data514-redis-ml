#!/bin/sh

wget https://github.com/tianqwang/Toxic-Comment-Classification-Challenge/raw/master/data/test.csv -O ./data/test.csv
wget https://github.com/tianqwang/Toxic-Comment-Classification-Challenge/raw/master/data/test_labels.csv -O ./data/test_labels.csv
wget https://github.com/tianqwang/Toxic-Comment-Classification-Challenge/raw/master/data/train.csv -O ./data/train.csv
wget https://worksheets.codalab.org/rest/bundles/0x219a956574434c6b952d9a2070baf9d9/contents/blob/glove.6B.100d.txt -O ./data/glove.6B.100d.txt