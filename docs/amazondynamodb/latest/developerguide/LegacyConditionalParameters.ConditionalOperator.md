---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.ConditionalOperator.html
---

# ConditionalOperator (legacy)
<a name="LegacyConditionalParameters.ConditionalOperator"></a>

**Note**
We recommend that you use the new expression parameters instead of these legacy parameters whenever possible. For more information, see [Using expressions in DynamoDB](Expressions.md).

The legacy conditional parameter `ConditionalOperator` is a logical operator used to apply to the conditions in a `Expected`, `QueryFilter` or `ScanFilter` map:
+ AND - If all of the conditions evaluate to true, then the entire map evaluates to true.
+ OR - If at least one of the conditions evaluates to true, then the entire map evaluates to true.

If you omit `ConditionalOperator`, then `AND` is the default.

The operation will succeed only if the entire map evaluates to true.

**Note**
This parameter does not support attributes of type List or Map.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
