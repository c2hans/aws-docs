---
source_url: https://docs.aws.amazon.com/sns/latest/dg/security_iam_service-with-iam.html
---

# How Amazon SNS works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon SNS, learn what IAM features are available to use with Amazon SNS.

**IAM features you can use with Amazon Simple Notification Service**

| IAM feature | Amazon SNS support |
| --- | --- |
| [Identity-based policies](security-iam.md#security_iam_service-with-iam-id-based-policies) |  Yes |
| [Resource-based policies](security-iam.md#security_iam_service-with-iam-resource-based-policies) | Yes |
| [Policy actions](security-iam.md#security_iam_service-with-iam-id-based-policies-actions) |  Yes |
| [Policy resources](security-iam.md#security_iam_service-with-iam-id-based-policies-resources) |  Yes |
| [Policy condition keys (service-specific)](security-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes |
| [ACLs](security-iam.md#security_iam_service-with-iam-acls) |  No  |
| [ABAC (tags in policies)](security-iam.md#security_iam_service-with-iam-tags) |  Partial |
| [Temporary credentials](security-iam.md#security_iam_service-with-iam-roles-tempcreds) |  Yes |
| [Principal permissions](security-iam.md#security_iam_service-with-iam-principal-permissions) |  Yes |
| [Service roles](security-iam.md#security_iam_service-with-iam-roles-service) |  Yes |
| [Service-linked roles](security-iam.md#security_iam_service-with-iam-roles-service-linked) |  No  |

To get a high-level view of how Amazon SNS and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Notification Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sns` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
