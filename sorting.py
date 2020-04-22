from abc import ABC, abstractmethod
from collections.abc import Iterable
from random import randint
from time import time


class Validation:

    def __init__(self, obj: list) -> None:
        self.obj = obj

    def validate_data(self) -> bool:
        if not self.__is_iterable(self.obj):
            print('ERROR: Object is not iterable.')
            return False
        if not self.__is_integers_in_array(self.obj):
            print('ERROR: Object contains some not-integer elements.')
            return False
        print('Object is valid')
        return True

    def __is_iterable(self, array: list) -> bool:
        return isinstance(array, Iterable)

    def __is_integers_in_array(self, array: list) -> bool:
        for element in array:
            if not isinstance(element, int):
                return False
        return True


class Sort(ABC):
    def __init__(self, obj: list) -> None:
        self.array = obj
        super(Sort, self).__init__()

    @abstractmethod
    def get_sorted_array(self):
        pass


class QuickSort(Sort):
    def get_sorted_array(self) -> list:
        def _get_sorted_array(array, low_num, high_num):
            if low_num < high_num:
                split_index = self.__partition(self.array, low_num, high_num)
                _get_sorted_array(array, low_num, split_index)
                _get_sorted_array(array, split_index + 1, high_num)

        _get_sorted_array(self.array, 0, len(self.array) - 1)

        return self.array

    def __partition(self, array, low_num, high_num) -> int:
        pivot = array[(low_num + high_num) // 2]
        i = low_num - 1
        j = high_num + 1

        while True:
            i += 1
            while array[i] < pivot:
                i += 1
            j -= 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            array[i], array[j] = array[j], array[i]


class MergeSort(Sort):
    def get_sorted_array(self) -> list:
        return self.__merge_sort(self.array)

    def __merge_sort(self, array) -> list:
        if len(array) <= 1:
            return array
        mediana = len(array) // 2
        left_array = self.__merge_sort(array[:mediana])
        right_array = self.__merge_sort(array[mediana:])
        return self.__merge(left_array, right_array)

    def __merge(self, left_array, right_array) -> list:
        sorted_array = []
        left_array_index = right_array_index = 0
        left_array_length, right_array_length = len(left_array), len(right_array)

        for i in range(left_array_length + right_array_length):
            if left_array_index < left_array_length and right_array_index < right_array_length:
                if left_array[left_array_index] <= right_array[right_array_index]:
                    sorted_array.append(left_array[left_array_index])
                    left_array_index += 1
                else:
                    sorted_array.append(right_array[right_array_index])
                    right_array_index += 1

            elif left_array_index == left_array_length:
                sorted_array.append(right_array[right_array_index])
                right_array_index += 1
            elif right_array_index == right_array_length:
                sorted_array.append(left_array[left_array_index])
                left_array_index += 1
        return sorted_array


class BubbleSort(Sort):
    def get_sorted_array(self) -> list:
        need_to_swap = True
        while need_to_swap:
            need_to_swap = False
            for i in range(len(self.array) - 1):
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
                    need_to_swap = True
        return self.array


class InsertionSort(Sort):
    def get_sorted_array(self) -> list:
        for i in range(1, len(self.array)):
            item_to_insert = self.array[i]
            j = i - 1
            while j >= 0 and self.array[j] > item_to_insert:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = item_to_insert
        return self.array


class DefaultPythonSort(Sort):
    def get_sorted_array(self) -> list:
        return sorted(self.array)


class SortContext:
    def __init__(self) -> None:
        self.current_sort = None

    def set_quick_sort(self) -> None:
        self.current_sort = QuickSort

    def set_bubble_sort(self) -> None:
        self.current_sort = BubbleSort

    def set_insertion_sort(self) -> None:
        self.current_sort = InsertionSort

    def set_merge_sort(self) -> None:
        self.current_sort = MergeSort


if __name__ == '__main__':

    objects_array = []  # массив обьектов сортировки
    result = {}  # словарь для результатов
    length_of_test_array = 1000  # длина тестового массива

    test_arrays = []
    while len(test_arrays) < 6:
        test_array = [randint(1, 100) for _ in range(length_of_test_array)]
        validate_obj = Validation(test_array)
        if validate_obj.validate_data():
            test_arrays.append(test_array)

    # добавляем в массив обьекты сортировки
    objects_array.append(InsertionSort(test_arrays[0]))
    objects_array.append(BubbleSort(test_arrays[1]))
    objects_array.append(MergeSort(test_arrays[2]))
    objects_array.append(QuickSort(test_arrays[3]))
    objects_array.append(DefaultPythonSort(test_arrays[4]))

    # проходим по массивам и выполняем сортировку, замеряем время сортировки и добавляем результаты в словарь
    for obj in objects_array:
        print(f'Sorting by {type(obj)}...')
        t1 = time()
        obj.get_sorted_array()
        t2 = time()
        delta_time = t2 - t1
        result[f'{type(obj)}'] = delta_time

    # делаем сортировку по скорости
    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}

    for element in result:
        print(f'{element} ==> {result[element]}')

    # test_array = [randint(1, 100) for _ in range(1000)]
    # context = SortContext()
    # if context.current_sort is None:
    #     print('Current sort method is not set.')









