---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.REPLACE_WITH_RANDOM_DATE_BETWEEN.html
---

# REPLACE\_WITH\_RANDOM\_DATE\_BETWEEN
<a name="recipe-actions.REPLACE_WITH_RANDOM_DATE_BETWEEN"></a>

Replaces values with a random date.

**Parameters**
+ `startDate` – The start of the range of dates from which a random date will be taken.
+ `sourceColumns` – A list of existing column names.
+ `endDate` – The end of the range of dates from which a random date will be taken.

**Example**

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_RANDOM_DATE_BETWEEN",
        "Parameters": {
            "startDate": "2020-12-12 12:12:12",
            "sourceColumns": ["column1", "column2"],
            "endDate": "2021-12-12 12:12:12"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
