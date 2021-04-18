from multiprocessing import Pool


class ParallelExcutor():
    def __init__(self, pool_size=40, func=None, task_list=[], args=[]):
        self.parallels = pool_size
        self.pool = Pool(pool_size)
        self.func = func
        self.task_list = task_list
        self.delta = int(len(task_list) / self.parallels) + 1
        self.args = args
        self.result_list = []

    def exec(self):
        for i in range(self.parallels):
            if (i + 1) * self.delta > len(self.task_list):
                task_list = self.task_list[i * self.delta:]
            else:
                task_list = self.task_list[i * self.delta:(i+1) * self.delta]

            args = list()
            args.append(task_list)
            for arg in self.args:
                args.append(arg)
            result = self.pool.apply_async(self.func, args=args)
            self.result_list.append(result)
        self.pool.close()
        self.pool.join()







