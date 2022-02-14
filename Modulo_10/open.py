
'''
Se trata de una sola función main() que abre el archivo inexistente. 
Al final, esta función usa un asistente de Python que indica al intérprete que ejecute la función main()
cuando se le llama en el terminal.
'''

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")