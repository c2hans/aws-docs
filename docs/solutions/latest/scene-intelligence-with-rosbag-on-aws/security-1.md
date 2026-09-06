---
source_url: https://docs.aws.amazon.com/solutions/latest/scene-intelligence-with-rosbag-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

IAM roles allow this solution to assign granular access policies and permissions to services and users on the AWS Cloud. This solution creates IAM roles that grant the solution’s Lambda functions access to manage Regional resources.

## VPC security groups
<a name="vpc-security-groups"></a>

The solution creates security groups designed to control and isolate network traffic between the Lambda functions, Amazon EC2 instances, and remote virtual private network (VPN) endpoints. We recommend that you review the security groups and further restrict access as needed once the deployment is up and running.
