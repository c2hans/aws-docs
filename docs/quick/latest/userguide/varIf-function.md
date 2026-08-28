---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/varIf-function.html
---

# varIf
<a name="varIf-function"></a>

Based on a conditional statement, the `varIf` function calculates the variance of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a sample.

## Syntax
<a name="varIf-function-syntax"></a>

```
varIf(measure, conditions)
```

## Arguments
<a name="varIf-function-arguments"></a>

 *measure*
The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field.

 *condition*
One or more conditions in a single statement.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
