---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/avgIf-function.html
---

# avgIf
<a name="avgIf-function"></a>

Based on a conditional statement, the `avgIf` function averages the set of numbers in the specified measure, grouped by the chosen dimension or dimensions. For example, `avgIf(ProdRev,CalendarDay >= ${BasePeriodStartDate} AND CalendarDay <= ${BasePeriodEndDate} AND SourcingType <> 'Indirect')` returns the average for that measure grouped by the (optional) chosen dimension, if the condition evaluates to true.

## Syntax
<a name="avgIf-function-syntax"></a>

```
avgIf({{dimension or measure, condition}})
```

## Arguments
<a name="avgIf-function-arguments"></a>

 *decimal*
The argument must be a measure. Null values are omitted from the results. Literal values don't work. The argument must be a field.

 *condition*
One or more conditions in a single statement.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
