SEQ_LEN = 48                               # last 60 minutes
FUTURE_PERIOD_PREDICT = 12                  # predict movement in 3 minutes
RATIO_TO_PREDICT = "BTC-USD"
currencies = ["BTCUSDT", "BCHABCUSDT", "ETHUSDT", "EOSUSDT", "LTCUSDT"]
OPEN_TIME_IDX = 0
OPEN_IDX = 1
HIGH_IDX = 2
LOW_IDX = 3
CLOSE_IDX = 4
VOLUME_IDX = 5
EPOCHS = 10
BATCH_SIZE = 256
LEARNING_RATE = 0.0003
DECAY = 1e-5
LOSS = 'sparse_categorical_crossentropy'
INPUT_DIM = 14                             # n_coins * [close, vol] + 4
# INPUT_DIM = 6                             # n_coins * [close, vol] + 4
