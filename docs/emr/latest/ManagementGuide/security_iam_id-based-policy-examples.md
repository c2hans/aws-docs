---
source_url: https://docs.aws.amazon.com/emr/latest/ManagementGuide/security_iam_id-based-policy-examples.html
---

# Amazon EMR identity-based policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, a users and roles don't have permission to create or modify Amazon EMR resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or AWS API. An IAM administrator must create IAM policies that grant users and roles permission to perform specific API operations on the specified resources they need. The administrator must then attach those policies to the a users or groups that require those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy documents, see [Creating policies on the JSON tab](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html#access_policies_create-json-editor) in the *IAM User Guide*.

**Topics**
+ [Policy best practices for Amazon EMR](security_iam_service-with-iam-policy-best-practices.md)
+ [Allow users to view their own permissions](security_iam_id-based-policy-examples-view-own-permissions.md)
+ [Amazon EMR managed policies](emr-managed-iam-policies.md)
+ [IAM policies for tag-based access to clusters and EMR notebooks](emr-fine-grained-cluster-access.md)
+ [Denying the ModifyInstanceGroup action in Amazon EMR](emr-cluster-deny-modifyinstancegroup.md)
+ [Troubleshooting Amazon EMR identity and access](security_iam_troubleshoot.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
