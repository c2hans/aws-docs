---
source_url: https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions.GET_ACTION_RESULT.html
---

# GET\_ACTION\_RESULT
<a name="recipe-actions.GET_ACTION_RESULT"></a>

Fetches the result of a previously submitted action. Only for use in the interactive experience.

**Parameters**
+ `actionId` – The ActionId returned in the original SendProjectSessionAction response.

**Example**

```
{
    "RecipeAction": {
        "Operation": "GET_ACTION_RESULT",
        "Parameters": {
            "actionId": "7",
        }
    }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
