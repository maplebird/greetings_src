#!/usr/bin/env python

import requests
import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(description='Check Hazelcast cluster statistics.')
    parser.add_argument("-u", "--url", type=str,
                        help="URL of environment to test")
    parser.add_argument("-p", "--port", type=str,
                        help="URL of environment to test")
    return parser.parse_args()


def get_url(args):
    if args.port:
        port = args.port
    else:
        port = str(80)
    url = args.url
    url = 'http://' + url + ':' + port
    return url


def run_tests(url):
    # Test 1: GET query
    test1 = requests.get(url)
    print test1.content
    test2 = requests.post(url, "vlad")
    print test2

def main():
    args = get_args()
    url = get_url(args)
    run_tests(url)

if __name__ == "__main__":
    main()