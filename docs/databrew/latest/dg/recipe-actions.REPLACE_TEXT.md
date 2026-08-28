---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REPLACE_TEXT.html
---

# REPLACE\_TEXT
<a name="recipe-actions.REPLACE_TEXT"></a>

Replaces a specified sequence of characters with another.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – Character or characters or a regular expression, indicating which characters should be replaced in the source column.
+ `value` – The replacement character or characters to be substituted.

**Examples**

```
{
    "RecipeAction": {
        "Operation": "REPLACE_TEXT",
        "Parameters": {
            "pattern": "x",
            "sourceColumn": "first_name",
            "value": "a"
        }
    }
}
```

```
{
    "RecipeAction": {
        "Operation": "REPLACE_TEXT",
        "Parameters": {
            "pattern": "[0-9]",
            "sourceColumn": "nationality",
            "value": "!"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
