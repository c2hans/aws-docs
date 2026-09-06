---
source_url: https://docs.aws.amazon.com/solutions/latest/scalable-analytics-using-apache-druid-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. The guidance creates IAM roles that grant the guidance’s constructs to access Regional resources provisioned by the guidance, such as:
+ IAM role used by the EC2 instances that run Druid workloads to read and write data in S3 buckets.
+ IAM roles used by AWS CloudFormation custom resources to retrieve the password from the Druid `system_user` secret within AWS Secrets Manager.

By default, all Amazon S3 buckets for the guidance have the following configuration:
+ Blocked all public access
+ Versioning enabled
+ Access log enabled
+ Encryption at rest by an AWS KMS customer managed key

Additionally, the Amazon S3 buckets are also configured with a default buckets policy that deny all non-HTTPS requests to ensure data in transit encryption.

## AWS WAF
<a name="aws-waf"></a>

This guidance incorporates the deployment of AWS Web Application Firewall (WAF) when the Application Load Balancer (ALB) is configured to be internet-facing. AWS WAF is used to enhance the security of the web applications exposed through the ALB by providing protection against various web-based threats and attacks.

## AWS Key Management Service keys
<a name="aws-key-management-service-keys"></a>

The guidance allows you to provide your own AWS KMS keys to encrypt stored data in the S3 bucket and Aurora cluster. We recommend referring to the [security best practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html) to enhance the protection of your encryption keys.

## Data protection
<a name="data-protection"></a>

All data committed to the guidance is encrypted at rest using [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) customer managed keys. This includes data stored in the following services:
+ Amazon S3
+ Amazon Aurora
+ Amazon SNS

Communication between the guidance’s different components is over HTTPS to ensure data encryption in transit.
