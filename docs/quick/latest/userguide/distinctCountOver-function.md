---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/distinctCountOver-function.html
---

# distinctCountOver
<a name="distinctCountOver-function"></a>

The `distinctCountOver` function calculates the distinct count of the operand partitioned by the specified attributes at a specified level. Supported levels are `PRE_FILTER` and `PRE_AGG`. The operand must be unaggregated.

## Syntax
<a name="distinctCountOver-function-syntax"></a>

The brackets are required. To see which arguments are optional, see the following descriptions.

```
distinctCountOver
(
  {{measure or dimension field}}
  ,{{[ partition_field, ... ]}}
  ,{{calculation level}}
)
```

## Arguments
<a name="distinctCountOver-function-arguments"></a>

 *measure or dimension field*
The measure or dimension that you want to do the calculation for, for example `{Sales Amt}`. Valid values are `PRE_FILTER` and `PRE_AGG`.

 *partition field*
(Optional) One or more dimensions that you want to partition by, separated by commas.
Each field in the list is enclosed in {} (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets).

 *calculation level*
(Optional) Specifies the calculation level to use:
+ **`PRE_FILTER`** – Prefilter calculations are computed before the dataset filters.
+ **`PRE_AGG`** – Preaggregate calculations are computed before applying aggregations and top and bottom *N* filters to the visuals.
This value defaults to `POST_AGG_FILTER` when blank. `POST_AGG_FILTER` is not a valid level for this operation and will result in an error message. For more information, see [Using level-aware calculations in Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations.html).

## Example
<a name="distinctCountOver-function-example"></a>

The following example gets the distinct count of `Sales` partitioned over `City` and `State` at the `PRE_AGG` level.

```
distinctCountOver
(
  Sales,
  [City, State], PRE_AGG
)
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
