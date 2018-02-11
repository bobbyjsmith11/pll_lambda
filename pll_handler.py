#!/usr/bin/env python
from pll import pll_calcs
import json

def my_handler_raw(event, context):
    """ requires the following keys in event
        first_name
        last_name
        what_i_like
    """
    # print(event)
    # q_str = event['queryStringParameters']
    # message = "Hello {} {}! Gosto muito da sua {}".format(q_str['first_name'], q_str['last_name'], q_str['what_i_like'])
    message = "Hello {} {}! Gosto muito da sua {}".format(event['first_name'], event['last_name'], event['what_i_like'])
    return {
        "message": message
        }
    # return {
    #     'statusCode': 200,
    #     'headers': {'x-custom-header': "my custom header value"},
    #     'body': message
    #     }

def my_handler_wrapped(event, context):
    """ requires the keys in event['body']
        first_name
        last_name
        what_i_like
    """
    d = json.loads(event['body'])
    message = "Hello {} {}! Gosto muito da sua {}".format(d['first_name'], d['last_name'], d['what_i_like'])

    return {
        'statusCode': 200,
        'headers': {'x-custom-header': "my custom header value"},
        'body': message
        }

def hello_world(event, context):
    """ does not require json input
    """
    return {
        'statusCode': 200,
        'headers': {'x-custom-header': "my custom header value"},
        'body': "Hello World"
        }

def power_sum_handler(event, context):
    """
    """
    p1 = float(event['power1'])
    p2 = float(event['power2'])
    result = pll_calcs.power_sum([p1, p2])
    return {
        'result': result
    }

def solve_for_comp_handler(event, context):
    """ invoke pll_calcs.solveForComponents and return dict of components with values
    """
    fc = float(event['fc'])
    pm = float(event['pm'])
    kphi = float(event['kphi'])
    kvco = float(event['kvco'])
    N = float(event['N'])
    gamma = float(event['gamma'])
    loop_type = event['loop_type']
    
    # returns a dict already
    res = pll_calcs.solveForComponents(fc, pm, kphi, kvco, N, gamma, loop_type=loop_type)
    return res