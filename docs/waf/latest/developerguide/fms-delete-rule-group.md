---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/fms-delete-rule-group.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Deleting a rule group from a Firewall Manager DNS Firewall policy
<a name="fms-delete-rule-group"></a>

**Deleting a rule group**
To delete a rule group from a Firewall Manager DNS Firewall policy, you must perform the following steps:

**Important**
Removing a rule group from your Firewall Manager DNS Firewall policy removes its effect from VPCs that have the policy applied, regardless of whether you also delete the rule group from your DNS Firewall rule groups. Deleting a rule group is a permanent action and can't be undone.

1. Remove the rule group from your Firewall Manager DNS Firewall policy.

1. Unshare the rule group in AWS Resource Access Manager. To unshare a rule group that you own, you must remove it from the resource share. You can do this using the AWS RAM console or the AWS CLI. For information about unsharing a resource, see [Update a resource share in AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/working-with-sharing-update.html) in the *AWS RAM User Guide*.

1. Delete the rule group using the DNS Firewall console or AWS CLI.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
