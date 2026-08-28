---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.DATEDIFF.html
---

# DATE\_DIFF
<a name="recipe-actions.functions.DATEDIFF"></a>

Creates a new column containing the difference between two dates.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `sourceColumn2` – The name of an existing column.
+ `value1` – A character string to evaluate.
+ `value2` – A character string to evaluate.
+ `units` – A unit of measure for describe the difference between the dates. Valid values are `MONTHS`, `YEARS`, `MILLISECONDS`, `QUARTERS`, `HOURS`, `MICROSECONDS`, `WEEKS`, `SECONDS`, `DAYS`, and `MINUTES`.
+ `targetColumn` – A name for the newly created column.

**Note**
You can only specify one of the following combinations:
Both of `sourceColumn1` and `sourceColumn2`.
One of `sourceColumn1` or `sourceColumn2` and one of `value1` or `value2`.
Both of `value1` and `value2`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "DATE_DIFF",
        "Parameters": {
            "value1": "2020-01-01",
            "value2": "2020-10-06",
            "units": "DAYS",
            "targetColumn": "DATEDIFF Column 1"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
