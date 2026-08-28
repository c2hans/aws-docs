---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.ENDS_WITH.html
---

# ENDS\_WITH
<a name="recipe-actions.functions.ENDS_WITH"></a>

Returns `true` in a new column if a specified number of rightmost characters, or custom string, matches a pattern.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `value` – A character string to evaluate.
+ `pattern` – A regular expression that must match the end of the string.
+ `targetColumn` – The name of the new column to be created.

**Note**
You can specify either `sourceColumn` or `value`, but not both.

**Example**

```
{
    "RecipeAction": {
        "Operation": "ENDS_WITH",
        "Parameters": {
            "sourceColumn": "nationality",
            "pattern": "[Ss]",
            "targetColumn": "nationality_ends_with"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
