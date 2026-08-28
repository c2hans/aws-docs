---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/security-iam-awsmanpol.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# AWS managed policies for AWS Toolkit for .NET Refactoring
<a name="security-iam-awsmanpol"></a>

To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.

## AWS managed policy: AWSRefactoringToolkitFullAccess
<a name="AWSRefactoringToolkitFullAccess"></a>

Use this policy to test your application on AWS when you modernize your application with the AWS Toolkit for .NET Refactoring extension for Microsoft Visual Studio. Attach the policy to your local AWS profile. The policy grants permissions to upload application artifacts and download the resulting artifacts from S3. It grants permissions to build the application into a container image using AWS CodeBuild and store and retrieve the images in Amazon Elastic Container Registry (Amazon ECR). In addition, it allows for the deployment of the application to container services on AWS, such as Amazon Elastic Container Service (Amazon ECS), the optional creation of Amazon VPC resources, and the optional connection to existing infrastructure, such as AWS Directory Service.

To view the permissions for this policy, see [AWSRefactoringToolkitFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSRefactoringToolkitFullAccess.html) in the *AWS Managed Policy Reference*.

**Permission details**

This policy includes permissions for the following services:
+ Application Transformation – Allows Toolkit for .NET Refactoring to perform compatibility assessments along with containerization and deployment operations.
+ Amazon CloudWatch – Allows Toolkit for .NET Refactoring to create log groups and store log output from Toolkit for .NET Refactoring operations and your applications.
+ Amazon Elastic Compute Cloud (Amazon EC2) – Allows Toolkit for .NET Refactoring to create and modify security groups, internet gateways, and Amazon VPC.
+ Amazon Elastic Container Registry (Amazon ECR) – Allows Toolkit for .NET Refactoring to create and read your Amazon ECR repository and to tag resources.
+ Amazon Elastic Container Service (Amazon ECS) – Allows Toolkit for .NET Refactoring to run your container images as tasks in Amazon ECS and to facilitate debugging.
+ Amazon Simple Storage Service (Amazon S3) – Allows Toolkit for .NET Refactoring to list and manage objects from Amazon S3 buckets that are used by Toolkit for .NET Refactoring.
+ CloudFormation – Allows Toolkit for .NET Refactoring to deploy the infrastructure components of CodeBuild and application deployment in the form of CloudFormation stacks.
+ AWS CodeBuild – Allows Toolkit for .NET Refactoring to allocate resources for CodeBuild projects and start builds.
+ AWS Identity and Access Management (IAM) – Allows Toolkit for .NET Refactoring to verify which roles are passed to other AWS services.
+ AWS Key Management Service (AWS KMS) – Allows Toolkit for .NET Refactoring to utilize user-provided KMS keys across AWS services for encryption.
+ AWS Systems Manager (Systems Manager) – Allows Toolkit for .NET Refactoring to manage Systems Manager parameters and communicate with Amazon ECS tasks.

## AWS managed policy: AWSRefactoringToolkitSidecarPolicy
<a name="AWSRefactoringToolkitSidecarPolicy"></a>

This policy is used by the Amazon ECS tasks that are created to run a test application on AWS with the AWS Toolkit for .NET Refactoring extension for Microsoft Visual Studio. The policy grants permissions to download application artifacts from S3 and to communicate the status of the task using AWS Systems Manager.

To view the permissions for this policy, see [AWSRefactoringToolkitSidecarPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSRefactoringToolkitSidecarPolicy.html) in the *AWS Managed Policy Reference*.

## Toolkit for .NET Refactoring updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for Toolkit for .NET Refactoring since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Toolkit for .NET Refactoring Document history page.

| Change | Description | Date |
| --- | --- | --- |
| [AWSRefactoringToolkitFullAccess](#AWSRefactoringToolkitFullAccess) – Updated policy | Modified the permissions for CreateTags by adding conditions that use the aws:CallVia condition key. | April 9, 2025 |
| [AWSRefactoringToolkitFullAccess](#AWSRefactoringToolkitFullAccess) – Updated policy | Added permissions for the `cloudformation:TagResource` and `cloudformation:UntagResource` actions to manage resource tags on stacks created for AWS App2Container. | March 25, 2024 |
| [AWSRefactoringToolkitFullAccess](#AWSRefactoringToolkitFullAccess) – Updated policy | Added permissions for `application-transformation` actions and KMS permissions for resources matching `ForAnyValue:StringLike` with `"kms:ResourceAliases": "alias/application-transformation*"`. Changed permissions for EC2, ECR, ECS, and CloudWatch Logs to scope them to the `application-transformation` request and resource tag. | November 18, 2023 |
| [AWSRefactoringToolkitFullAccess](#AWSRefactoringToolkitFullAccess) – Updated policy | Added `ListStacks` permissions. | March 22, 2023 |
| [AWSRefactoringToolkitFullAccess](#AWSRefactoringToolkitFullAccess) – Updated policy | Added tagging permissions that allow new accounts to perform the `CreateLogGroup` action.  | December 15, 2022 |
| [AWSRefactoringToolkitSidecarPolicy](#AWSRefactoringToolkitSidecarPolicy) – Updated policy | Added permissions to open a data channel to transfer files to the customer's container. | October 29, 2022 |
| [AWSRefactoringToolkitFullAccess](#AWSRefactoringToolkitFullAccess) – New policy | Added the `AWSRefactoringToolkitFullAccess` policy. | October 25, 2022 |
| [AWSRefactoringToolkitSidecarPolicy](#AWSRefactoringToolkitSidecarPolicy) – New policy | Added the AWSRefactoringToolkitSidecarPolicy policy. | October 25, 2022 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
