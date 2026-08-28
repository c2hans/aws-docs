---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SPLIT_COLUMN_MULTIPLE_DELIMITER.html
---

# SPLIT\_COLUMN\_MULTIPLE\_DELIMITER
<a name="recipe-actions.SPLIT_COLUMN_MULTIPLE_DELIMITER"></a>

Splits a column according to multiple delimiters.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `patternOptions` – A JSON-encoded string representing one or more patterns that determine the split criteria.
+ `pattern` – One or more characters to use as a separator, when splitting the data.
+ `limit` – How many splits to perform. The minimum is 1; the maximum is 20.
+ `includeInSplit` – If true, includes the pattern in the new column; otherwise, the pattern is discarded.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SPLIT_COLUMN_MULTIPLE_DELIMITER",
        "Parameters": {
            "limit": "1",
            "patternOptions": "[{\"pattern\":\",\",\"includeInSplit\":true},{\"pattern\":\" \",\"includeInSplit\":true}]",
            "sourceColumn": "description"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
