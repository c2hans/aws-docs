---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, see [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM Roles
<a name="iam-roles"></a>

 AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This guidance creates IAM roles that grant the guidance's AWS Lambda functions, Amazon API Gateway and Amazon Cognito or OpenID connect access to create regional resources.

## Amazon VPC
<a name="amazon-vpc"></a>

 This guidance optionally deploys a web console within your VPC. You can isolate access to the web console via Bastion hosts, VPNs, or Direct Connect. You can create [VPC endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html) to let traffic between your Amazon VPC and AWS services not leave the Amazon network to satisfy the compliance requirements.

## Security groups
<a name="security-groups"></a>

 The security groups created in this guidance are designed to control and isolate network traffic between the guidance components. We recommend that you review the security groups and further restrict access as needed once the deployment is up and running.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

 This guidance optionally deploys a web console hosted in an Amazon S3 bucket and Amazon API Gateway. To help reduce latency and improve security, this guidance includes an Amazon CloudFront distribution with an Origin Access Control (OAC), which is a CloudFront user that provides public access to the guidance's website bucket contents. For more information, refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the Amazon CloudFront Developer Guide.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Clickstream Analytics on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
