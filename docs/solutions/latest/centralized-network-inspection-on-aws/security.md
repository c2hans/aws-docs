---
source_url: https://docs.aws.amazon.com/solutions/latest/centralized-network-inspection-on-aws/security.html
---

# Security
<a name="security"></a>

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

 [AWS Identity and Access Management](https://aws.amazon.com/iam/) (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud.

## AWS Key Management Service
<a name="aws-key-management-service"></a>

 This guidance creates two [AWS Key Management Service](https://aws.amazon.com/kms/) (AWS KMS) encryption keys:
+  One of the keys is used to encrypt objects in the S3 artifact and source code buckets, and CodeBuild projects.
+  The second key is used to encrypt the Network Firewall log destinations, which depends on whether you select `Amazon CloudWatch` or `Amazon S3 bucket` for the **Select the type of log destination for the Network Firewall** parameter.

 By default, only IAM roles provisioned by this guidance have permission to perform encrypt or decrypt operations with this key. Automatic key rotation is enabled by default.
