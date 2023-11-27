import aws_cdk as core
import aws_cdk.assertions as assertions



from lambda_cw_dashboard_cdk.lambda_cw_dashboard_cdk_stack import LambdaCwDashboardCdkStack

def test_lambda_created():
    app = core.App()
    stack = LambdaCwDashboardCdkStack(app, "lambda-cw-dashboard-cdk")
    template = assertions.Template.from_stack(stack)


    template.has_resource_properties("AWS::Lambda::Function", {
        "Handler": "lambda_function.lambda_handler",
        "Runtime": "python3.8"
    })

