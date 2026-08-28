---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters deploys the following components in your AWS account.

 **Distributed Load Testing on AWS architecture**

![Distributed Load Testing on AWS architecture](http://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/images/architecture-diagram.png)

**Note**
AWS CloudFormation resources are created from AWS Cloud Development Kit (AWS CDK) constructs.

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1.  *(CloudFront \+ S3 hosting deployment option)* The Console User accesses the web console through [Amazon CloudFront](https://aws.amazon.com/cloudfront), which serves the [AWS Amplify](https://aws.amazon.com/amplify) application hosted in an [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) bucket.

1.  *(ALB \+ ECS Fargate hosting deployment option)* The Console User accesses the web console through an [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/), which routes traffic to the AWS Amplify application running on [Amazon Elastic Container Service](https://aws.amazon.com/ecs) (Amazon ECS) on [AWS Fargate](https://aws.amazon.com/fargate) inside an [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc) (Amazon VPC).

1.  *(Headless deployment option)* No public front end is deployed. The solution provides the web console as a downloadable ZIP in a private Amazon S3 bucket. The Console User can access the console from a self-hosted web server.

1. During initial configuration, the solution creates a default administrator user in the [Amazon Cognito](https://aws.amazon.com/cognito) user pool and sends an account creation email to the email address you provide. The Cognito user pool manages user access to the web console, the REST API, the CLI, and the MCP Server.

1.  [Amazon API Gateway](https://aws.amazon.com/api-gateway) invokes [AWS Lambda](https://aws.amazon.com/lambda) microservices that provide the business logic to manage test data and run the tests.

1. The microservices interact with Amazon S3, [Amazon DynamoDB](https://aws.amazon.com/dynamodb), and [Amazon EventBridge](https://aws.amazon.com/eventbridge) to store test scenario details and manage test schedules. When you schedule a test to run at a future time or on a recurring interval, the microservices create an EventBridge Scheduler schedule that invokes the microservice at the scheduled time.

1. To run a test, the microservices invoke [AWS Step Functions](https://aws.amazon.com/step-functions), which orchestrates the test execution.

1. EventBridge rules route Amazon ECS task and Step Functions failure events to a failure handler Lambda function.

1. Step Functions launches [Amazon Elastic Container Service](https://aws.amazon.com/ecs) (Amazon ECS) tasks on [AWS Fargate](https://aws.amazon.com/fargate) in each AWS Region you selected.

1. Each task runs within an [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc) (Amazon VPC) in the selected Region.

1. Load testing container uses an [Amazon Linux 2023](https://aws.amazon.com/linux/amazon-linux-2023/) base image with the [Taurus](https://gettaurus.org/) test automation framework installed. Taurus executes your JMeter, k6, Locust, or Single HTTP Endpoint test. For details on how each test framework is provisioned, refer to [Testing framework provisioning](back-end.md#framework-provisioning). The ALB \+ ECS option will use the web host container. The container images are hosted by AWS in an [Amazon Elastic Container Registry](https://aws.amazon.com/ecr) (Amazon ECR) public repository.

1. Each Fargate task writes its per-Region test results to Amazon S3 and emits logs to [Amazon CloudWatch](https://aws.amazon.com/cloudwatch). When all Regions complete, the microservices aggregate the results in DynamoDB.

1. If you enable the live data option, a Lambda function receives CloudWatch logs from Fargate tasks during the test.

1. The Lambda function publishes the logs to a topic in [AWS IoT Core](https://aws.amazon.com/iot-core) in the Region where the main stack is deployed. The web console subscribes to the topic to display real-time metrics while the test runs.

1.  *(Optional CLI access)* Users can install the DLT command-line interface (CLI) locally to interact with the solution from their terminal. The CLI authenticates through Cognito and calls the REST API directly, enabling scripted automation and CI/CD integration.
**Note**
The following steps describe the optional MCP Server integration for AI-assisted load testing analysis. This component is only deployed if you select the MCP Server option during solution deployment.

1. An MCP client (AI development tool) connects to the [Amazon Bedrock AgentCore Gateway](https://aws.amazon.com/bedrock/agentcore/) endpoint to access the Distributed Load Testing solution’s data through the Model Context Protocol. AgentCore Gateway validates the user’s Cognito authentication token to ensure authorized access to the MCP Server.

1. Upon successful authentication, AgentCore Gateway forwards the MCP tool request to the DLT MCP Server Lambda function.

1. The Lambda function calls the existing DLT REST API to retrieve the requested load testing data. It then returns the structured data to AgentCore Gateway, which sends it back to the MCP client for AI-assisted analysis and insights.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Distributed Load Testing on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
