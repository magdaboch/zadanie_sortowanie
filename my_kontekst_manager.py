class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        file = None
        print('__init__')

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print('__enter__')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val != None:
            print('Exception has been handled \n File: {} {}'.format(self.filename, exc_val))
        self.file.close()
        print('__exit__')
        return True

#if __name__ == '__main__':
    # print('123')
    # with open('log.txt') as f:
    #     data = f.read()
    #
    # file = FileManager('code', 'w')
    # file.__enter__()
    # file.__exit__('w', 45, 60)
with FileManager('demo.txt', 'r') as opened_file:
    data = opened_file.undefined_function()





