---
source_url: https://docs.aws.amazon.com/solutions/latest/video-on-demand-on-aws-foundation/security-1.html
---

# Security
<a name="security-1"></a>

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## Amazon S3 bucket policy
<a name="amazon-s3-bucket-policy"></a>

 The S3 buckets for MediaConvert output include a policy that allows access from CloudFront. Because the CloudFront endpoints are publicly accessible, the MediaConvert output bucket is also publicly accessible when accessed with CloudFront. For information on how to secure Amazon CloudFront, refer to [Serving private content with signed URLs and signed cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html) in the *Amazon CloudFront Developer Guide*.

## IAM roles
<a name="iam-roles"></a>

 IAM roles allow you to assign granular access policies and permissions to services and users on the AWS Cloud. This solution creates several IAM roles, including a role that grants MediaConvert access to Amazon S3. This role is necessary to allow the services to operate in your account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Video on Demand on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
