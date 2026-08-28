---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.ROLLING_MAX.html
---

# ROLLING\_MAX
<a name="recipe-actions.functions.ROLLING_MAX"></a>

Returns in a new column the rolling maximum of values from a specified number of rows before to a specified number of rows after the current row in the specified column.

**Parameters**
+ `sourceColumn` – The name of an existing column.

  `numRowsBefore` – A number of rows before the current source row, representing the start of the window.
+ `numRowsAfter` – A number of rows after the current source row, representing the end of the window.
+ `targetColumn` – A name for the newly created column.

**Example**

```
{
    "Action": {
        "Operation": "ROLLING_MAX",
        "Parameters": {
            "numRowsAfter": "10",
            "numRowsBefore": "10",
            "sourceColumn": "weight_kg",
            "targetColumn": "weight_kg_ROLLING_MAX"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
