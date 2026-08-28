---
source_url: https://docs.aws.amazon.com/servicequotas/latest/userguide/stopping-automatic-management.html
---

# Stopping Service Quotas Automatic Management
<a name="stopping-automatic-management"></a>

Use the following procedure to stop Service Quotas Automatic Management of service quotas for supported AWS services in your AWS account using the AWS Management Console or AWS CLI.

------
#### [ AWS Management Console ]

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **Automatic Management**.

1. Choose **Stop Automatic Management** at the top corner of the page.

1. Confirm your selection in the confirmation pop-up box.

------
#### [ AWS CLI ]

Use the following command to stop Automatic Management. Replace the {{italicized placeholder text}} in the example command with your information.

```
aws service-quotas stop-auto-management-configuration --region {{ca-central-1}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Service Quotas. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicequotas` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
