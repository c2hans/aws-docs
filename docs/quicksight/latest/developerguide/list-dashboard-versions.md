---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/list-dashboard-versions.html
---

# ListDashboardVersions
<a name="list-dashboard-versions"></a>

Use the `ListDashboardVersions` API operation to list all the versions of a dashboard in an AWS account. To use this operation, you need the ID of the dashboard that you want to update. The dashboard ID is part of the dashboard URL in Quick Sight. You can also use the `ListDashboards` API operation to get the ID.

Following is an example AWS CLI command for this operation.

------
#### [ AWS CLI ]

```
aws quicksight list-dashboard-versions
    --aws-account-id {{AWSACCOUNTID}}
    --dashboard-id {{DASHBOARD}}
    --page-size {{10}}
    --max-items {{100}}
```

------

For more information about the `ListDashboardVersions` API operation, see [ListDashboardVersions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ListDashboardVersions.html) in the *Amazon Quick Sight API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
