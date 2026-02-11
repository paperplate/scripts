import os
import subprocess
import sys

def extractName(filePath, ext):
    filename = ''

    dirLevel = filePath.rfind('/')
    if dirLevel >= 0:
        name = filePath[dirLevel:]
    else:
        name = filePath

    opn = name.find(']')
    ed = name[opn:].find('[')

    if opn < ed:
        opn = opn + 2
        ed = ed - 3
        filename = name[opn : opn+ed] + ext
    else:
        filename = name

    if filename == filePath:
        filename = filename[:-4] + ' (1)' + ext

    return filename


def cvt(dirName):
    for root, _, files in os.walk(dirName):
        if files == []:
            continue
        for file in files:
            ext = file[-4:]
            if ext == '.mkv' or ext == '.mp4':
                filename = extractName(file, ext)
                if filename == '':
                    print('skipped', file)
                    continue
            else:
                continue
            print('processing:', filename)
            subprocess.call('./convert.sh "%s" "%s"' % (root+'/'+file, root+'/'+filename), shell=True)



def batch(filename, outname, n):
    for i in range(int(n)):
        try:
            subprocess.call('./convert.sh "%s" "%s"' % (filename.format(i), outname.format(i)), shell=True)
        except:
            print('skipped', filename.format(i))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print('Converting bracketed files.')
        cvt(sys.argv[1])
    elif len(sys.argv) == 4:
        print('Converting batch files.')
        batch(sys.argv[1], sys.argv[2], sys.argv[3])
    print('Done!')
