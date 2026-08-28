---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/lastValue-function.html
---

# lastValue
<a name="lastValue-function"></a>

The `lastValue` function calculates the last value of the aggregated measure or dimension partitioned and sorted by specified attributes.

## Syntax
<a name="lastValue-function-syntax"></a>

The brackets are required. To see which arguments are optional, see the following descriptions.

```
lastValue
	(
	     {{aggregated measure or dimension}},
	     {{[ sort_attribute ASC_or_DESC, ... ]}},
	     {{[ partition_by_attribute, ... ]}}
	)
```

## Arguments
<a name="lastValue-function-arguments"></a>

*aggregated measure or dimension*
An aggregated measure or dimension that you want to see the last value for.

*sort attribute*
One or more aggregated fields, either measures or dimensions or both, that you want to sort the data by, separated by commas. You can either specify ascending (`ASC`) or descending (`DESC`) sort order.
Each field in the list is enclosed in {} (curly braces), if it's more than one word. The entire list is enclosed in [ ] (square brackets).

*partition by attribute*
(Optional) One or more measures or dimensions that you want to partition by, separated by commas.
Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets).

## Example
<a name="lastValue-function-example"></a>

The following example calculates the last value for `Destination Airport`. This calculation is sorted by the `Flight Date` value and partitioned by the `Flight Date` value sorted in ascending order and the `Origin Airport` value.

```
lastValue(
    [{Destination Airport}],
    [{Flight Date} ASC],
    [
        {Origin Airport},
    	truncDate('DAY', {Flight Date})
    ]
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
