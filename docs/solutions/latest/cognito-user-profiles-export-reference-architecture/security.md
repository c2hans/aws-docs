---
source_url: https://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This shared model reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit the [AWS Security Center](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

AWS Identity and Access Management (IAM) roles enable customers to assign granular access policies and permissions to services and users in the AWS Cloud. This guidance creates IAM roles that grant the guidance’s AWS Lambda functions access to create regional resources.
