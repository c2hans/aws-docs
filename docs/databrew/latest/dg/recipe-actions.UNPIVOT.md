---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.UNPIVOT.html
---

# UNPIVOT
<a name="recipe-actions.UNPIVOT"></a>

Converts all the column values in a selected row into individual rows with values.

![Table transformation from wide format with three columns to long format with column names and values.](http://docs.aws.amazon.com/databrew/latest/dg/images/unpivot.png)

**Parameters**
+ `sourceColumns` — A JSON-encoded string representing a list of one or more columns to be unpivoted.
+ `unpivotColumn` — The value column for the unpivot operation.
+ `valueColumn` — The column to hold unpivoted values.

**Example**

```
{
    "Action": {
        "Operation": "UNPIVOT",
        "Parameters": {
            "sourceColumns": "[\"idealpoint_estimate\"]",
            "unpivotColumn": "unpivoted_idealpoint_estimate",
            "valueColumn": "unpivoted_column_values"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
