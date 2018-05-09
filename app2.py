import boto3
import json
import time


sfn  = boto3.client('stepfunctions', region_name='us-east-1')

while True:
    # check stepfunctions for a task
    response  = sfn.get_activity_task(
        activityArn='arn:aws:states:us-east-1:303710525837:activity:runApp2',
        workerName='runApp2'
    )

    if response is not None:
        try:
            taskToken, taskInput  = response['taskToken'], response['input']

            # convert to Python dict and make some changes to the data
            data = json.loads(taskInput)

            newComment = data['Comment'] + ' From App2: Yes!  I believe it is...'
            data['Comment'] = newComment

            # convert data back to JSON
            taskInput = json.dumps(data)

            sfn.send_task_success(taskToken=taskToken, output=taskInput)

        except:
            sfn.send_task_failure(taskToken=taskToken, error='error', cause='Oops!  Something went wrong')

    else:
        time.sleep(3)
