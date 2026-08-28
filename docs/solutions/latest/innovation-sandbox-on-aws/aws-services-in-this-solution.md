---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/aws-services-in-this-solution.html
---

# AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core**. This solution uses CloudFront with an Amazon S3 bucket as the origin. This restricts access to the Amazon S3 bucket so that it is not publicly accessible and prevents direct access from the bucket. |
|  [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)  |  **Core**. The solution federates web application authentication through Amazon Cognito to IAM Identity Center using SAML 2.0, and uses IAM Identity Center to manage role-based access to sandbox accounts for solution users. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Core**. The solution uses an Amazon Cognito user pool (federated to IAM Identity Center using SAML 2.0) to authenticate web application users, and a Cognito identity pool to vend the temporary IAM credentials the web UI uses to sign API requests. |
|  [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)  |  **Core**. The solution uses AWS AppConfig to store the account cleanup configuration used by the account cleaner. This includes the AWS Nuke configuration and the cleanup validator exclusion configuration. |
|  [AWS Resource Explorer](https://aws.amazon.com/resource-explorer/)  |  **Core**. The solution uses Resource Explorer to enumerate resources in sandbox accounts before cleanup, after cleanup, and after cooldown — providing post-cleanup validation and resource usage metrics. |
|  [AWS Organizations](https://aws.amazon.com/organizations/)  |  **Core**. The solution uses AWS Organizations to centrally manage and govern multiple AWS accounts required by the solution. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core**. This solution uses DynamoDB to store state for the solution, including sandbox account, lease, and lease template records, and the solution’s global configuration settings. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** This solution uses serverless Lambda functions, with Node.js to handle API calls. |
|  [AWS CodeBuild](https://aws.amazon.com/codebuild/)  |  **Core**. This solution uses CodeBuild for the account cleanup process. |
|  [Amazon Simple Storage Service](https://aws.amazon.com/s3/)  |  **Core.** This solution uses Amazon S3 for frontend and backend storage purposes. |
|  [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/)  |  **Core**. This solution uses AWS KMS to manage creation and control of encryption keys, required to encrypt various AWS resources used in the solution. |
|  [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/)  |  **Core**. This solution uses Amazon SQS to manage message queues. |
|  [AWS Step Functions](https://aws.amazon.com/step-functions/)  |  **Core**. This solution uses AWS Step Functions to orchestrate blueprint deployment workflows, lease assignment processing, and the account tag activation workflow. |
|  [AWS Billing and Cost Management](https://aws.amazon.com/aws-cost-management/)  |  **Supporting.** This solution activates account cost allocation tags in AWS Billing and Cost Management so that you can analyze sandbox costs by tag in Cost Explorer, AWS Budgets, and Cost and Usage Reports. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Supporting.** This solution uses CloudWatch to collect and visualize real-time logs, metrics, and event data in automated cases. Additionally, you can monitor the deployed solution’s resource usage and performance issues. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** This solution uses AWS Systems Manager for solution configuration and sharing cross account/stack parameters using the RAM service. |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Supporting.** This solution uses AWS WAF to protect the Amazon API Gateway from common exploits and bots that can affect availability, compromise security, or consume excessive resources. |
|  [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)  |  **Supporting.** This solution uses AWS Cost Explorer to retrieve cost and usage data for accounts and leases. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
