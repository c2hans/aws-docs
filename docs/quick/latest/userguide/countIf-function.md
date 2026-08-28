---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/countIf-function.html
---

# countIf
<a name="countIf-function"></a>

Based on a conditional statement, the `countIf` function calculates the number of values in a dimension or measure, grouped by the chosen dimension or dimensions.

## Syntax
<a name="countIf-function-syntax"></a>

```
countIf(dimension or measure, condition)
```

## Arguments
<a name="countIf-function-arguments"></a>

 *dimension or measure*
The argument must be a measure or a dimension. Null values are omitted from the results. Literal values don't work. The argument must be a field.

 *condition*
One or more conditions in a single statement.

## Return type
<a name="countIf-function-return-type"></a>

Integer

## Example
<a name="countIf-function-example"></a>

The following function returns a count of the sales transactions (`Revenue`) that meet the conditions, including any duplicates.

```
countIf (
    Revenue,
    # Conditions
        CalendarDay >= ${BasePeriodStartDate} AND
        CalendarDay <= ${BasePeriodEndDate} AND
        SourcingType <> 'Indirect'
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
