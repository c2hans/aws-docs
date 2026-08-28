---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SPLIT_COLUMN_BETWEEN_DELIMITER.html
---

# SPLIT\_COLUMN\_BETWEEN\_DELIMITER
<a name="recipe-actions.SPLIT_COLUMN_BETWEEN_DELIMITER"></a>

Splits a column into three new columns, according to a beginning and ending delimiter.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `patternOption1` – A JSON-encoded string representing one or more characters that indicate the first delimiter.
+ `patternOption2` – A JSON-encoded string representing one or more characters that indicate the second delimiter.
+ `pattern` – One or more characters to use as a separator, when splitting the data.
+ `includeInSplit` – If true, includes the pattern in the new column; otherwise, the pattern is discarded.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_BETWEEN_DELIMITER",
        "Parameters": {
            "patternOption1": "{\"pattern\":\"H\",\"includeInSplit\":true}",
            "patternOption2": "{\"pattern\":\"M\",\"includeInSplit\":true}",
            "sourceColumn": "last_name"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
