#!/usr/bin/python

import os
import shutil
import codecs
import commands


def get_all_files(directory):
    ignore = ['t', 'a', 'o', 'png', 'pcap', 'pcapng']
    cmd = 'find {}'.format(directory)
    filelist = commands.getoutput(cmd).split('\n')
    ret = []
    for f in filelist:
        suffix = f.split('.')[-1]
        if os.path.isfile(f) and suffix not in ignore:
            ret.append(f)
    return ret


def convert2utf8(source, target):
    #from_encode = 'iso-8859-1'
    from_encode = 'gb2312'
    to_encode = 'utf-8'
    BLOCKSIZE = 1024 *1024

    with codecs.open(source, "r", from_encode) as sourceFile:
        with codecs.open(target, "w", to_encode) as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)


def tempfile(f):
    return '{}.tmp'.format(f)


def convert_all_files(filelist):
    for f in filelist:
        print 'converting {} ...'.format(f)
        try:
            shutil.copyfile(f, tempfile(f))
            convert2utf8(tempfile(f), f)
        except Exception as e:
            shutil.copyfile(tempfile(f), f)
            print e
        finally:
            os.remove(tempfile(f))


#filelist = get_all_files('./notes')
filelist = get_all_files('./nginx-1.9.2/src/core')
convert_all_files(filelist)
