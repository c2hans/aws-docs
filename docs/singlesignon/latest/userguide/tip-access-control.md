---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-access-control.html
---

# Control access with the identity context

You can control access based on the identity context in two ways. We recommend group-based access control where available, because group membership changes in your identity source apply automatically.

1. [Group-based access control (recommended)](#tip-access-group)

1. [IAM policy-based access control with the username](#tip-access-iam)

## Group-based access control (recommended)
<a name="tip-access-group"></a>

Services that have their own grant engines, such as AWS Lake Formation and Amazon S3 Access Grants, can grant access directly to IAM Identity Center groups. When a user's group membership changes in your identity source, their access changes with it, and you don't need to update policies when someone joins or leaves. For setup guidance, see [Setting up AWS Lake Formation with IAM Identity Center](tip-tutorial-lf.md) and [Setting up Amazon S3 Access Grants with IAM Identity Center](tip-tutorial-s3.md). For the latest information about Lake Formation support, see the [AWS Lake Formation Developer Guide](https://docs.aws.amazon.com/lake-formation/latest/dg/connect-lf-identity-center.html).

## IAM policy-based access control with the username
<a name="tip-access-iam"></a>

IAM can evaluate the propagated username and other IAM Identity Center context keys in identity-based policies, resource-based policies, role trust policies, service control policies (SCPs), and resource control policies (RCPs). Because these policies name individual users, you must update them when someone joins, leaves, or is renamed. For examples, see [Use the identity context for IAM policies](simplified-tip-iam-policies.md).
