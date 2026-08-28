---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.GET_STEP_DATAFRAME.html
---

# GET\_STEP\_DATAFRAME
<a name="recipe-actions.GET_STEP_DATAFRAME"></a>

Fetches the data frame from a step in the project's recipe. Only for use in the interactive experience. Used with the ViewFrame parameter to paginate across a large data frame.

**Parameters**
+ `stepIndex` – The index of the step in the project's recipe for which to fetch the data frame.

**Example**

```
{
    "RecipeAction": {
        "Operation": "GET_STEP_DATAFRAME",
        "Parameters": {
            "stepIndex": "0"
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
