---
source_url: https://docs.aws.amazon.com/msk/latest/developerguide/security_iam_id-based-policy-examples.html
---

# Amazon MSK identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, IAM users and roles don't have permission to execute Amazon MSK API actions. An administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the IAM users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating Policies on the JSON Tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices](security_iam_service-with-iam-policy-best-practices.md)
+ [Allow users to view their own permissions](security_iam_id-based-policy-examples-view-own-permissions.md)
+ [Accessing one Amazon MSK cluster](security_iam_id-based-policy-examples-access-one-cluster.md)
+ [Accessing Amazon MSK clusters based on tags](security_iam_id-based-policy-examples-view-widget-tags.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
