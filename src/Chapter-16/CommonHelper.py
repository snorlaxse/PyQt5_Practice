'''
@FileName: CommonHelper.py
@Author: CaptainSE
@Time: 2019-01-31 
@Desc: For LoadQSS.py

'''

class CommonHelper:
    @staticmethod
    def readQSS(style):
        with open(style,'r') as f:
            return f.read()