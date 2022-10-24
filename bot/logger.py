import datetime
import codecs

def info(string):
    file = codecs.open('log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'Debug: ' + string + '\n')
    file.close()

def debug(string):
    file = codecs.open('log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'Info: ' + string + '\n')
    file.close()

def warn(string):
    file = codecs.open('log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'Warn: ' + string + '\n')
    file.close()

def exception(string):
    file = codecs.open('log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'Debug: ' + string + '\n')
    file.close()

def error(string):
    file = codecs.open('log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'Error: ' + string + '\n')
    file.close()    

def critical(string):
    file = codecs.open('bot/log.txt', 'a', 'utf-8')
    file.write('[' + str(datetime.datetime.now()) + '] ' + 'Critical: ' + string + '\n')
    file.close()
