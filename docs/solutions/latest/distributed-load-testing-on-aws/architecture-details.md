---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and [AWS services that make up this solution](#aws-services-in-this-solution) and the architecture details on how these components work together.

The Distributed Load Testing on AWS solution consists of three high-level components: a [front end](front-end.md), a [backend](back-end.md), and an optional [MCP Server](MCP-Server.md).

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

The following AWS services are included in this solution:

| AWS service | Description |
| --- | --- |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  **Core.** Hosts REST API endpoints in the solution. |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Core.** Manages deployments for the solution infrastructure. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core (default deployment only).** Serves the web content hosted in Amazon S3 when using the default CloudFront \+ S3 hosting option. |
|  [Elastic Load Balancing (Application Load Balancer)](https://aws.amazon.com/elasticloadbalancing/)  |  **Core (ALB \+ ECS Fargate deployment only).** Serves the web console when using the ALB \+ ECS Fargate deployment option. |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Supporting, Optional (ALB \+ ECS Fargate deployment only).** Provides web application firewall protection for the ALB and ECS hosted web console. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Core.** Stores the solution logs and metrics. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Core.** Handles user management and authentication for the API. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core.** Stores deployment information and tests scenario details and results. |
|  [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)  |  **Core.** Deploys and manages independent Amazon ECS tasks on AWS Fargate containers. |
|  [AWS Fargate](https://aws.amazon.com/fargate/)  |  **Core.** Hosts solution's Amazon ECS containers |
|  [AWS Identity and Access Management](https://aws.amazon.com/iam/)  |  **Core.** Handles user role and permissions management. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** Provides logic for APIs implementation, tests results parsing, and launching workers/leader tasks. |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  **Core.** Orchestrates the provisioning of Amazon ECS containers on AWS Fargate tasks in the specified regions |
|  [AWS Amplify](https://aws.amazon.com/amplify/)  |  **Supporting.** Provides a web console powered by [AWS Amplify](https://aws.amazon.com/amplify). |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Supporting**. Routes Amazon ECS task and Step Functions failure events to failure handler Lambda functions, and schedules tests to automatically begin at a specified date or on recurring dates using EventBridge Scheduler. |
|  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)  |  **Supporting**. Hosts the container image in a public ECR repository. |
|  [AWS IoT Core](https://aws.amazon.com/iot-core/)  |  **Supporting.** Enables viewing live data for a running test by subscribing to the corresponding topic in AWS IoT Core. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** Provides application-level resource monitoring and visualization of resource operations and cost data. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Supporting.** Hosts the static web content, logs, metrics, and tests data. |
|  [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)  |  **Supporting.** Contains the solution's Amazon ECS containers running on AWS Fargate. |
|  [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)  |  **Supporting, Optional.** Hosts the solution's optional Remote Model Context Protocol (MCP) Server for AI agent integration with API. |
