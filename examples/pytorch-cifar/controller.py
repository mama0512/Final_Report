from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

# 单线程
server = SimpleJSONRPCServer(('localhost', 8080))

used_peers = [ ]

def controller(name):

    if not have_been_add(name):
        if not partial_enough():
            used_peers.append(name)
            # print('1')
            return 1,used_peers
        else:
            # print('2')
            return 0,[ ]
    else:
        if not partial_enough():
            # print('3')
            return 1,used_peers
        else:
            a=used_peers

            # print('4')
            return 1,a





def partial_enough():
    if len(used_peers)==2:
            return True
def have_been_add(name):
    if name in used_peers:
        return True

num = [ ]
def have_re(name):
    num.append(name)
    if len(num)==2:
        used_peers.clear()
        num.clear()

server.register_function(controller)
server.register_function(have_re)
server.serve_forever()