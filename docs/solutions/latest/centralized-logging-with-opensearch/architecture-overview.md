---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram with description and [AWS Well-Architected design considerations](aws-well-architected-pillars.md).

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters builds the following environment in the AWS Cloud.

 **Architecture diagram, as described in text that follows.**

![image1](http://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/images/image1.png)

This solution deploys the AWS CloudFormation template in your AWS Cloud account and completes the following settings.

1.  [Amazon CloudFront](https://aws.amazon.com/cloudfront) distributes the frontend web UI assets hosted in an [Amazon S3](https://aws.amazon.com/s3) bucket.

1.  [Amazon Cognito](https://aws.amazon.com/cognito) user pool or OpenID Connector (OIDC) can be used for authentication.

1.  [AWS AppSync](https://aws.amazon.com/appsync) provides the backend GraphQL APIs.

1.  [Amazon DynamoDB](https://aws.amazon.com/dynamodb) stores the solution-related information as the backend database.

1.  [AWS Lambda](https://aws.amazon.com/lambda) interacts with other AWS Services to process the core logic of managing log pipeline, log agents, and obtains information updated in DynamoDB tables.

1.  [AWS Step Functions](https://aws.amazon.com/step-functions) orchestrates the on-demand [AWS CloudFormation](https://aws.amazon.com/cloudformation) deployment of a set of predefined stacks for log pipeline management. The log pipeline stacks deploy separate AWS resources and are used to collect and process logs and ingest them into [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service) for further analysis and visualization.

1. Service Log Pipeline or Application Log Pipeline is provisioned on demand via Centralized Logging with the OpenSearch console.

1.  [AWS Systems Manager](https://aws.amazon.com/systems-manager) and [Amazon EventBridge](https://aws.amazon.com/eventbridge) manage log agents for collecting logs from application servers, such as installing log agents (Fluent Bit) for application servers and monitoring the health status of the agents.

1.  [Amazon EC2](https://aws.amazon.com/ec2) or [Amazon EKS](https://aws.amazon.com/eks) installs Fluent Bit agents and uploads log data to the application log pipeline.

1. Application log pipelines read, parse, process application logs, and ingest them into Amazon OpenSearch Service domains or Light Engine.

1. Service log pipelines read, parse, process AWS service logs and ingest them into Amazon OpenSearch Service domains or Light Engine.

**Note**
After deploying the solution, you can use [AWS WAF](https://aws.amazon.com/waf/) to protect CloudFront or AWS AppSync. Moreover, you can follow this [guide](https://docs.aws.amazon.com/appsync/latest/devguide/WAF-Integration.html) to configure your AWS WAF settings to prevent GraphQL schema introspection.

This solution supports two types of log pipelines: **Service Log Analytics Pipeline** and **Application Log Analytics Pipeline**, and two types of log analytics engines: **OpenSearch Engine** and **Light Engine**. Architecture details for pipelines and Light Engine are described in:
+  [Service Log Analytics Pipeline](service-log-analytics-pipeline.md)
+  [Application Log Analytics Pipeline](application-log-analytics-pipeline.md)
+  [Light Engine](light-engine.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Centralized Logging with OpenSearch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
