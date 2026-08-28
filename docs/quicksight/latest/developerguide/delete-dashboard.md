---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/delete-dashboard.html
---

# DeleteDashboard
<a name="delete-dashboard"></a>

Use the `DeleteDashboard` API operation to delete a dashboard. To use this operation, you need the ID of the dashboard that you want to delete. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

You can add a `VersionNumber` parameter to this operation to only delete the specified version of the dashboard.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight delete-dashboard
    --aws-account-id {{555555555555}}
    --dashboard-id {{DASHBOARDID}}
```

------

For more information about the `DeleteDashboard` API operation, see [DeleteDashboard](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DeleteDashboard.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
