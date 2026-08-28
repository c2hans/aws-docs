---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FLAG_DUPLICATES_IN_COLUMN.html
---

# FLAG\_DUPLICATES\_IN\_COLUMN
<a name="recipe-actions.FLAG_DUPLICATES_IN_COLUMN"></a>

Returns a new column with a specified value in each row that indicates whether the value in the row's source column matches a value in an earlier row of the source column. When matches are found, they are flagged as duplicates. The initial occurrence is not flagged, because it doesn't match an earlier row.

**Parameters**
+ `sourceColumn` – Name of the source column.
+ `targetColumn` – Name of the target column.
+ `trueString` – String to be inserted in the target column when a source column value duplicates an earlier value in that column.
+ `falseString` – String to be inserted in the target column when a source column value is distinct from earlier values in that column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FLAG_DUPLICATES_IN_COLUMN",
        "Parameters": {
            "sourceColumn": "Name",
            "targetColumn": "Duplicate",
            "trueString": "TRUE",
            "falseString": "FALSE"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
