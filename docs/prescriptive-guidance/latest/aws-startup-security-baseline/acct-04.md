---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/acct-04.html
---

# ACCT.04 Assign permissions
<a name="acct-04"></a>

Configure user permissions by attaching [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) to IAM roles. *AWS managed policies* are standalone policies designed by AWS to provide permissions for many common use cases. If you customize permissions, follow the security best practice of [granting least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). *Least privilege* is the practice of granting the minimum set of permissions that each user needs to perform their tasks. Examples of roles for early-stage startups include administrator, developer, contractor, and finance team member. Create specialized roles as specific job functions are identified.

If you are using federated identities, users access the account by assuming an IAM role through the external identity provider. The IAM role defines the actions that users authenticated by your organization's IdP can perform. Apply custom or AWS managed policies to this role to configure permissions.

**To assign permissions for federated identities using IAM Identity Center**

1. See [Use IAM policies in permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocmp.html) in the IAM Identity Center documentation.

1. If you are using an external or third-party IdP, see [Adding IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console) in the IAM documentation.

   If you are using IAM users, configure IAM roles for the work your users perform, and have users assume those roles rather than attaching policies directly to individual IAM users. When an IAM user assumes a role, they receive temporary credentials that automatically expire. This reduces the risk of credential exposure compared to policies attached directly to IAM users, which remain in effect until explicitly removed.
