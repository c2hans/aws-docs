---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REPLACE_WITH_RANDOM_BETWEEN.html
---

# REPLACE\_WITH\_RANDOM\_BETWEEN
<a name="recipe-actions.REPLACE_WITH_RANDOM_BETWEEN"></a>

Replaces values with a random number.

**Parameters**
+ `lowerBound` – The lower bound of the random number range.
+ `sourceColumns` – A list of existing column names.
+ `upperBound` – The upper bound of the random number range.

**Example**

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_RANDOM_BETWEEN",
        "Parameters": {
            "lowerBound": "1",
            "sourceColumns": ["column1", "column2"],
            "upperBound": "100"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
