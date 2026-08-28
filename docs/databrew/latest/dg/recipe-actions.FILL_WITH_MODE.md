---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.FILL_WITH_MODE.html
---

# FILL\_WITH\_MODE
<a name="recipe-actions.FILL_WITH_MODE"></a>

Returns a column with missing data replaced by the mode of all values.

You can also specify tie-breaker logic, where some of the values are identical. For example, consider the following values:

`1 2 2 3 3 4`

A `modeType` of `MINIMUM` causes `FILL_WITH_MODE` to return 2 as the mode value. If `modeType` is `MAXIMUM`, the mode is 3. For `AVERAGE`, the mode is 2.5.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `modeType` – How to resolve tie values in the data. This value must be `MINIMUM`, `NONE`, `AVERAGE`, or `MAXIMUM`.

**Example**

```
{
    "RecipeAction": {
        "Operation": "FILL_WITH_MODE",
        "Parameters": {
            "modeType": "MAXIMUM",
            "sourceColumn": "age"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
