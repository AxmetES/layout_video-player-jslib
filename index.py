from livereload import Server


def rebuild():
    print("Site rebuilded")


rebuild()

server = Server()
server.watch('index.html', rebuild)
server.serve(root='.')
