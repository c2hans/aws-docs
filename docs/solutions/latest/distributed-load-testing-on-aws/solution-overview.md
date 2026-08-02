---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/solution-overview.html
---

# Automate the testing of your software applications at scale
<a name="solution-overview"></a>

Distributed Load Testing on AWS helps you automate performance testing of your software applications at scale to identify bottlenecks before you release your application. This solution simulates thousands of connected users generating HTTP requests at a sustained rate without the need to provision servers.

This solution leverages [Amazon Elastic Container Service (Amazon ECS) on AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) to deploy containers that run your load test simulations and offers the following capabilities:
+ Deploy Amazon ECS on AWS Fargate containers that run independently to test the load capacity of your application.
+ Simulate tens of thousands of concurrent users across multiple AWS Regions generating requests at a continuous pace.
+ Customize your application tests using [JMeter](https://jmeter.apache.org/), [k6](https://k6.io/), [Locust](https://locust.io/) test scripts, or simple HTTP endpoint configuration. For security considerations about the bundled frameworks, refer to [Third-party testing frameworks](security-1.md#third-party-testing-frameworks).
+ Schedule load tests to run immediately, at a future date and time, or on a recurring schedule.
+ Run multiple load tests concurrently across different scenarios and regions.

This implementation guide provides an overview of the Distributed Load Testing on AWS solution, its reference architecture and components, considerations for planning the deployment, and configuration steps for deploying the solution to the Amazon Web Services (AWS) Cloud. It includes links to an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template that launches and configures the AWS services required to deploy this solution using AWS best practices for security and availability.

The intended audience for using this solution's features and capabilities in their environment includes IT infrastructure architects, administrators, and DevOps professionals who have practical experience architecting in the AWS Cloud.

Use this navigation table to quickly find answers to these questions:

| If you want to . . . | Read . . . |
| --- | --- |
| Know the cost for running this solution.<br />The estimated cost for running this solution in the US East (N. Virginia) Region is USD $ 30.90 per month for AWS resources. |  [Cost](cost.md)  |
| Understand the security considerations for this solution. |  [Security](security-1.md)  |
| Know how to plan for quotas for this solution. |  [Quotas](quotas.md)  |
| Know which AWS Regions support this solution. |  [Supported AWS Regions](plan-your-deployment.md#supported-aws-regions)  |
| Learn about the optional MCP Server for AI-assisted load testing analysis. |  [MCP Server integration](mcp-server-integration.md)  |
| Learn about the available web console hosting options (CloudFront \+ S3, ALB \+ ECS Fargate, or headless). |  [Deploy the solution](deploy-the-solution.md)  |
| View or download the AWS CloudFormation template included in this solution to automatically deploy the infrastructure resources (the "stack") for this solution. |  [AWS CloudFormation template](aws-cloudformation-template.md)  |
| Access the source code and optionally use the AWS Cloud Development Kit (AWS CDK) to deploy the solution. |  [GitHub repository](https://github.com/aws-solutions/distributed-load-testing-on-aws)  |
