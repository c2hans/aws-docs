---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.EXTRACT_BETWEEN_POSITIONS.html
---

# EXTRACT\_BETWEEN\_POSITIONS
<a name="recipe-actions.EXTRACT_BETWEEN_POSITIONS"></a>

Creates a new column, based on character positions, from the values in an existing column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `targetColumn` – The name of the new column to be created.
+ `startPosition` – The character position at which to perform the extract.
+ `endPosition` – The character position at which to end the extract.

**Example**

```
{
    "RecipeAction": {
        "Operation": "EXTRACT_BETWEEN_POSITIONS",
        "Parameters": {
            "endPosition": "9",
            "sourceColumn": "last_name",
            "startPosition": "3",
            "targetColumn": "characters_3_to_9"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
