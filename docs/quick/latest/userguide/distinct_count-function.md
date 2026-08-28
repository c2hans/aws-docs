---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/distinct_count-function.html
---

# distinct\_count
<a name="distinct_count-function"></a>

The `distinct_count` function calculates the number of distinct values in a dimension or measure, grouped by the chosen dimension or dimensions. For example, `distinct_count(product type)` returns the total number of unique product types grouped by the (optional) chosen dimension, without any duplicates. The `distinct_count(ship date)` function returns the total number of dates when products were shipped grouped by the (optional) chosen dimension, for example region.

## Syntax
<a name="distinct_count-function-syntax"></a>

```
distinct_count(dimension or measure, [group-by level])
```

## Arguments
<a name="distinct_count-function-arguments"></a>

 *dimension or measure*
The argument must be a measure or a dimension. Null values are omitted from the results. Literal values don't work. The argument must be a field.

 *group-by level*
(Optional) Specifies the level to group the aggregation by. The level added can be any dimension or dimensions independent of the dimensions added to the visual.
The argument must be a dimension field. The group-by level must be enclosed in square brackets `[ ]`. For more information, see [Level-aware calculation - aggregate (LAC-A) functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html).

## Example
<a name="distinct_count-function-examples"></a>

The following example calculates the total number of dates when products were ordered grouped by the (optional) chosen dimension in the visual, for example region.

```
distinct_count({Order Date})
```

![The total number of dates when products were ordered in each region.](http://docs.aws.amazon.com/quick/latest/userguide/images/distinct_count-function-example.png)

You can also specify at what level to group the computation using one or more dimensions in the view or in your dataset. This is called a LAC-A function. For more information about LAC-A functions, see [Level-aware calculation - aggregate (LAC-A) functions](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations-aggregate.html). The following example calculates the average sales at the Country level, but not across other dimensions (Region) in the visual.

```
distinct_count({Order Date}, [Country])
```

![The total number of dates when products were ordered in each country.](http://docs.aws.amazon.com/quick/latest/userguide/images/distinct_count-function-example2.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
