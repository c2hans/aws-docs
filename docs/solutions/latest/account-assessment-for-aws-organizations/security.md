---
source_url: https://docs.aws.amazon.com/solutions/latest/account-assessment-for-aws-organizations/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

**Warning**
Make sure to follow the guideline in the [AWS account structure section](aws-accounts.md) when choosing hub and spoke accounts to install the guidance in.

## IAM roles
<a name="iam-roles"></a>

IAM roles allow you to assign granular access policies and permissions to services and users on the AWS Cloud. This guidance creates IAM roles that grant the guidance’s Lambda functions access to create Regional resources.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

This guidance deploys a web console [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket. To help reduce latency and improve security, this guidance includes a CloudFront distribution with an origin access identity, which is a CloudFront user that provides public access to the guidance’s website bucket contents. For more information, refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.

**Note**
If you require Transport Layer Security (TLS) 1.2, you can configure a custom domain (also called an alternate domain name) in [CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html) and [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html#apigateway-custom-domain-tls-version-how-to).

## Amazon DynamoDB
<a name="dynamodb-security"></a>

All user data stored in DynamoDB is encrypted at rest using encryption keys stored in AWS KMS. We recommend enforcing [AWS Managed Keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) because they will allow you to audit key usage. Refer to [Managing encrypted tables in DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/encryption.tutorial.html) for more information.

## AWS WAF
<a name="aws-waf"></a>

AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It allows you to configure a web ACL that allows, blocks, or counts web requests based on configurable web security rules and conditions that you define. For more information, refer to [How AWS WAF Works](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html).

You can use AWS WAF to protect your API Gateway API from common web exploits, such as SQL injection and XSS attacks. These types of attacks could affect API availability and performance, compromise security, or consume excessive resources. For example, you can create rules to allow or block requests from specified IP address ranges, requests from Classless Inter-Domain Routing (CIDR) blocks, requests that originate from a specific country or Region, requests that contain malicious SQL code, or requests that contain malicious script.
