from webweb import Web

def f(arr, name):
    i = 0
    node = 0
    a = ([])
    d = {'nodes': {},}
   
    while i < len(arr):
        a.append([arr[i][0], arr[i][1]]),
        if arr[i][0] == name:
            d['nodes'][arr[i][0]] = {'cooperativity' : 'Наш микросервис',}
        else:
            d['nodes'][arr[i][0]] = {'cooperativity' : 'Связанный микросервис',}
        if arr[i][1] == name:
            d['nodes'][arr[i][1]] = {'cooperativity' : 'Наш микросервис',}
        else:
            d['nodes'][arr[i][1]] = {'cooperativity' : 'Зависимый микросервис',}
        node += 2
        i += 1
    
    web = Web(
        adjacency= a,
        display= d
    )
    web.display.colorBy = 'cooperativity'
    web.display.radius = 40
    web.display.linkLength = 400
    web.display.colorPalette = 'Reds'
    web.display.charge = 4000
    web.display.showNodeNames = True
    web.display.scaleLinkWidth = True
    web.display.nameToMatch = name
    web.show()

if __name__ == '__main__':
    name = 'vk'
    arr = [['viber', 'vk'], ['vk', 'inst'], ['b', 'vk']]
    f(arr, name)
