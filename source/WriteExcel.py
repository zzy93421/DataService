'''
Created on 2017年4月21日
本类用于写excel文件
@author: zhangzhiyuan
'''
import xlwt
import os


class WriteExcel:
    '''
    用于写excel文件的类
    '''

    def __init__(self, path, filename, sheetname, colheader, dataset):
        '''
        初始化函数
        '''
        self.filepath = path
        self.filename = filename + '.xls'
        self.sheetname = sheetname
        self.colheader = colheader
        self.cols = len(colheader)
        self.dataset = dataset
        self.file = xlwt.Workbook()
        self.sheet = self.file.add_sheet(
            self.sheetname, cell_overwrite_ok=True)
        self.style = xlwt.easyxf('font: bold 1')
        self.style1 = xlwt.easyxf()
        self.width = list()
        for i in range(self.cols):
            self.width.append(len(self.colheader[i][0]) * 350)
        '''
        self.style = xlwt.easyxf(
            'pattern: pattern solid; font: bold on;')
        '''
        borders = xlwt.Borders()
        # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR,
        # MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED,
        # THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED,
        # SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
        borders.left = xlwt.Borders.THIN
        borders.right = xlwt.Borders.THIN
        borders.top = xlwt.Borders.THIN
        borders.bottom = xlwt.Borders.THIN
        borders.left_colour = 0x40
        borders.right_colour = 0x40
        borders.top_colour = 0x40
        borders.bottom_colour = 0x40
        self.style.borders = borders
        self.style1.borders = borders

    def writerow(self, rowrecord, cols, rowindex, style):
        '''
        用于在sheet表中写入一行数据
        '''
        for i in range(cols):
            self.sheet.write(rowindex, i, rowrecord[i], style)

    def writefile(self):
        '''
        用于创建excel文件，并调用writerow函数写入内容
        '''
        # 写入列标题
        rowindex = 0
        self.writerow(self.colheader, self.cols, rowindex, self.style)
        # 写入数据
        for rec in self.dataset:
            rowindex += 1
            self.writerow(rec, self.cols, rowindex, self.style1)
        for i in range(self.cols):
            self.sheet.col(i).width = self.width[i]
        # 保存文档
        self.file.save(os.path.join(self.filepath, self.filename))
        print('程序已正常结束！')
