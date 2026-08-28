---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/aws-services-in-this-solution.html
---

# AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |  |
| --- | --- | --- |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  |  **Prerequisite.** Deploy Cloud Migration Factory using CloudFormation templates. |  |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway/)  |  **Core.** Provides REST APIs to the whole solution, used to access backend data and initiate and manage migration automation tasks. |  |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** Provide the necessary services for you to log in to the web interface, perform the necessary administrative functions to manage the migration, and connect to third-party APIs to automate the migration process. |  |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Core.** EventBridge serves as the central event-driven communication backbone for asynchronous notifications between Lambda functions, enabling decoupled task orchestration, status updates, email notifications, and real-time UI updates during migration workflows. |  |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core.** Metadata store for all user and system managed data, accessed via Amazon API Gateways and Lambda functions. |  |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Core.** User authorization and authentication, optional federation with other IDPs is also achieved through Amazon Cognito. |  |
|  [Amazon Simple Queue Service](https://aws.amazon.com/sqs/)  |  **Supporting.** Provides dead letter queues (DLQs) for failed EventBridge-triggered Lambda invocations and asynchronous processing queue for GenAI WebSocket operations, ensuring reliable message delivery and error handling. |  |
|  [Amazon Simple Notification Service](https://aws.amazon.com/sns/)  |  **Supporting.** Delivers email notifications to migration team members for task status updates, manual approval requests, and task failures via configured SNS topics. |  |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** Supports the running of Cloud Migration Factory on AWS automation packages on the customer provided Automation server. |  |
|  [Amazon EC2](https://aws.amazon.com/ec2/)  |  **Supporting.** Automation server running AWS Systems Manager agents to allow running of automation packages. |  |
|  [Amazon Bedrock](https://aws.amazon.com/bedrock/)  |  **Supporting.** Automatically map headers in imported Excel/CSV files to schemas in Wave Planning Manager(WPM), and generate wave planning rules from natural language. |  |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Supporting.** Used in multiple areas of the solution, 1/ using the static web hosting feature of Amazon S3, it serves the main web interface(via Amazon CloudFront), 2/ logs and other automation outputs are stored in Amazon S3 by the solution. |  |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)  |  **Supporting.** When using the automation features of the solution, AWS Secrets Manager is used to securely store the credentials that are used to access migrating resources in order to run tasks and actions to facilitate and migrate workloads. |  |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Optional.** For standard deployments Amazon CloudFront provides the distribution of the web interface content from Amazon S3, making it highly available globally, and providing secure TLS access to the web interface content from anywhere. |  |
|  [AWS Application Migration Service (AWS MGN)](https://aws.amazon.com/application-migration-service/)  |  **Optional.** When performing rehost migrations of Windows or Linux workloads, Cloud Migration Factory on AWS uses AWS MGN to facilitate the system migration to Amazon EC2. |  |
|  [Amazon QuickSight](https://aws.amazon.com/quicksight/)  |  **Optional.** Allows for customizable migration dashboards to be created based on the data stored in the migration metastore held in Amazon DynamoDB, providing teams the data they need to track and report on their migrations. |  |
|  [AWS Glue](https://aws.amazon.com/glue/)  |  **Optional.** Regularly extracts data held in Amazon DynamoDB to Amazon S3, providing reporting data for use in Amazon Athena and Amazon QuickSight dashboards. |  |
|  [Amazon Athena](https://aws.amazon.com/athena/)  |  **Optional.** Provides access to reporting data extracted by AWS Glue from the migration metadata, allowing dashboards to be created using Amazon QuickSight. |  |
|  [AWS Web Application Firewall](https://aws.amazon.com/waf/)  |  **Optional.** Apply additional security on the endpoints for Amazon API Gateway and Amazon CloudFront to restrict access to specific devices based on source IP address or other access criteria. |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Cloud Migration Factory on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
