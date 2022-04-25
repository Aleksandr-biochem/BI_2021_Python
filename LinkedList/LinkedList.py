class LinkedListItem:
    def __init__(self, value):
        self.value = value
        self.__next = None

    def get_next(self):
        return self.__next

    def set_next(self, next_item):
        self.__next = next_item

    def has_next(self):
        return self.__next is not None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__len = 0

    def __getitem__(self, index):
        current = self.__head
        for _ in range(index):
            if current is None or not current.has_next():
                raise IndexError
            current = current.get_next()
        return current.value

    def __len__(self):
        return self.__len

    def __contains__(self, value):
        contains = False
        current = self.__head
        for _ in range(self.__len):
            if current.value == value:
                contains = True
                break
            current = current.get_next()
        return contains

    def add(self, value, index=None):
        if index is None:  # by default add to the tail
            index = self.__len
        if self.__len < index:  # check if index is valid
            raise IndexError
        new_item = LinkedListItem(value)
        if not self.__head:  # if empty add first element
            self.__head = new_item
            self.__tail = new_item
        else:
            if index == 0:  # add item as new head
                new_item.set_next(self.__head)
                self.__head = new_item
            elif index == self.__len:  # add item to the tail
                self.__tail.set_next(new_item)
                self.__tail = new_item
            else:
                right = self.__head  # get items between which a new one is inserted
                for _ in range(index - 1):
                    right = right.get_next()
                left = right.get_next()
                right.set_next(new_item)
                new_item.set_next(left)
        self.__len += 1

    def extend(self, values, index=None):
        if index is None:  # by default extend from the tail
            index = self.__len
        if self.__len < index:  # check if the index is valid
            raise IndexError
        for value in values:  # add each value to linked list
            self.add(value, index)
            index += 1

    def pop(self, index=None):
        if index is None:  # by default pop tail item
            index = self.__len - 1
        if self.__len <= index or self.__len == 0:  # check if the index is valid
            raise IndexError
        if index == 0:  # pop head
            self.__head = self.__head.get_next()
            if self.__len == 1:  # if the only element is poped erase tail too
                self.__tail = None
        else:  # pop any other item
            previous = self.__head
            for i in range(index - 1):
                previous = previous.get_next()
            new_next = previous.get_next().get_next()
            previous.set_next(new_next)
            if new_next is None:  # if last item is poped - change tail
                self.__tail = previous
        self.__len -= 1  # decrease length

    def remove_last_occurence(self, value):
        last_occurence = None
        current = self.__head
        for index in range(self.__len):
            if current.value == value:
                last_occurence = index
            current = current.get_next()
        if not last_occurence is None:
            self.pop(last_occurence)

    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value


if __name__ == "__main__":
    items = LinkedList()
    items.add(10)
    items.add(11)
    items.add(12)
    items.add(13)
    items.add(20)
    print(items[1])
    print(items[2])
    print(items[100])
    print(items.first())
    print(items.last())
    print(len(items))
