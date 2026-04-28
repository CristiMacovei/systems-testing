import pytest
from tree import Tree  # Importă clasa Tree din fișierul tău tree.py

@pytest.fixture
def bst_tree():
    tree = Tree()
    for value in [10, 5, 15, 2, 7, 20]:
        tree.add(value)
    return tree

def test_find_existing_element(bst_tree):
    found_node = bst_tree.find(7)
    assert found_node is not None, "Funcția ar trebui să returneze un nod, nu None."
    assert found_node.data == 7, f"Ne așteptam la valoarea 7, dar am primit {found_node.data}"

def test_find_non_existing_element(bst_tree):
    not_found_node = bst_tree.find(99)
    assert not_found_node is None, "Funcția ar trebui să returneze None pentru o valoare inexistentă."
