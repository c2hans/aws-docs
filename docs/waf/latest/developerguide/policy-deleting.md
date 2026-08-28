---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/policy-deleting.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Deleting an AWS Firewall Manager policy
<a name="policy-deleting"></a>

You can delete a Firewall Manager policy by performing the following steps.

**To delete a policy (console)**

1. In the navigation pane, choose **Security policies**.

1. Choose the option next to the policy that you want to delete.

1. Choose **Delete**.

**Note**
When you delete a Firewall Manager common security group policy, to remove the policy's replica security groups, choose the option to clean up the resources created by the policy. Otherwise, after the primary is deleted, the replicas remain and require manual management in each Amazon VPC instance.

**Important**
When you delete a Firewall Manager Shield Advanced policy, the policy is deleted, but your accounts remain subscribed to Shield Advanced.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
