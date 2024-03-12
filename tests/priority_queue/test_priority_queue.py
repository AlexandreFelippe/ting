# from ting_file_management.priority_queue import PriorityQueue
# import pytest


# def test_basic_priority_queueing():
#     my_priority_queue = PriorityQueue()

#     my_priority_queue.enqueue({"qtd_linhas": 3})
#     my_priority_queue.enqueue({"qtd_linhas": 4})
#     my_priority_queue.enqueue({"qtd_linhas": 6})

#     assert len(my_priority_queue) == 3
#     assert len(my_priority_queue.high_priority) == 2
#     assert len(my_priority_queue.regular_priority) == 1

#     my_priority_queue.dequeue()
#     assert len(my_priority_queue) == 2

#     searched_element = my_priority_queue.search(0)
#     assert searched_element["qtd_linhas"] == 4

#     with pytest.raises(IndexError):
#         my_priority_queue.search(52)
