---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.SKEWNESS.html
---

# SKEWNESS
<a name="recipe-actions.SKEWNESS"></a>

Applies transformations on your data values to change the distribution shape and its skew.

**Parameters**
+ `sourceColumn` – The name of an existing column.

  `targetColumn` – The name of the new column to be created.

  `skewFunction`
  + `ROOT` – extract value-root. The root can be provided in the `value` parameter.

    `LOG` – log base value. The log base can be provided in the `value` parameter.

    `SQUARE` – square function

  `value` – Argument of the skewFunction.

**Example**

```
{
    "RecipeAction": {
        "Operation": "SKEWNESS",
        "Parameters": {
            "sourceColumn": "level",
            "targetColumn": "bin",
            "skewFunction": "LOG",
            "value": "2.718281828"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
