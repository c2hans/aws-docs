---
source_url: https://docs.aws.amazon.com/glue/latest/dg/glue-policy-examples.html
---

# AWS Glue access control policy examples
<a name="glue-policy-examples"></a>

This section contains examples of both identity-based (IAM) access control policies and AWS Glue resource policies.

**Contents**
+ [Identity-based policy examples for AWS Glue](security_iam_id-based-policy-examples.md)
  + [Policy best practices](security_iam_id-based-policy-examples.md#security_iam_service-with-iam-policy-best-practices)
  + [Resource-level permissions only apply to specific AWS Glue objects](security_iam_id-based-policy-examples.md#glue-identity-based-policy-limitations)
  + [Using the AWS Glue console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console)
  + [Allow users to view their own permissions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-own-permissions)
  + [Grant read-only permission to a table](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-read-only-table-access)
  + [Filter tables by GetTables permission](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-filter-tables)
  + [Grant full access to a table and all partitions](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-full-access-tables-partitions)
  + [Control access by name prefix and explicit denial](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-deny-by-name-prefix)
  + [Grant access using tags](security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-allow)
  + [Deny access using tags](security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-deny)
  + [Use tags with list and batch API operations](security_iam_id-based-policy-examples.md#tags-control-access-example-triggers-list-batch)
  + [Control settings using condition keys or context keys](security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-keys)
    + [Control policies that control settings using condition keys](security_iam_id-based-policy-examples.md#glue-identity-based-policy-condition-key-vpc)
    + [Control policies that control settings using context keys](security_iam_id-based-policy-examples.md#glue-identity-based-policy-context-key-glue)
  + [Deny an identity the ability to create data preview sessions](security_iam_id-based-policy-examples.md#deny-data-preview-sessions-per-identity)
+ [Resource-based policy examples for AWS Glue](security_iam_resource-based-policy-examples.md)
  + [Considerations for using resource-based policies with AWS Glue](security_iam_resource-based-policy-examples.md#security_iam_resource-based-policy-examples-considerations)
  + [Use a resource policy to control access in the same account](security_iam_resource-based-policy-examples.md#glue-policy-resource-policies-example-same-account)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
