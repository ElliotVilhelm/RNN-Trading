SEQ_LEN = 60                               # last 60 minutes
FUTURE_PERIOD_PREDICT = 3                  # predict movement in 3 minutes
RATIO_TO_PREDICT = "BTC-USD"
currencies = ["BTCUSDT", "LTCUSDT", "ETHUSDT"]
OPEN_TIME_IDX = 0
OPEN_IDX = 1
HIGH_IDX = 2
LOW_IDX = 3
CLOSE_IDX = 4
VOLUME_IDX = 5
EPOCHS = 20
BATCH_SIZE = 128
LEARNING_RATE = 0.001
DECAY = 1e-4
LOSS = 'sparse_categorical_crossentropy'
INPUT_DIM = 6                              # n_coins * [close, vol]
