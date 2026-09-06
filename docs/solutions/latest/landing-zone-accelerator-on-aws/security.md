---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This solution creates IAM roles that grant the solution’s CodePipeline pipelines read/write access to their respective artifact S3 buckets, source code repositories, and run CodeBuild projects. Additional IAM roles are created that grant CodeBuild projects to write to Amazon CloudWatch Logs log groups and create Regional resources.

## AWS KMS keys
<a name="aws-kms-keys"></a>

AWS KMS helps you create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications. This solution uses AWS KMS keys to turn on encryption at rest for the applicable services it deploys. In a default installation, these keys will rotate automatically once per year. More information about the key management infrastructure for this solution is outlined in [Architecture details](architecture-details.md).
