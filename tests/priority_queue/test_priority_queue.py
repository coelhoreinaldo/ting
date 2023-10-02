from ting_file_management.priority_queue import PriorityQueue
from pytest import raises


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue({"qtd_linhas": 10})
    priority_queue.enqueue({"qtd_linhas": 2})
    priority_queue.enqueue({"qtd_linhas": 29})
    priority_queue.enqueue({"qtd_linhas": 4})
    priority_queue.enqueue({"qtd_linhas": 40})
    assert priority_queue.__len__() == 5
    assert priority_queue.high_priority.__len__() == 2
    assert priority_queue.regular_priority.__len__() == 3

    priority_queue.dequeue()
    assert priority_queue.__len__() == 4
    assert priority_queue.high_priority.__len__() == 1
    assert priority_queue.regular_priority.__len__() == 3

    found_elem = priority_queue.search(0)
    assert found_elem == {"qtd_linhas": 4}

    with raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(99)
