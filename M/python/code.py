class HistoricalArray:
    def __init__(self, size) -> None:
        self.size_ = size
        self.data = dict()
        self.current_era_id = 0
        self.data[self.current_era_id] = dict()

    def set(self, index, value) -> None:
        self.data[self.current_era_id][index] = value

    def get(self, index, era_id) -> int:
        if index in self.data[era_id]:
            return self.data[era_id][index]
        else:
            return 0

    def begin_new_era(self, era_id) -> None:
        self.current_era_id = era_id
        self.data[self.current_era_id] = dict()

size = int(input())
q = int(input())
historical_array = HistoricalArray(size)
for i in range(q):
    query = input().split()
    query_type = query[0]
    if query_type == "set":
        historical_array.set(int(query[1]), int(query[2]))
    elif query_type == "begin_new_era":
        historical_array.begin_new_era(int(query[1]))
    else:
        print(historical_array.get(int(query[1]), int(query[2])))
