from datetime import timedelta
import requests
import json


def open_session():
    # LOGIN TO INFA

    # is used to get icSessionId
    url = 'https://dm-em.informaticacloud.com/ma/api/v2/user/login'

    myobj = {
        "@type":"login",
        "username":"TestServiceAccount",
        "password":"***"
    }

    # x is response from INFA
    x = requests.post(url, json = myobj)
    # make response as json to be able to read as dictionary
    json_obj = x.json()

    # informatica session id
    session_id = json_obj["icSessionId"]    
    return session_id


def run_a_task(session_id):
    # START A TASK

    url_job = 'https://emw1.dm-em.informaticacloud.com/saas/api/v2/job'
    
    # get session_id from another function
    
    Headers = {"icSessionId": session_id}

    myobj = {
        "@type":"job",
        "taskId":"0119EH0I000000000002",
        "taskType":"DSS"
    }

    y = requests.post(url_job, headers=Headers, json = myobj)
    print(y)



def close_session(session_id):
    # CLOSE SESSION

    url_logout = "https://dm-em.informaticacloud.com/ma/api/v2/user/logout"

    myobj = {
        "@type":"logout"
    }
    z = requests.post(url_logout, json = myobj)
    return "session is closed"

session_id = open_session()
run_a_task(session_id)
close_session(session_id)
