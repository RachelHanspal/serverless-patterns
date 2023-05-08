import json

from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit

metrics = Metrics(namespace="CWMApp", service="CWMApp-Lambda")


@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event, context):
    metrics.add_metric(name="SuccessfulGreetings", unit=MetricUnit.Count, value=1)
    return {
        'statusCode': 200,
        'body': "Hello world"
    }
