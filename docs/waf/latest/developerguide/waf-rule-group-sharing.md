---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-group-sharing.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Sharing a rule group
<a name="waf-rule-group-sharing"></a>

You can share a rule group with other acccounts, for use by those accounts.

**Sharing a rule group**
You can share with one or more specific accounts, and you can share with all accounts in an organization.

To share a rule group, you use the AWS WAF API to create a policy for the rule group sharing that you want. For more information, see [PutPermissionPolicy](https://docs.aws.amazon.com/waf/latest/APIReference/API_PutPermissionPolicy.html) in the *AWS WAF API Reference*.

**Using a rule group that's been shared with you**
If a rule group has been shared with your account, you can access it through the API and you can reference it when you create or update your protection packs (web ACLs) through the API. For more information, see [GetRuleGroup](https://docs.aws.amazon.com/waf/latest/APIReference/API_GetRuleGroup.html), [CreateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_CreateWebACL.html), and [UpdateWebACL](https://docs.aws.amazon.com/waf/latest/APIReference/API_UpdateWebACL.html) in the *AWS WAF API Reference*. Rule groups that are shared with you don't appear in your AWS WAF console rule groups listing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
