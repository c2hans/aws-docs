---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.NEXT.html
---

# NEXT
<a name="recipe-actions.functions.NEXT"></a>

Returns a new column, where each value represents a value that is *n* rows later in the source column.

**Parameters**
+ `sourceColumn` – The name of an existing column.
+ `numRows` – A value that represents *n* rows earlier in the source column. For example, if `numRows` is 3, then `NEXT` uses the third-next `sourceColumn` value as the new `targetColumn` value.
+ `targetColumn` – A name for the newly created column.

**Example**

```
{
    "Action": {
        "Operation": "NEXT",
        "Parameters": {
            "numRows": "1",
            "sourceColumn": "age",
            "targetColumn": "age_NEXT"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
