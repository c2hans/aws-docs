---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/count-function.html
---

# COUNT and COUNT DISTINCT functions
<a name="count-function"></a>

The COUNT function counts the rows defined by the expression. The COUNT DISTINCT function computes the number of distinct non-NULL values in a column or expression. It eliminates all duplicate values from the specified expression before doing the count.

## Syntax
<a name="count-function-syntax"></a>

```
COUNT (DISTINCT {{column}})
```

## Arguments
<a name="count-function-arguments"></a>

{{column}}
The target column that the function operates on.

## Data types
<a name="count-function-data-types"></a>

The COUNT function and the COUNT DISTINCT function supports all argument data types.

The COUNT DISTINCT function returns BIGINT.

## Examples
<a name="count-function-examples"></a>

Count all of the users from the state of Florida.

```
select count (identifier) from users where state='FL';
```

Count all of the unique venue IDs from the EVENT table.

```
select count (distinct venueid) as venues from event;
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
