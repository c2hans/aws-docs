---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on how these components work together.

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

|  **AWS service**  |  **Description**  |
| --- | --- |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Core**. Used to deploy the solution and develop MCS internal and Third-Party Modules. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core**. Used to cache and deliver the MCS web console hosted in Amazon S3. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Core**. Provides authentication to the MCS web console and API. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core**. Used to store information about MCS modules and the state of the modules. |
|  [Amazon EC2](https://aws.amazon.com/ec2/)  |  **Core**. Used to run the workstations managed by the MCS Workstation Management module. MCS uses Amazon EC2 Image Builder to build Windows and Linux Amazon Machine Images (AMIs) used in the solution. |
|  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)  |  **Core**. Used to manage connections between MCS Workstation Management module and Amazon EC2 workstations. |
|  [IAM](https://aws.amazon.com/iam/)  |  **Core**. Used to authorize access to MCS using roles to manage resources effectively. MCS resources are limited by roles and policies defined in IAM and in Cognito user pools. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core**. Handles the processing logic for adding, updating, editing, or deleting MCS modules and storing sensitive information in Secrets Manager. |
|  [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/)  |  **Core**. Used as a database for the Leostream Broker EC2 instances. |
|  [Amazon Route 53](https://aws.amazon.com/route53/)  |  **Core**. Used to manage domain resolution to load balancer addresses. |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  **Core**. Used to store module parameters that contain sensitive information. |
|  [AWS Service Catalog](https://aws.amazon.com/servicecatalog/)  |  **Core**. Used to manage the portfolio of MCS modules and to provision the CloudFormation stack when modules are enabled. |
|  [Amazon VPC](https://aws.amazon.com/vpc/)  |  **Core**. Used to deploy an isolated virtual networking environment to build the MCS studio. Users can create a new VPC or import an existing one. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Supporting.** Used for monitoring the solution and logs. |
|  [Amazon EventBridge Event Bus](https://aws.amazon.com/eventbridge/event-bus/)  |  **Supporting.** Listens to CloudFront changes and invokes Lambda to update the state of MCS modules in DynamoDB. |
|  [Amazon EventBridge Pipe](https://aws.amazon.com/eventbridge/pipes/)  |  **Supporting.** Used to process and transform operational metrics from Amazon SQS and deliver them anonymously to an API destination for monitoring. |
|  [Amazon SQS](https://aws.amazon.com/sqs/)  |  **Supporting.** Used to deliver operational metrics to EventBridge Pipe |
|  [Amazon Simple Storage Service](https://aws.amazon.com/s3/)  |  **Supporting.** Provides object storage for content used in the MCS web console. |
|  [AWS Systems Manager Parameter Store](http://aws.amazon.com/systems-manager/)  |  **Supporting.** Provides application-level resource monitoring, visualization of resource operations, and secrets management. |
|  [Amazon DCV](https://aws.amazon.com/hpc/dcv/)  |  **Supporting**. Used to connect users securely to the workstations. |
|  [AWS Directory Service](https://aws.amazon.com/directoryservice/)  |  **Optional**. Used to deploy an instance of [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html). |
|  [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/)  |  **Optional**. Used to deploy a fully managed shared file system built on Windows Server. |
|  [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/)  |  **Optional**. Used to deploy a fully managed shared file system built on Lustre. |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  **Optional**. Used to register and deregister MCS Third-Party Modules. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
