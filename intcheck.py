"""
Created By: Abhiroop Talasila
Date: May 23 2020
Description: This module checks the integrity of data

"""

import hashlib
import sys
import os


def check_md5(fname):
    md5hash = hashlib.md5()
    with open(fname) as handle:  # Consider one line in the file at a time 
        for line in handle:
            md5hash.update(line.encode('utf-8'))
    return md5hash.hexdigest()

def check_sha1(fname):
    sha1hash = hashlib.sha1()
    with open(fname) as handle:
        for line in handle:
            sha1hash.update(line.encode('utf-8'))
    return sha1hash.hexdigest()

def check_sha512(fname):
    sha512hash = hashlib.sha512()
    with open(fname) as handle:
        for line in handle:
            sha512hash.update(line.encode('utf-8'))
    return sha512hash.hexdigest()


if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        print("Incorrect arguments\nCorrect Usage:\n\tArg1: Input File to check against\n\tArg2: File to be checked")
        sys.exit(0)
    else:
        files = [sys.argv[1], sys.argv[2]] # input arguments 
    
    print("Comparing Files:", files[0], 'and', files[1])

    if check_md5(files[0]) == check_md5(files[1]):
        print('MD5 Matched')
    else: 
        print('MD5 Not Matched')

    if check_sha1(files[0]) == check_sha1(files[1]):
        print('SHA1 Matched')
    else: 
        print('SHA1 Not Matched')

    if check_sha512(files[0]) == check_sha512(files[1]):
        print('SHA512 Matched')
    else: 
        print('SHA512 Not Matched')
    