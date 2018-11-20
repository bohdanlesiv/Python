import  os



class LogReader():
    def __init__(self,path =os.path.dirname(os.path.realpath(__file__)) ,mask ='.log'):
        self.path =path
        self.mask =mask

    @property
    def files(self):
        files =os.listdir(self.path)
        list = sorted([i for i in files if i.endswith(self.mask)])
        for i in list:
            yield i

    def __iter__(self):
        self._files = list(self.files)
        self._files_count =0
        self._line_counter = 0
        return  self

    def __next__(self):
        if len(self._files) == self._files_count:
            raise StopIteration
        file = self._files[self._files_count]
        with open(os.path.join(self.path,file),'r') as f:
            lines = list(f)
            line_total = len(lines)
            try:
               line = lines[self._line_counter].rstrip()
            except:
               line =''
            self._line_counter +=1
            if line_total == self._line_counter or line_total == 0:
                self._line_counter = 0
                self._files_count += 1
            return line

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass








