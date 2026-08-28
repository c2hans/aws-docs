---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/describe-dashboard-permissions.html
---

# DescribeDashboardPermissions
<a name="describe-dashboard-permissions"></a>

Use the `DescribeDashboardPermissions` API operation to view the read and write permissions for a dashboard. To use this operation, you need the ID of the dashboard whose permissions you want to view. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight describe-dashboard-permissions
    --aws-account-id {{555555555555}}
    --dashboard-id {{111122223333}}
```

------

For more information about the `DescribeDashboardPermissions` API operation, see [DescribeDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardPermissions.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
