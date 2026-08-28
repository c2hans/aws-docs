---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.RANDOM_BETWEEN.html
---

# RANDOM\_BETWEEN
<a name="recipe-actions.functions.RANDOM_BETWEEN"></a>

In a new column, returns a random number between a specified lower bound (inclusive) and a specified upper bound (inclusive).

**Parameters**
+ `lowerBound` – The lower bound of the random number range.
+ `upperBound` – The upper bound of the random number range.
+ `targetColumn` – The name of the new column to be created.

**Example**

```
{
    "RecipeAction": {
        "Operation": "RANDOM_BETWEEN",
        "Parameters": {
            "lowerBound": "1",
            "targetColumn": "RANDOM_BETWEEN Column 1",
            "upperBound": "100"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
