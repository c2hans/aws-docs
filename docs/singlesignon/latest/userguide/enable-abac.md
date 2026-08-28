---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/enable-abac.html
---

# Enable attributes for access control
<a name="enable-abac"></a>

Use the following procedure to enable the attributes for access (ABAC) control feature using the IAM Identity Center console.

**Note**
If you have existing permission sets and you plan to enable ABAC in your IAM Identity Center instance, additional security restrictions require you to first have the `iam:UpdateAssumeRolePolicy` policy. These additional security restrictions are not required if you do not have any permission sets created in your account.
If your IAM Identity Center instance was created before December 2020 and you plan to enable ABAC in it, you must have the `iam:UpdateAssumeRolePolicy` policy associated with the IAM Identity Center administrative role, regardless of whether you have permission sets created in your account.

**To enable Attributes for access control**

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**

1. On the **Settings** page, locate the **Attributes for access control** information box, and then choose **Enable**. Continue to the next procedure to configure it.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
