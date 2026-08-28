---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/search-dashboards.html
---

# SearchDashboards
<a name="search-dashboards"></a>

Use the `SearchDashboards` API operation to search for dashboards in an AWS account. Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight search-dashboards
    --aws-account-id {{555555555555}}
    --filters Operator={{StringEquals}},Name={{QUICKSIGHT_USER}},Value=arn:aws:quicksight:{{us-east-1}}:{{555555555555}}:user/default/{{USERNAME}}
    --page-size {{10}}
    --max-items {{100}}
```

If your `region` has already been configured within the CLI, it doesn't need to be included as an argument.

------

If your region has already been configured with the CLI, it does not need to be included in an argument.

For more information about the `SearchDashboards` API operation, see [SearchDashboards](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SearchDashboards.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
