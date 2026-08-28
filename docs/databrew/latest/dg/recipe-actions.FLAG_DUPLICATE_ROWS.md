---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FLAG_DUPLICATE_ROWS.html
---

# FLAG\_DUPLICATE\_ROWS
<a name="recipe-actions.FLAG_DUPLICATE_ROWS"></a>

Returns a new column with a specified value in each row that indicates whether that row is an exact match of an earlier row in the dataset. When matches are found, they are flagged as duplicates. The initial occurrence is not flagged, because it doesn't match an earlier row.

**Parameters**
+ `trueString` – Value to be inserted if the row matches an earlier row.
+ `falseString` – Value to be inserted if the row is unique.
+ `targetColumn` – Name of the new column that is inserted in the dataset.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FLAG_DUPLICATE_ROWS",
        "Parameters": {
            "trueString": "TRUE",
            "falseString": "FALSE",
            "targetColumn": "Flag"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
