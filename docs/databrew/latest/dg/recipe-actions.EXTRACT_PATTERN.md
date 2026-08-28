---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.EXTRACT_PATTERN.html
---

# EXTRACT\_PATTERN
<a name="recipe-actions.EXTRACT_PATTERN"></a>

Creates a new column, based on a regular expression, from the values in an existing column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.
+ `pattern` – A regular expression that indicates which character or characters to extract and create the new column from.

**Example**

```
{
    "RecipeAction": {
        "Operation": "EXTRACT_PATTERN",
        "Parameters": {
            "pattern": "^....*...$",
            "sourceColumn": "last_name",
            "targetColumn": "first_and_last_few_characters"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
