---
source_url: https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-label-add.html
---

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html).

# AWS WAF rules that add labels
<a name="waf-rule-label-add"></a>

In almost all rules, you can define labels and AWS WAF will apply them to any matching request.

The following rule types are the only exceptions:
+ **Rate-based rules label only while rate limiting** – Rate-based rules only add labels to web requests for a specific aggregation instance while that instance is being rate limited by AWS WAF. For information about rate-based rules, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md).
+ **Labeling isn't allowed in rule group reference statements** – The console doesn't accept labels for rule group statements or managed rule group statements. Through the API, specifying a label for either statement type results in a validation exception. For information about these statement types, see [Using managed rule group statements in AWS WAF](waf-rule-statement-type-managed-rule-group.md) and [Using rule group statements in AWS WAF](waf-rule-statement-type-rule-group.md).

**WCUs ** – 1 WCU for every 5 labels that you define in your protection pack (web ACL) or rule group rules.

**Where to find this**
+ **Rule builder** on the console – Under the rule's **Action** settings, under **Label**.
+ **API data type** – `Rule` `RuleLabels`

You define a label in a rule by specifying the custom namespace strings and name to append to the label namespace prefix. AWS WAF derives the prefix from the context in which you define the rule. For information about this, see the label syntax information under [Label syntax and naming requirements in AWS WAF](waf-rule-label-requirements.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
