from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_cloudwatch as cw,
    aws_iam as iam, Duration,
    aws_lambda_python_alpha as alambda_,
    aws_apigateway as apigw,
)
from constructs import Construct


class LambdaCwDashboardCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        managed_policy_insights = iam.ManagedPolicy.from_aws_managed_policy_name(
            'CloudWatchLambdaInsightsExecutionRolePolicy')
        managed_policy_basic_exec = iam.ManagedPolicy.from_aws_managed_policy_name(
            'service-role/AWSLambdaBasicExecutionRole')

        lambda_role = iam.Role(self,
                               id='cdk-lambda-role',
                               assumed_by=iam.ServicePrincipal(
                                   'lambda.amazonaws.com'),
                               managed_policies=[managed_policy_insights, managed_policy_basic_exec])

        lambdaLayer_insights = lambda_.LayerVersion.from_layer_version_arn(self, "Cw-inisghts-layer",
                                                                           layer_version_arn="arn:aws:lambda:us-east-1:580247275435:layer:LambdaInsightsExtension:21"
                                                                           )

                               

        lambda_handler = alambda_.PythonFunction(self, "MyFunction",
                                                 entry="./lambda/",  # required
                                                 runtime=lambda_.Runtime.PYTHON_3_9,  # required
                                                 index="handler.py",  # optional, defaults to 'index.py'
                                                 handler="lambda_handler",
                                                 layers=[lambdaLayer_insights]
                                                 )
        #optional apigateway
        apigw.LambdaRestApi(self, 'Endpoint', handler = lambda_handler)
        

        dimensions_function_name = {
            "function_name": lambda_handler.function_name
        }

        dimensions_service = {
            "service": "CWMApp-Lambda"
        }

        title_widget = cw.TextWidget(
            markdown="# Dashboard: {}".format(lambda_handler.function_name),
            height=1,
            width=24
        )
        innvocation_widget_1 = cw.GraphWidget(title="Invocations",
                                              left=[
                                                  lambda_handler.metric_invocations()],
                                              width=24)
        
        memory_metric = cw.Metric(metric_name="memory_utilization", namespace="LambdaInsights", statistic="avg",
                                  dimensions_map=dimensions_function_name, period=Duration.seconds(10))

        innvocation_widget_2 = cw.GraphWidget(title="Memory Utilization - From LambdaInsights",
                                              left=[memory_metric],
                                              width=24)
        
        successful_greetings = cw.Metric(metric_name="SuccessfulGreetings", namespace="CWMApp", statistic="sum",
                                  dimensions_map=dimensions_service, period=Duration.seconds(10))
        
        innvocation_widget_3 = cw.GraphWidget(title="Count - From Custom Metrics",
                                              left=[successful_greetings],
                                              width=24)

        dashboard = cw.Dashboard(self, "MyFirstDashboard",
                                 dashboard_name="LambdaCDKDashboard",
                                 ).add_widgets(title_widget, innvocation_widget_1, innvocation_widget_2, innvocation_widget_3)

