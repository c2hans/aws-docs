---
source_url: https://docs.aws.amazon.com/amazonswf/latest/developerguide/security_iam_service-with-iam.html
---

# How Amazon Simple Workflow Service works with IAM
<a name="security_iam_service-with-iam"></a>

Before you use IAM to manage access to Amazon SWF, learn what IAM features are available to use with Amazon SWF.

**IAM features you can use with Amazon Simple Workflow Service**

| IAM feature | Amazon SWF support |
| --- | --- |
| [Identity-based policies](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies) |  Yes |
| [Resource-based policies](swf-dev-iam.md#security_iam_service-with-iam-resource-based-policies) |  No  |
| [Policy actions](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-actions) |  Yes |
| [Policy resources](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-resources) |  Yes |
| [Policy condition keys (service-specific)](swf-dev-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys) |  Yes |
| [ACLs](swf-dev-iam.md#security_iam_service-with-iam-acls) |  No  |
| [ABAC (tags in policies)](swf-dev-iam.md#security_iam_service-with-iam-tags) |  Partial |
| [Temporary credentials](swf-dev-iam.md#security_iam_service-with-iam-roles-tempcreds) |  Yes |
| [Principal permissions](swf-dev-iam.md#security_iam_service-with-iam-principal-permissions) |  Yes |
| [Service roles](swf-dev-iam.md#security_iam_service-with-iam-roles-service) |  Yes |
| [Service-linked roles](swf-dev-iam.md#security_iam_service-with-iam-roles-service-linked) |  No  |

To get a high-level view of how Amazon SWF and other AWS services work with most IAM features, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Workflow Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonswf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
