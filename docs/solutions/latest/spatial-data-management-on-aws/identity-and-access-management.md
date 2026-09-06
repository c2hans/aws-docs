---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/identity-and-access-management.html
---

# Identity and Access Management
<a name="identity-and-access-management"></a>

The solution implements fine-grained access control using multiple AWS services.

## How SDMA Works with IAM
<a name="how-sdma-works-with-iam"></a>

The solution uses AWS Identity and Access Management (IAM) for:

 **Service Roles**
+ Lambda execution roles with least-privilege permissions
+ API Gateway invocation roles
+ CloudFormation deployment roles
+ EventBridge target invocation roles

 **Resource Policies**
+ S3 bucket policies restrict access to authorized principals
+ DynamoDB table policies control access to specific tables
+ KMS key policies define who can use encryption keys
+ SQS queue policies control message producers and consumers

 **Cross-Service Access**
+ Lambda functions assume IAM roles to access other AWS services
+ API Gateway uses IAM authorization for programmatic access
+ CloudFront uses Origin Access Identity (OAI) to access S3

## Authentication
<a name="authentication"></a>

 **User Authentication**
+  **Amazon Cognito User Pool**: Manages user identities and authentication
+ Sign-in options: Email or username
+ Multi-factor authentication (MFA): Optional, using time-based one-time passwords (TOTP)
+ Password policy requirements:
+ Minimum 8 characters
+ Must include uppercase, lowercase, digits, and symbols
+ Temporary passwords valid for 1 day
+ Account recovery: Email-only recovery
+ Device tracking: Challenges required on new devices, remembered only on user prompt
+ Managed login: Cognito Hosted UI (version 2) for OAuth 2.0 flows
+ User groups: Pre-configured "SpatialDataManagementAdministrators" group for library ownership

 **Application Authentication**
+  **API Keys**: API Gateway API keys for rate limiting and usage tracking
+  **IAM Credentials**: AWS Signature Version 4 for programmatic access
+  **Temporary Credentials**: AWS STS for direct S3 access

## Authorization
<a name="authorization"></a>

 **Fine-Grained Access Control**
+  **Amazon Verified Permissions**: Cedar policy language for resource-based authorization
+ Library-level access control
+ Project-level access control
+ Asset-level access control
+ Role-based access (Owner, Manager, Contributor, Viewer)
+ Attribute-based access control (ABAC)

 **API Authorization**
+  **Cognito Authorizer**: JWT token validation for user requests
+  **IAM Authorizer**: AWS Signature Version 4 (SigV4) for service-to-service calls
+  **Lambda Authorizer**: Custom authorization logic when needed

 **Resource Membership**
+  **Members Table**: Tracks user and group membership for resources
+  **Hierarchical Permissions**: Library permissions cascade to projects and assets
+  **Explicit Deny**: Deny rules take precedence over allow rules

## AWS Managed Policies
<a name="aws-managed-policies"></a>

The solution uses the following AWS managed policies:
+  **AWSLambdaBasicExecutionRole**: CloudWatch Logs access for Lambda functions
+  **AWSLambdaVPCAccessExecutionRole**: ENI management for VPC Lambda functions
+  **AWSXRayDaemonWriteAccess**: X-Ray tracing for Lambda functions
+  **CloudWatchLambdaInsightsExecutionRolePolicy**: Lambda Insights monitoring

## Using Service-Linked Roles
<a name="using-service-linked-roles"></a>

The solution uses AWS service-linked roles for:

 **Amazon OpenSearch Serverless**
+ Role: `AWSServiceRoleForAmazonOpenSearchServerless`
+ Purpose: Allows OpenSearch Serverless to manage VPC endpoints and network interfaces
+ Created automatically when OpenSearch collection is created

 **AWS Lambda**
+ Role: `AWSServiceRoleForLambdaReplicator`
+ Purpose: Allows Lambda to replicate functions across regions (if enabled)
+ Created automatically when Lambda replication is configured

 **Amazon API Gateway**
+ Role: `AWSServiceRoleForAPIGateway`
+ Purpose: Allows API Gateway to push logs to CloudWatch
+ Created automatically when API Gateway logging is enabled
