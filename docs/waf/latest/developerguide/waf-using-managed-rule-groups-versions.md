---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-using-managed-rule-groups-versions.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Retrieving the available versions for a managed rule group
<a name="waf-using-managed-rule-groups-versions"></a>

The available versions of a managed rule group are versions that haven't yet been scheduled to expire. The list indicates which version is the current default version for the rule group.

**To retrieve a list of the available versions of a managed rule group**
+ **Console**
  + (Option) When you add the managed rule group to your protection pack (web ACL), choose **Edit** to see the rule group's information. Expand the **Version** dropdown to see the list of available versions.
  + (Option) After you've added the managed rule group into your protection pack (web ACL), choose **Edit** on the protection pack (web ACL), and then select and edit the rule group rule. Expand the **Version** dropdown to see the list of available versions.
+ **API** –
  +  `ListAvailableManagedRuleGroupVersions`
+ **CLI** –
  +  `aws wafv2 list-available-managed-rule-group-versions --scope=<CLOUDFRONT|REGIONAL> --vendor-name <vendor> --name <managedrule_name>`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
