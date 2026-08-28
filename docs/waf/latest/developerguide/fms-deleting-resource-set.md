---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/fms-deleting-resource-set.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Deleting a resource set in Firewall Manager
<a name="fms-deleting-resource-set"></a>

Before you can delete a resource set, the resource set must be disassociated from all policies using the resource set. You can disassociate resource groups in the policy detail page using the console, or with the [PutPolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutPolicy.html) API.

**To delete a resource set (console)**

1. In the navigation pane, choose **Resource sets**.

1. Choose the option next to the resource set that you want to delete.

1. Choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
