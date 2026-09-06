---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/features-and-benefits.html
---

# Features and benefits
<a name="features-and-benefits"></a>

The Account Assessment for AWS Organizations solution provides the following features.

## Access the solution using a web UI
<a name="access-the-solution-using-a-web-ui"></a>

This solution provides a web UI to help you view scan results. For more details, see [Use the solution](use-the-solution.md).

## Identify enabled services with AWS Organizations
<a name="identify-enabled-services-with-aws-organizations"></a>

In your AWS Organization, you can enable more than 30 compatible AWS services to perform operations across all of the AWS accounts. This solution finds enabled services and delegated admin accounts per service (if activated).

## Explore your policies to find actions and conditions
<a name="explore-your-policies-to-find-actions-and-conditions"></a>

This feature allows you to search through all the policies across your AWS Organization to find specific conditions and actions. In case an action is deprecated you need to remove or update a given action or condition across all accounts or a specific set of accounts, you can quickly find and review the policies in the solutions UI, and update them across your environment to meet your needs.

The policies included in the scans are identity-based policies, resource-based policies, and organization-based policies (such as service control policies). The daily scan will store representations of all the policies in your environment in DynamoDB on a daily basis, so you can search through them, and find the attributes you are looking for in the solution’s web UI.

## Assess IAM policy conditions
<a name="assess-iam-policy-conditions"></a>

The `Condition` policy element lets you use keys to specify conditions for when a policy is in effect. You can use specific keys to compare the identifier or path of the requesting [principal’s](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html#intro-structure-principal) Organization in AWS Organizations with the identifier specified in the policy. This helps you identify existing conditions and dependencies. If desired, you can use [global condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html). This solution scans conditions in the following types of policies and presents them for your review in the solution’s web UI.

### Assume role (trust relationship) conditions
<a name="assume-role-trust-relationship-conditions"></a>

With IAM roles, you can establish trust relationships between your trusting account (the account that owns the resource) and other AWS trusted accounts (the accounts that contain the users that need to access the resource). In this trust relationship, you can use condition keys to grant permissions to any principal in your AWS Organization.

### Identity-based policy conditions
<a name="identity-based-policy-conditions"></a>

 [Identity-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) are attached to a user, group, or role. Use these policies to specify permissions for a given identity.

### Resource-based policy conditions
<a name="resource-based-policy-conditions"></a>

 [Resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html) are attached to a resource. Use these policies to specify who has access to the resource and what actions they can perform on it. For example, you can attach resource-based policies to [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) buckets, [Amazon Simple Queue Service](https://aws.amazon.com/sqs/) (Amazon SQS) queues, [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC) endpoints, and [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) encryption keys.

The following table provides a list of services supported by this solution.

| AWS service | Policy type |
| --- | --- |
|  [Amazon API Gateway](https://aws.amazon.com/api-gateway)  | Resource-based |
|  [AWS Backup](https://aws.amazon.com/backup)  | Resource-based |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation)  | Resource-based |
|  [AWS CodeArtifact](https://aws.amazon.com/codeartifact)  | Resource-based |
|  [AWS CodeBuild](https://aws.amazon.com/codebuild)  | Resource-based |
|  [AWS Config](https://aws.amazon.com/config)  | Resource-based |
|  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr) (Amazon ECR) | Resource-based |
|  [Amazon Elastic File System](https://aws.amazon.com/efs) (Amazon EFS) | Resource-based |
|  [AWS Elemental MediaStore](https://aws.amazon.com/mediastore)  | Resource-based |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge)  | Resource-based |
|  [AWS Glue](https://aws.amazon.com/glue)  | Resource-based |
|  [AWS Identity and Access Management](https://aws.amazon.com/iam) (IAM) | Identity-based |
|  [AWS IoT Core](https://aws.amazon.com/iot-core)  | Resource-based |
|  [AWS Key Management Service](https://aws.amazon.com/kms) (AWS KMS) | Resource-based |
|  [AWS Lambda](https://aws.amazon.com/lambda)  | Resource-based |
|  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service)  | Resource-based |
|  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager)  | Resource-based |
|  [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo/)  | Resource-based |
|  [Amazon Simple Email Service](https://aws.amazon.com/ses) (Amazon SES) | Resource-based |
|  [Amazon Simple Notification Service](https://aws.amazon.com/sns) (Amazon SNS) | Resource-based |
|  [Amazon Simple Queue Service](https://aws.amazon.com/sqs) (Amazon SQS) | Resource-based |
|  [Amazon Simple Storage Service](https://aws.amazon.com/s3) (Amazon S3) | Resource-based |
|  [Amazon S3 Glacier](https://aws.amazon.com/s3/storage-classes/glacier/)  | Resource-based |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager) ([AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html)) | Resource-based |
|  [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc) (Amazon VPC) ([VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html#concepts-service-consumers)) | Resource-based |
| AWS Resource Access Manager (Amazon RAM) | Resource-based |
| Amazon EventBridge Schemas | Resource-based |
| AWS Systems Manager Incident Manager Contacts | Resource-based |
| Amazon Lex | Resource-based |
| ACM-PCA (AWS Certificate Manager Private Certificate Authority) | Resource-based |
