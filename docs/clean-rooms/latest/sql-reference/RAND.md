---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/sql-reference/RAND.html
---

# RAND function
<a name="RAND"></a>

The RAND function generates a random floating-point number between 0 and 1. The RAND function generates a new random number each time it's called.

## Syntax
<a name="RAND-syntax"></a>

```
RAND()
```

## Return type
<a name="RAND-return-type"></a>

RANDOM returns a DOUBLE.

## Example
<a name="RAND-example"></a>

The following example generates a column of random floating-point numbers between 0 and 1 for each row in the `squirrels` table. The resulting output would be a single column containing a list of random decimal values, with one value for each row in the squirrels table.

```
SELECT rand() FROM squirrels
```

This type of query is useful when you need to generate random numbers, for example, to simulate random events or to introduce randomness into your data analysis. In the context of the `squirrels` table, it might be used to assign random values to each squirrel, which could then be used for further processing or analysis.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
