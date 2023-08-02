# AWS Cloudwatch Dashboard using Lambda and CDK in Python
This pattern helps build CloudWatch Dashboard with AWS Lambda Metrics. The Dashboard built with 4 widgets,
1. Invocations - from AWS/Lambda Namespace
2. memory_utilization - from LambdaInsights Namespace
3. Custom Metrics (Count of successful greetings) - from Custom Namespace

Learn more about this pattern at Serverless Land Patterns: https://serverlessland.com/patterns/

Important: this application uses various AWS services and there are costs associated with these services after the Free Tier usage - please see the [AWS Pricing page](https://aws.amazon.com/pricing/) for details. You are responsible for any AWS costs incurred. No warranty is implied in this example.

## Requirements

* [Create an AWS account](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html) if you do not already have one and log in. The IAM user that you use must have sufficient permissions to make necessary AWS service calls and manage AWS resources.
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) installed and configured
* [Git Installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [AWS Cloud Development Kit](https://docs.aws.amazon.com/cdk/latest/guide/cli.html) (AWS CDK) installed

## Deployment Instructions

1. Create a new directory, navigate to that directory in a terminal and clone the GitHub repository:
    ``` 
    git clone https://github.com/aws-samples/serverless-patterns
    ```
2. Change directory to the pattern directory:
    ```
    cd serverless-patterns/lambda_cw_dashboard_python
    ```
3. Deploy the stack to your default AWS account and region.
    ```
    cdk deploy
    ```
## How it works
A CloudWatch dashboard was created to display metrics from the Lambda function. The dashboard includes the following meterics.
- Default metrics in the Default Namespace
- Insight metrics that were collected by instrumenting the Docker Lambda function with Lambda Insight 
- Custom metrics were sent to CloudWatch by Lambda using Powertools. The Lambda function has custom metrics successful requests.
**Lambda**: Lambda is a serverless computing service offered by AWS. It allows you to run code without provisioning or managing servers. Lambda functions are triggered by events, such as HTTP requests, database changes, or file uploads.
**CloudWatch**: CloudWatch is a monitoring service offered by Amazon Web Services (AWS). It collects and stores metrics from AWS resources, such as EC2 instances, RDS databases, and Lambda functions. CloudWatch can be used to track the performance, health, and usage of AWS resources.
**Lambda Insight**: Lambda Insight is a feature of Lambda that allows you to collect and analyze metrics from your Lambda functions. Lambda Insight can be used to track the performance, health, and usage of your Lambda functions.
**LambdaPowertools**: Powertools is a set of tools that can be used to collect and send custom metrics to CloudWatch. Powertools can be used with a variety of AWS services, including Lambda, EC2, and RDS.
**Custom metrics**: Custom metrics are metrics that are not collected by default by CloudWatch. Custom metrics can be collected by using Powertools or by writing your own code.
## Testing
1. Invoke the Lambda 
2. Go to Cloudwatch dashboard and check to see if metrics have been recorded on the dashboard (note: it takes a few minutes to load the graph in case of cold start)



# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
