from collections import deque

graph = {}
graph['you'] = ['olia', 'sasha', 'denis', 'diana']
graph['olia'] = ['diana', 'misha']
graph['sasha'] = ['ivan', 'yulia']
graph['denis'] = []
graph['diana'] = ['you']
graph['misha'] = []
graph['ivan'] = []
graph['yulia'] = []


def person_is_seller(name):
    return name[-1] == 'o'
    pass


def do_search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            print('Check {}'.format(person))
            if person_is_seller(person):
                print('{} is mango seller'.format(person))
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    print('Not found mango seller')
    return False


do_search('you')