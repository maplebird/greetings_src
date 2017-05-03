#!/usr/bin/env python

import requests
import argparse
import sys
import json

final_result = []


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


# Grabs content of rest API response
def get_content(json_var):
    response = json.loads(json_var)
    return response['content']


# Run all unit tests
def run_tests(url):

    # Test 1: Server 200 OK
    resp = requests.get(url).status_code
    if resp == 200:
        print 'Test 1 successful, server is up'
        final_result.append(1)
    else:
        final_result.append(0)
        print 'Test 1 failed.  Server response:'
        print resp

    # Test 2: GET query
    resp = requests.get(url).content
    content = get_content(resp)
    if 'Hello, World!' in content:
        print 'Test 2 successful, GET returns Hello, World!'
        final_result.append(1)
    else:
        final_result.append(0)
        print 'Test 2 failed.  Server returned:'
        print content
    # Add new tests below


# Show final results
def show_results():
    successful = 0
    total = len(final_result)

    for result in final_result:
        successful += result
    print "%s out of %s tests were successful." % (successful, total)

    # Fail if any unit tests fail
    if successful < total:
        sys.exit(1)


def main():
    args = get_args()
    url = get_url(args)
    run_tests(url)
    show_results()


if __name__ == "__main__":
    main()