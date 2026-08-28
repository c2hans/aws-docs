---
source_url: https://docs.aws.amazon.com/vpc/latest/reachability/manage-delegated-administrators.html
---

# Manage delegated administrator accounts in Reachability Analyzer
<a name="manage-delegated-administrators"></a>

You can register up to 5 delegated administrator accounts in Reachability Analyzer. If you deregister a delegated administrator account, the users in the account can't run a new cross-account analysis, but they can still see the previously run analyses.

**To manage delegated administrators**

1. Sign in to the management account.

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home).

1. From the navigation pane, choose **Reachability Analyzer**, **Settings**.

1. To register a member account as a delegated administrator account, choose **Register delegated administrator**. Select the check box for the account, and then choose **Register delegated administrator**.

1. To deregister a delegated administrator account, select the check box for the account, and then choose **Deregister**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
