---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SPLIT_COLUMN_SINGLE_DELIMITER.html
---

# SPLIT\_COLUMN\_SINGLE\_DELIMITER
<a name="recipe-actions.SPLIT_COLUMN_SINGLE_DELIMITER"></a>

Splits a column into one or more new columns, according to a specific delimiter.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `pattern` – One or more characters to use as a separator, when splitting the data.
+ `limit` – How many splits to perform. The minimum is 1; the maximum is 20.
+ `includeInSplit` – If true, includes the pattern in the new column; otherwise, the pattern is discarded.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_SINGLE_DELIMITER",
        "Parameters": {
            "includeInSplit": "true",
            "limit": "1",
            "pattern": "/",
            "sourceColumn": "info_url"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
