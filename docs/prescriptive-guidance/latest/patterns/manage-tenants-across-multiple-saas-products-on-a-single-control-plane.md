---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/manage-tenants-across-multiple-saas-products-on-a-single-control-plane.html
---

# Manage tenants across multiple SaaS products on a single control plane
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane"></a>

*Ramanna Avancha, Kishan Kavala, Anusha Mandava, and Jenifer Pascal, Amazon Web Services*

## Summary
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane-summary"></a>

This pattern shows how to manage tenant lifecycles across multiple software as a service (SaaS) products on a single control plane in the AWS Cloud. The reference architecture provided can help organizations reduce the implementation of redundant, shared features across their individual SaaS products and provide governance efficiencies at scale.

Large enterprises can have multiple SaaS products across various business units. These products often need to be provisioned for use by external tenants at different subscription levels. Without a common tenant solution, IT administrators must spend time managing undifferentiated features across multiple SaaS APIs, instead of focusing on core product feature development.

The common tenant solution provided in this pattern can help centralize the management of many of an organization's shared SaaS product features, including the following:
+ Security
+ Tenant provisioning
+ Tenant data storage
+ Tenant communications
+ Product management
+ Metrics logging and monitoring

## Prerequisites and limitations
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Knowledge of Amazon Cognito or a third-party identity provider (IdP)
+ Knowledge of Amazon API Gateway
+ Knowledge of AWS Lambda
+ Knowledge of Amazon DynamoDB
+ Knowledge of AWS Identity and Access Management (IAM)
+ Knowledge of AWS Step Functions
+ Knowledge of AWS CloudTrail and Amazon CloudWatch
+ Knowledge of Python libraries and code
+ Knowledge of SaaS APIs, including the different types of users (organizations, tenants, administrators, and application users), subscription models, and tenant isolation models
+ Knowledge of your organization's multi-product SaaS requirements and multi-tenant subscriptions

**Limitations**
+ Integrations between the common tenant solution and individual SaaS products aren’t covered in this pattern.
+ This pattern deploys the Amazon Cognito service in a single AWS Region only.

## Architecture
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane-architecture"></a>

**Target technology stack  **
+ Amazon API Gateway
+ Amazon Cognito
+ AWS CloudTrail
+ Amazon CloudWatch
+ Amazon DynamoDB
+ IAM
+ AWS Lambda
+ Amazon Simple Storage Service (Amazon S3)
+ Amazon Simple Notification Service (Amazon SNS)
+ AWS Step functions

**Target architecture **

The following diagram shows an example workflow for managing tenant lifecycles across multiple SaaS products on a single control plane in the AWS Cloud.

![Workflow for managing tenant lifecycles on a single control plane.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4306bc76-22a7-45ca-a107-43df6c6f7ac8/images/700faf4d-c28f-4814-96aa-2d895cdcb518.png)

 The diagram shows the following workflow:

1. An AWS user initiates tenant provisioning, product provisioning, or administration-related actions by making a call to an API Gateway endpoint.

1. The user is authenticated by an access token that’s retrieved from an Amazon Cognito user pool, or another IdP.

1. Individual provisioning or administration tasks are run by Lambda functions that are integrated with API Gateway API endpoints.

1. Administration APIs for the common tenant solution (for tenants, products, and users) gather all of the required input parameters, headers, and tokens. Then, the administration APIs invoke the associated Lambda functions.

1. IAM permissions for both the administration APIs and the Lambda functions are validated by the IAM service.

1. Lambda functions store and retrieve data from the catalogs (for tenants, products, and users) in DynamoDB and Amazon S3.

1. After permissions are validated, an AWS Step Functions workflow is invoked to perform a specific task. The example in the diagram shows a tenant provisioning workflow.

1. Individual AWS Step Functions workflow tasks are run in a predetermined workflow (state machine).

1. Any essential data that’s needed to run the Lambda function associated with each workflow task is retrieved from either DynamoDB or Amazon S3. Other AWS resources might need to be provisioned by using an AWS CloudFormation template.

1. If needed, the workflow sends a request to provision additional AWS resources for a specific SaaS product to that product’s AWS account.

1. When the request succeeds or fails, the workflow publishes the status update as a message to an Amazon SNS topic.

1. Amazon SNS is subscribed to the Step Functions workflow’s Amazon SNS topic.

1. Amazon SNS then sends the workflow status update back to the AWS user.

1. Logs of each AWS service’s actions, including an audit trail of API calls, are sent to CloudWatch. Specific rules and alarms can be configured in CloudWatch for each use case.

1. Logs are archived in Amazon S3 buckets for auditing purposes.

**Automation and scale**

This pattern uses a CloudFormation template to help automate the deployment of the common tenant solution. The template can also help you quickly scale the associated resources up or down.

For more information, see [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the *AWS CloudFormation User Guide*.

## Tools
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.
+ [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) helps you audit the governance, compliance, and operational risk of your AWS account.
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications you run on AWS in real time.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.

## Best practices
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane-best-practices"></a>

The solution in this pattern uses a single control plane to manage the onboarding of multiple tenants and to provision access to multiple SaaS products. The control plane helps administrative users manage four other, feature-specific planes:
+ Security plane
+ Workflow plane
+ Communication plane
+ Logging and monitoring plane

## Epics
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane-epics"></a>

### Configure the security plane
<a name="configure-the-security-plane"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Establish the requirements for your multi-tenant SaaS platform. | Establish detailed requirements for the following:+ Tenants<br />+ Users<br />+ Roles<br />+ SaaS products<br />+ Subscriptions<br />+ Profile exchanges | Cloud architect, AWS systems administrator |
| Set up the Amazon Cognito service. | Follow the instructions in [Getting started with Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-getting-started.html) in the *Amazon Cognito Developer Guide*. | Cloud architect |
| Configure the required IAM policies. | Create the required IAM policies for your use case. Then, map the policies to IAM roles in Amazon Cognito.<br />For more information, see [Managing access using policies](https://docs.aws.amazon.com/cognito/latest/developerguide/security-iam.html#security_iam_access-manage) and [Role-based access control](https://docs.aws.amazon.com/cognito/latest/developerguide/role-based-access-control.html) in the *Amazon Cognito Developer Guide*. | Cloud administrator, Cloud architect, AWS IAM security |
| Configure the required API permissions.  | Set up API Gateway access permissions by using IAM roles and policies, and Lambda authorizers.<br />For instructions, see the following sections of the *Amazon API Gateway Developer Guide*:+ [Control access to an API with IAM permissions](https://docs.aws.amazon.com/apigateway/latest/developerguide/permissions.html)<br />+ [Use API Gateway Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) | Cloud administrator, Cloud architect |

### Configure the data plane
<a name="configure-the-data-plane"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the required data catalogs. | 1. Create DynamoDB tables to store data for the user catalogs. Make sure that you include user attributes and roles. Also, make sure that you perform data modeling on the catalog tables to maintain the required and optional attributes for each user and role.<br />2. Create DynamoDB tables to store data for the product catalogs. Make sure that you model the specific use cases for your SaaS products.<br />3. Create DynamoDB tables to store data for the tenant catalogs. Make sure that you set up subscription models for tenants, products and licensing for multi-SaaS subscriptions, and tags.For more information, see [Setting up DynamoDB ](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/SettingUp.html)in the *Amazon DynamoDB Developer Guide*. | DBA |

### Configure the control plane
<a name="configure-the-control-plane"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create Lambda functions and API Gateway APIs to run required control plane tasks. | Create separate Lambda functions and API Gateway APIs to add, delete, and manage the following:+ Users<br />+ Tenants<br />+ Products<br />For more information, see [Using AWS Lambda with Amazon API Gateway](https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html) in the *AWS Lambda Developer Guide*. | App developer |

### Configure the workflow plane
<a name="configure-the-workflow-plane"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify the tasks that AWS Step Functions workflows must run. | Identify and document the detailed AWS Step Functions workflow requirements for the following:+ Users<br />+ Tenants<br />+ ProductsMake sure that key stakeholders approve the requirements. | App owner |
| Create the required AWS Step Functions workflows. | 1. Create the required workflows for users, tenants, and products in AWS Step Functions. For more information, see the [*AWS Step Functions Developer Guide*](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html).<br />2. Identify the retry and error handling mechanisms. For more information, see [Handling errors, retries, and adding alerting to Step Function State Machines](https://aws.amazon.com/blogs/developer/handling-errors-retries-and-adding-alerting-to-step-function-state-machine-executions/) on the AWS Blog.<br />3. Implement the workflow steps by using Lambda functions. For instructions, see [Creating a Step Functions state machine that uses Lambda](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-creating-lambda-state-machine.html) in the *AWS Step Functions Developer Guide*.<br />4. Integrate any external services with AWS Step Functions as needed.<br />5. Maintain each workflow’s status in a DynamoDB table and communicate each workflow’s status by using Amazon SNS. | App developer, Build lead |

### Configure the communication plane
<a name="configure-the-communication-plane"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create Amazon SNS topics. | Create Amazon SNS topics to receive notifications about the following:+ Workflow statuses<br />+ Errors<br />+ Retries<br />For more information, see [Creating an SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-topic.html) in the *Amazon SNS Developer Guide*. | App owner, Cloud architect |
| Subscribe endpoints to each Amazon SNS topic. | To receive messages published to an Amazon SNS topic, you must subscribe an endpoint to each topic.<br />For more information, see [Subscribing to an Amazon SNS topic](https://docs.aws.amazon.com/sns/latest/dg/sns-create-subscribe-endpoint-to-topic.html) in the *Amazon SNS Developer Guide*. | App developer, Cloud architect |

### Configure the logging and monitoring plane
<a name="configure-the-logging-and-monitoring-plane"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Activate logging for each component of the common tenant solution. | Activate logging at the component level for each resource in the common tenant solution that you created.<br />For instructions, see the following:+ [How do I turn on CloudWatch Logs for troubleshooting my API Gateway REST API or WebSocket API?](https://aws.amazon.com/premiumsupport/knowledge-center/api-gateway-cloudwatch-logs/) (AWS Knowledge Center)<br />+ [Logging using CloudWatch Logs](https://docs.aws.amazon.com/step-functions/latest/dg/cw-logs.html) (*AWS Step Functions Developer Guide*)<br />+ [AWS Lambda function logging in Python](https://docs.aws.amazon.com/lambda/latest/dg/python-logging.html) (*AWS Lambda Developer Guide*)<br />+ [Logging and monitoring in Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/monitoring.html) (*Amazon Cognito Developer Guide*)<br />+ [Monitoring with Amazon CloudWatch](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/monitoring-cloudwatch.html) (*Amazon DynamoDB Developer Guide*)You can consolidate logs for each resource into a centralized logging account by using IAM policies. For more information, see [Centralized logging and multiple-account security guardrails](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/centralized-logging-and-multiple-account-security-guardrails.html). | App developer, AWS systems administrator, Cloud administrator |

### Provision and deploy the common tenant solution
<a name="provision-and-deploy-the-common-tenant-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create CloudFormation templates. | Automate the deployment and maintenance of the full common tenant solution and all its components by using CloudFormation templates.<br />For more information, see the [*AWS CloudFormation User Guide*](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html). | App developer, DevOps engineer, CloudFormation developer |

## Related resources
<a name="manage-tenants-across-multiple-saas-products-on-a-single-control-plane-resources"></a>
+ [Control access to a REST API using Amazon Cognito user pools as authorizer](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html) (*Amazon API Gateway Developer Guide*)
+ [Use API Gateway Lambda authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html) (*Amazon API Gateway Developer Guide*)
+ [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) (*Amazon Cognito Developer Guide*)
+ [Cross-account cross-Region CloudWatch console](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html) (*Amazon CloudWatch User Guide*)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
