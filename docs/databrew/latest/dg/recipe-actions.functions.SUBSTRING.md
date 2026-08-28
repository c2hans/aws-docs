---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.SUBSTRING.html
---

# SUBSTRING
<a name="recipe-actions.functions.SUBSTRING"></a>

Returns in a new column some or all of the specified strings in the source column, based on the user-defined starting and ending index values.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `startPosition` – The character position to begin with, from the left end of the string.
+ `endPosition` – The character position to end with, from the left end of the string.
+ `targetColumn` – The name of the new column to be created.

**Note**
You can specify either `sourceColumn` or `value`, but not both.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SUBSTRING",
        "Parameters": {
            "sourceColumn": "last_name",
            "startPosition": "5",
            "endPosition": "8",
            "targetColumn": "chars_5_through_8"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
