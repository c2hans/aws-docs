---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

IAM roles allow customers to assign granular access policies and permissions to services and users on AWS. This Guidance creates IAM roles and sets permissions in the respective accounts. This allows it to assume a defined role in the spoke and management account to make changes when necessary. The hub account assumes role in the Management account and spoke accounts.

## AWS WAF
<a name="aws-waf-security"></a>

AWS WAF is a web application firewall that helps protect web applications and APIs from attacks. It allows you to configure a web ACL that allows, blocks, or counts web requests based on configurable web security rules and conditions that you define. For more information, refer to [How AWS WAF Works](https://docs.aws.amazon.com/waf/latest/developerguide/how-aws-waf-works.html).

You can use AWS WAF to protect AWS AppSync from common security events, such as SQL injection and XSS. These types of security events could affect API availability and performance, compromise security, or consume excessive resources. For example, you can create rules to allow or block requests from specified IP address ranges, requests from Classless Inter-Domain Routing (CIDR) blocks, requests that originate from a specific country or Region, requests that contain malicious SQL code, or requests that contain malicious script.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

This Guidance deploys a static website [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an S3 bucket. To help reduce latency and improve security, it includes an Amazon CloudFront distribution with an origin access identity. This identity is a CloudFront user that helps provide public access to the website bucket contents. For more information, refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html).

## Amazon Cognito
<a name="amazon-cognito"></a>

This Guidance creates Amazon Cognito user accounts for signing in to the web UI. It also grants the administrator and the read-only users with the appropriate permissions to control user access to data.

**Important**
If you connect an external identity provider through SAML, every user from your identity provider will have read access to the web UI. To prevent giving read access to all users by default, modify the `cognito-trigger` Lambda function deployed by this stack. For more information, see [Configuring Lambda function options](https://docs.aws.amazon.com/lambda/latest/dg/configuration-function-common.html).
