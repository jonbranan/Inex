def inexLog(self):
    """Setting up the log file, if self.useLog is set to true and self.logLevel is DEBUG, INFO, WARNING or ERROR"""
    if self.useLog:
        if self.logLevel.lower() == 'debug':
            self.il.basicConfig(filename=self.logPath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.il.DEBUG)
        elif self.logLevel.lower() == 'info':
            self.il.basicConfig(filename=self.logPath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.il.INFO)
        elif self.logLevel.lower() == 'warning':
            self.il.basicConfig(filename=self.logPath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.il.WARNING)
        elif self.logLevel.lower() == 'error':
            self.il.basicConfig(filename=self.logPath, format='%(asctime)s:%(levelname)s:%(message)s', encoding='utf-8', datefmt='%m/%d/%Y %I:%M:%S %p',level=self.il.ERROR)