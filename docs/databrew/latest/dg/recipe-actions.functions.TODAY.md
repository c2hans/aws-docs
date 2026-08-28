---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.functions.TODAY.html
---

# TODAY
<a name="recipe-actions.functions.TODAY"></a>

Creates a new column containing the current date in the format `yyyy-mm-dd`.

**Parameters**
+ `timeZone` – The name of a time zone. If no time zone is specified, then the default is Universal Coordinated Time (UTC).
+ `targetColumn` – A name for the newly created column.

**Example**

```
{
    "RecipeAction": {
        "Operation": "TODAY",
        "Parameters": {
            "timeZone": "US/Pacific",
            "targetColumn": "TODAY Column 1"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
