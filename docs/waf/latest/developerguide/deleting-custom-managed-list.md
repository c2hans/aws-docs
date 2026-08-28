---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/deleting-custom-managed-list.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Deleting a custom managed list in Firewall Manager
<a name="deleting-custom-managed-list"></a>

You can delete custom managed lists. You can't edit or delete lists that Firewall Manager manages.

**Note**
Currently, Firewall Manager doesn’t check references to a custom managed list when you delete it. This means that you can delete a custom managed application list or protocol list even when it is in use by an active policy. This can cause the policy to stop functioning. Only delete an application list or protocol list after you have verified that it isn't referenced by any active polices.

**To delete a custom managed application or protocol list**

1. Sign in to the AWS Management Console using your Firewall Manager administrator account, and then open the Firewall Manager console at [https://console.aws.amazon.com/wafv2/fmsv2](https://console.aws.amazon.com/wafv2/fmsv2). For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).
**Note**
For information about setting up a Firewall Manager administrator account, see [AWS Firewall Manager prerequisites](fms-prereq.md).

1. Make sure that the list that you want to delete isn't in use in any of your audit security group policies by doing the following:

   1. In the navigation pane, choose **Security policies**.

   1. In the **AWS Firewall Manager policies** page, select and edit your audit security groups, and remove any references to the custom list that you want to delete.

      If you delete a custom managed list that's in use in an audit security group policy, the policy that's using it can stop functioning.

1. In the navigation pane, choose **Application lists** or **Protocol lists**, depending on the type of list you want to delete.

1. In the list page, select the custom list that you want to delete and choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
