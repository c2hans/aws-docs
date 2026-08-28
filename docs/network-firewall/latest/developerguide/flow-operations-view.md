---
source_url: https://docs.aws.amazon.com/network-firewall/latest/developerguide/flow-operations-view.html
---

# Viewing flow operations in Network Firewall
<a name="flow-operations-view"></a>

You can view the history of operations in your firewall and monitor the progress of ongoing operations. Network Firewall only stores capture and flush operations performed within the last 12 hours.

**To view operation history**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, under **Network Firewall**, choose **Firewalls**.

1. Choose the name of the firewall that you want to view.

1. Navigate to the **Firewall operation history** section.

1. Review the status of operations:
**In progress**
Operations that have not yet completed.
**Completed**
Operations that successfully completed.
**Failed**
Operations that could not be completed.
**Completed with errors**
Operations that experienced a timeout issue or an issue that prevented completion across all hosts. These operations may have flows missing from the results.

1. Choose any completed operation to view the summary of results.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query network-firewall` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
