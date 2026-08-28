---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statements-rule-group.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# Using rule group rule statements in AWS WAF
<a name="waf-rule-statements-rule-group"></a>

**Note**
Rule group rule statements are not nestable.

This section describes the rule group rule statements that you can use in your protection pack (web ACL). Rule group protection pack (web ACL) capacity units (WCUs) are set by the rule group owner at the time of creation. For information about WCUs, see [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md).

| Rule group statement | Description | WCUs |
| --- | --- | --- |
| [Using managed rule group statements](waf-rule-statement-type-managed-rule-group.md) | Runs the rules that are defined in the specified managed rule group. <br />You can narrow the scope of requests that the rule group evaluates by adding a scope-down statement. <br />You can't nest a managed rule group statement inside any other statement type. | Defined by the rule group, plus any additional WCUs for a scope-down statement. |
| [Using rule group statements](waf-rule-statement-type-rule-group.md) | Runs the rules that are defined in a rule group that you manage. <br />You can't add a scope-down statement to a rule group reference statement for your own rule group. <br />You can't nest a rule group statement inside any other statement type | You define the WCU limit for the rule group when you create it. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
