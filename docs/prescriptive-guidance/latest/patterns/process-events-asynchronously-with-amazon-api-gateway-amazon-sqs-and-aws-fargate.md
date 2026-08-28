---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate.html
---

# Process events asynchronously with Amazon API Gateway, Amazon SQS, and AWS Fargate
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate"></a>

*Andrea Meroni, Mariem Kthiri, Nadim Majed, Alessandro Trisolini, and Michael Wallner, Amazon Web Services*

## Summary
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-summary"></a>

[Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) is a fully managed service that developers can use to create, publish, maintain, monitor, and secure APIs at any scale. It handles the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls.

An important service quota of API Gateway is the integration timeout. The timeout is the maximum time in which a backend service must return a response before the REST API returns an error. The hard limit of 29 seconds is generally acceptable for synchronous workloads. However, that limit represents a challenge for those developers who want to use API Gateway with asynchronous workloads.

This pattern shows an example architecture to process events asynchronously using API Gateway, Amazon Simple Queue Service (Amazon SQS) and AWS Fargate. The architecture supports running processing jobs without duration restrictions, and it uses a basic REST API as the interface.

[Projen](https://pypi.org/project/projen/) is used to set up the local development environment and to deploy the example architecture to a target AWS account, in combination with the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/cli.html), [Docker](https://docs.docker.com/get-docker/), and [Node.js](https://nodejs.org/en/download/). Projen automatically sets up a [Python](https://www.python.org/downloads/) virtual environment with [pre-commit](https://pre-commit.com/) and the tools that are used for code quality assurance, security scanning, and unit testing. For more information, see the [Tools](#process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-tools) section.

## Prerequisites and limitations
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ The following tools installed on your workstation:
  + [AWS Cloud Development Kit (AWS CDK) Toolkit](https://docs.aws.amazon.com/cdk/v2/guide/cli.html) version 2.85.0 or later
  + [Docker](https://docs.docker.com/get-docker/) version 20.10.21 or later
  + [Node.js](https://nodejs.org/en/download/) version 18 or later
  + [Projen](https://pypi.org/project/projen/) version 0.71.111 or later
  + [Python](https://www.python.org/downloads/) version 3.9.16 or later

**Limitations**
+ Concurrent jobs are limited to 500 tasks per minute, which is the maximum number of tasks that Fargate can provision.

## Architecture
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-architecture"></a>

The following diagram shows the interaction of the jobs API with the `jobs` Amazon DynamoDB table, the event-processing Fargate service, and the error-handling AWS Lambda function. Events are stored in an Amazon EventBridge event archive.

![Architecture diagram with description following the diagram.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/8a03149c-8f34-4593-84d5-accc1800a0a2/images/5e1071aa-4fbc-495c-bc22-8e62a32a136b.png)

A typical workflow includes the following steps:

1. You authenticate against AWS Identity and Access Management (IAM) and obtain security credentials.

1. You send an HTTP `POST` request to the `/jobs` jobs API endpoint, specifying the job parameters in the request body.

1. The jobs API, which is an API Gateway REST API, returns to you an HTTP response that contains the job identifier.

1. The jobs API sends a message to the SQS queue.

1. Fargate pulls the message from the SQS queue, processes the event, and then puts the job results in the `jobs` DynamoDB table.

1. You send an HTTP `GET` request to the `/jobs/{jobId}` jobs API endpoint, with the job identifier from step 3 as `{jobId}`.

1. The jobs API queries the `jobs` DynamoDB table to retrieve the job results.

1. The jobs API returns an HTTP response that contains the job results.

1. If the event processing fails, the SQS queue sends the event to the dead-letter queue (DLQ).

1. An EventBridge event initiates the error-handling function.

1. The error-handling function puts the job parameters in the `jobs` DynamoDB table.

1. You can retrieve the job parameters by sending an HTTP `GET` request to the `/jobs/{jobId}` jobs API endpoint.

1. If the error handling fails, the error-handling function sends the event to an EventBridge archive.

   You can replay the archived events by using EventBridge.

## Tools
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) helps you run containers without needing to manage servers or Amazon Elastic Compute Cloud (Amazon EC2) instances. It’s used in conjunction with Amazon Elastic Container Service (Amazon ECS).
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.

**Other tools**
+ [autopep8](https://github.com/hhatto/autopep8) automatically formats Python code based on the Python Enhancement Proposal (PEP) 8 style guide.
+ [Bandit](https://bandit.readthedocs.io/en/latest/) scans Python code to find common security issues.
+ [Commitizen](https://commitizen-tools.github.io/commitizen/) is a Git commit checker and `CHANGELOG` generator.
+ [cfn-lint](https://github.com/aws-cloudformation/cfn-lint) is an AWS CloudFormation linter
+ [Checkov](https://github.com/bridgecrewio/checkov) is a static code-analysis tool that checks infrastructure as code (IaC) for security and compliance misconfigurations.
+ [jq](https://stedolan.github.io/jq/download/) is a command-line tool for parsing JSON.
+ [Postman](https://www.postman.com/) is an API platform.
+ [pre-commit](https://pre-commit.com/) is a Git hooks manager.
+ [Projen](https://github.com/projen/projen) is a project generator.
+ [pytest](https://docs.pytest.org/en/7.2.x/index.html) is a Python framework for writing small, readable tests.

**Code repository**

This example architecture code can be found in the GitHub [Asynchronous Processing with API Gateway and SQS](https://github.com/aws-samples/asynchronous-event-processing-api-gateway-sqs-cdk) repository.

## Best practices
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-best-practices"></a>
+ This example architecture doesn't include monitoring of the deployed infrastructure. If your use case requires monitoring, evaluate adding [CDK Monitoring Constructs](https://constructs.dev/packages/cdk-monitoring-constructs) or another monitoring solution.
+ This example architecture uses [IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html) to control the access to the jobs API. Anyone authorized to assume the `JobsAPIInvokeRole` will be able to invoke the jobs API. As such, the access control mechanism is binary. If your use case requires a more complex authorization model, evaluate using a different [access control mechanism](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html).
+ When a user sends an HTTP `POST` request to the `/jobs` jobs API endpoint, the input data is validated at two different levels:
  + API Gateway is in charge of the first [request validation](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html).
  + The event processing function performs the second request.

    No validation is performed when the user does an HTTP `GET` request to the `/jobs/{jobId}` jobs API endpoint. If your use case requires additional input validation and an increased level of security, evaluate [using AWS WAF to protect your API](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html).

## Epics
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the repository locally, run the following command:<pre>git clone https://github.com/aws-samples/asynchronous-event-processing-api-gateway-sqs-cdk.git</pre> | DevOps engineer |
| Set up the project. | Change the directory to the repository root, and set up the Python virtual environment and all the tools by using [Projen](https://github.com/projen/projen):<pre>cd asynchronous-event-processing-api-gateway-api-gateway-sqs-cdk<br />npx projen</pre> | DevOps engineer |
| Install pre-commit hooks. | To install pre-commit hooks, do the following:1. Activate the [Python virtual environment](https://docs.python.org/3/library/venv.html):<pre>source .env/bin/activate</pre><br />2. Install the [pre-commit](https://pre-commit.com/) hooks:<pre>pre-commit install<br />pre-commit install --hook-type commit-msg</pre> | DevOps engineer |

### Deploy the example architecture
<a name="deploy-the-example-architecture"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Bootstrap AWS CDK. | To bootstrap [AWS CDK](https://aws.amazon.com/cdk/) in your AWS account, run the following command:<pre>AWS_PROFILE=$YOUR_AWS_PROFILE npx projen bootstrap</pre> | AWS DevOps |
| Deploy the example architecture. | To deploy the example architecture in your AWS account, run the following command:<pre>AWS_PROFILE=$YOUR_AWS_PROFILE npx projen deploy</pre> | AWS DevOps |

### Test the architecture
<a name="test-the-architecture"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install test prerequisites. | Install on your workstation the [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), [Postman](https://www.postman.com/downloads/), and [jq](https://jqlang.github.io/jq/).<br />Using [Postman](https://www.postman.com/downloads/) to test this example architecture is suggested but not mandatory. If you choose an alternative API testing tool, make sure that it supports [AWS Signature Version 4 authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html), and refer to the exposed API endpoints that can be inspected by [exporting the REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-export-api.html). | DevOps engineer |
| Assume the `JobsAPIInvokeRole`. | [Assume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html) the `JobsAPIInvokeRole` that was printed as output from the `deploy` command:<pre>CREDENTIALS=$(AWS_PROFILE=$<YOUR_AWS_PROFILE> aws sts assume-role \<br />--no-cli-pager \<br />--role-arn $<JOBS_API_INVOKE_ROLE_ARN> \<br />--role-session-name JobsAPIInvoke)<br />export AWS_ACCESS_KEY_ID=$(cat $CREDENTIALS | jq ‘.Credentials’’.AccessKeyId’)<br />export AWS_SECRET_ACCESS_KEY=$(cat $CREDENTIALS | jq ‘.Credentials’’.SecretAccessKey’)<br />export AWS_SESSION_TOKEN==$(cat $CREDENTIALS | jq ‘.Credentials’’.SessionToken’)</pre> | AWS DevOps |
| Configure Postman. | + To import the Postman collection that's included in the repository, follow the instructions in the [Postman documentation](https://learning.postman.com/docs/getting-started/importing-and-exporting/importing-data/#import-postman-data).<br />+ Set the `JobsAPI` [variables](https://learning.postman.com/docs/sending-requests/variables/variables/) with the following values:`accessKey` ‒ The value of the `Credentials.AccessKeyId` attribute from the `assume-role` command.`baseUrl` ‒ The value of the `JobsApiJobsAPIEndpoint` output from the `deploy` command, without the trailing slash.`region` ‒ The value of the AWS Region where you deployed the example architecture.`seconds` ‒ The value of the input parameter for the example job. It must be a positive integer.`secretKey` ‒ The value of the `Credentials.SecretAccessKey` attribute from the `assume-role` command.`sessionToken` ‒ The value of the `Credentials.SessionToken` attribute from the `assume-role` command. | AWS DevOps |
| Test the example architecture. | To test the example architecture, send requests to the jobs API. For more information, see the [Postman documentation](https://learning.postman.com/docs/getting-started/first-steps/sending-the-first-request/#send-an-api-request). | DevOps engineer |

## Troubleshooting
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Destruction and subsequent redeployment of the example architecture fails because the [Amazon CloudWatch Logs log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) `/aws/apigateway/JobsAPIAccessLogs` already exists. | 1. If necessary, [export your log data to Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html).<br />2. Delete the CloudWatch Logs log group `/aws/apigateway/JobsAPIAccessLogs`.<br />3. Redeploy the example architecture. |
| Destruction and subsequent redeployment of the example architecture fails because the [CloudWatch Logs log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) `/aws/ecs/EventProcessingServiceLogs` already exists. | 1. If necessary, [export your log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html).<br />2. Delete the CloudWatch Logs log group `/aws/ecs/EventProcessingServiceLogs.`<br />3. Redeploy the example architecture. |

## Related resources
<a name="process-events-asynchronously-with-amazon-api-gateway-amazon-sqs-and-aws-fargate-resources"></a>
+ [API Gateway mapping template and access logging variable reference](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html)
+ [How do I integrate an API Gateway REST API with Amazon SQS and resolve common errors?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-rest-api-sqs-errors/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
