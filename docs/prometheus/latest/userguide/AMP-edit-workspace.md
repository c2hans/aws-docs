---
source_url: https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-edit-workspace.html
---

# Edit a workspace alias
<a name="AMP-edit-workspace"></a>

You can edit a workspace to change its alias. To change the workspace alias using the AWS CLI, enter the following command.

```
aws amp update-workspace-alias --workspace-id {{my-workspace-id}} --alias "{{new-alias}}"
```

**To edit a workspace using the Amazon Managed Service for Prometheus console**

1. Open the Amazon Managed Service for Prometheus console at [https://console.aws.amazon.com/prometheus/](https://console.aws.amazon.com/prometheus/home).

1. In the upper left corner of the page, choose the menu icon and then choose **All workspaces**.

1. Choose the workspace ID of the workspace that you want to edit, and then choose **Edit**.

1. Enter a new alias for the workspace and then choose **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Prometheus. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prometheus` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
