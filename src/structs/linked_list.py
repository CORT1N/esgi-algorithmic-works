def search_list(head, key):
    current = head
    while current:
        if current['key'] == key:
            return current
        current = current['next']
    return None

def insert_list(head, key):
    new_node = {'key': key, 'next': head}
    return new_node

def delete_list(head, key):
    if head is None:
        return None

    if head['key'] == key:
        return head['next']

    current = head
    while current['next']:
        if current['next']['key'] == key:
            current['next'] = current['next']['next']
            return head

        current = current['next']

    return head

# Test function to validate the linked list operations
def test_linked_list():
    head = None
    
    # Insert elements
    head = insert_list(head, 10)
    head = insert_list(head, 20)
    head = insert_list(head, 30)
    print("Linked list after insertions:")
    current = head
    while current:
        print(current['key'], end=" -> ")
        current = current['next']
    print("None")

    # Search for a key
    key_to_search = 20
    result = search_list(head, key_to_search)
    print(f"Search result for key {key_to_search}: {result['key'] if result else 'Not found'}")

    # Delete an element
    key_to_delete = 20
    head = delete_list(head, key_to_delete)
    print(f"Linked list after deleting key {key_to_delete}:")
    current = head
    while current:
        print(current['key'], end=" -> ")
        current = current['next']
    print("None")

    # Try deleting a non-existing element
    key_to_delete = 100
    head = delete_list(head, key_to_delete)
    print(f"Linked list after attempting to delete key {key_to_delete}:")
    current = head
    while current:
        print(current['key'], end=" -> ")
        current = current['next']
    print("None")

test_linked_list()