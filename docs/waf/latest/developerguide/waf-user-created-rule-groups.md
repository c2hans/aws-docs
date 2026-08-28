---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-user-created-rule-groups.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Managing your own rule groups
<a name="waf-user-created-rule-groups"></a>

You can create your own rule group to reuse collections of rules that you either don't find in the managed rule group offerings or that you prefer to handle on your own.

Rule groups that you create hold rules just like a protection pack (web ACL) does, and you add rules to a rule group in the same way as you do to a protection pack (web ACL). When you create your own rule group, you must set an immutable maximum capacity for it.

**Topics**
+ [Creating a rule group](waf-rule-group-creating.md)
+ [Editing a rule group](waf-rule-group-editing.md)
+ [Using your rule group in a protection pack (web ACL)](waf-rule-group-using.md)
+ [Deleting a rule group](waf-rule-group-deleting.md)
+ [Sharing a rule group](waf-rule-group-sharing.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
