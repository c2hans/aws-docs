---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit the [AWS Security Center](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

IAM roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. Multiple roles are required to run Innovation Sandbox on AWS and discover resources in AWS accounts.

## IAM Identity Center and SAML authentication
<a name="iam-identity-center"></a>

AWS IAM Identity Center provides a central way to manage access to multiple AWS accounts and business applications using SAML 2.0-based authentication. The solution uses an Amazon Cognito user pool federated to IAM Identity Center as the SAML service provider. You sign in to the web UI with your existing corporate credentials, so you don’t need to manage separate accounts or passwords. After sign-in, the web UI obtains temporary IAM credentials from a Cognito identity pool and signs API requests with those credentials. You do not manage any long-lived application secrets for authentication.

The solution API can also be accessed programmatically; for details, see [Programmatic access (machine-to-machine)](m2m-access.md).

## AWS Key Management Service
<a name="kms"></a>

This solution creates four KMS Customer Managed Keys (one for each stack - AccountPool, IDC, Data, and Compute) to encrypt various AWS resources. The encrypted services include Amazon CloudWatch Logs, Amazon Simple Queue Service (SQS) queues, Amazon EventBridge event buses, AWS Secrets Manager secrets, AWS CodeBuild projects, and Amazon DynamoDB tables.

Each CMK is specifically tailored to its stack’s requirements, with appropriate key policies that grant necessary permissions to relevant services and IAM roles. This approach of using separate CMKs per stack follows the principle of separation of concerns and allows for more granular control over encryption permissions across different components of the solution.

## AWS WAF
<a name="waf"></a>

In this solution, AWS WAF (Web Application Firewall) is implemented to protect the API Gateway endpoints through multiple layers of security controls. The solution creates a regional WAF web ACL that combines four AWS managed rule groups and two custom rules.

The default action of the web ACL is set to **allow** and the rule actions are set to **block**, so any request that does not satisfy all rules will be blocked. This comprehensive WAF configuration helps protect the API Gateway against common web exploits, malicious bots, and unauthorized access while allowing legitimate traffic from approved sources.

**Note**
WAF SizeRestrictions\_QUERYSTRING Rule Modification\*
The solution disables the `SizeRestrictions_QUERYSTRING` rule from the `AWSManagedRulesCommonRuleSet` to accommodate legitimate large pagination tokens from the AWS Organizations API. The GET `/accounts/unregistered` endpoint retrieves accounts from AWS Organizations, which can return pagination tokens that exceed the default WAF query string size limit when handling large numbers of accounts (>20).
This modification is necessary for the solution to function properly with large account pools. If you require additional query string size protection for other endpoints, you can manually implement a custom rule that excludes the `/accounts/unregistered` endpoint while applying size restrictions to other API endpoints.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

This solution deploys a web UI [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket that is distributed by Amazon CloudFront. To help reduce latency and improve security, this solution includes a CloudFront distribution with an origin access identity, which is a CloudFront user that provides public access to the solution website’s bucket contents. By default, the CloudFront distribution uses TLS 1.2 to enforce the highest level of security protocol. For more information, refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.

CloudFront activates additional security mitigations to append HTTP security headers to each viewer response. For more information, refer to [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/adding-response-headers.html).

This solution uses the default CloudFront certificate which has a minimum supported security protocol of TLS v1.0. To enforce the use of TLS v1.2 or TLS v1.3, you must use a custom SSL certificate instead of the default CloudFront certificate. For more information, refer to [How do I configure my CloudFront distribution to use an SSL/TLS certificate](https://aws.amazon.com/premiumsupport/knowledge-center/install-ssl-cloudfront/).

## Amazon DynamoDB
<a name="amazon-dynamodb"></a>

All user data stored in Amazon DynamoDB is encrypted at rest using customer managed keys (CMK) stored in AWS KMS.

## AWS Lambda
<a name="aws-lambda"></a>

By default, the Lambda functions are configured with the most recent stable version of the language runtime. No sensitive data or secrets are logged. Service interactions are carried out with the least required privilege. Roles that define these privileges are not shared between functions.

## Amazon CloudWatch Alarms
<a name="amazon-cloudwatch-alarms"></a>

The solution provides Amazon CloudWatch Alarms to monitor for Lambda errors, throttling, and execution duration.

To set up SNS notifications to detect changes in these alarms, refer to [Acting on alarm changes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Acting_Alarm_Changes.html). You can configure additional alarms based on metrics reported by the different services within the solution.

## Log retention and monitoring
<a name="log-retention-and-monitoring"></a>

By default, Innovation Sandbox retains all compute logs for 90 days in Amazon CloudWatch Logs. AWS recommends retaining security-relevant logs for 10 years to support compliance and forensic analysis requirements. You can modify the default log retention period by adjusting the `cloudWatchLogRetentionInDays` value in the CloudFormation template mapping before deployment.

All logs are encrypted at rest using AWS KMS customer-managed keys and are automatically archived to Amazon S3 for long-term retention following a multi-tier strategy (Amazon CloudWatch Logs → S3 Standard → S3 Glacier).

## AWS CloudTrail
<a name="aws-cloudtrail"></a>

AWS CloudTrail is not automatically enabled by the Innovation Sandbox solution. AWS recommends enabling organization-level CloudTrail in your Organization Management Account to monitor API calls and administrative actions across all accounts.

## Amazon S3 security features
<a name="amazon-s3-security"></a>

The solution uses Amazon S3 for storing cost reports, log archives, and operational data. By default, the solution only enables S3 access logging and versioning on critical buckets to reduce costs from redundant logs. AWS recommends enabling these features on all solution buckets for enhanced security monitoring if required for your compliance needs.

If desired, you can manually enable S3 access logging to monitor all bucket access, S3 versioning to protect against accidental deletion or modification, and S3 event notifications for real-time alerts on critical bucket operations.

## Custom client security considerations
<a name="custom-client-security"></a>

The Innovation Sandbox on AWS API allows certain free-text fields (such as lease template names and descriptions) to contain characters that may lead to cross-site scripting (XSS) vulnerabilities in insecure client implementations. The included React-based web client implements proper security controls and safely handles all user-provided data. If you develop a custom client application that integrates with the solution’s API, ensure your implementation includes appropriate input validation, output encoding, and XSS protection measures following secure coding practices for your chosen technology stack.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
