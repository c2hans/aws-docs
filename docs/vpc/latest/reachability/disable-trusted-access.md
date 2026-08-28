---
source_url: https://docs.aws.amazon.com/vpc/latest/reachability/disable-trusted-access.html
---

# Disable trusted access in Reachability Analyzer
<a name="disable-trusted-access"></a>

After you disable trusted access, the users in the management account and delegated administrator accounts can't run a new cross-account analysis in Reachability Analyzer. However, they can still see the previously run analyses. Before you can disable trusted access, you must deregister the delegated administrator accounts.

You can enable trusted access again after disabling it. However, you must first re-register the delegated administrator accounts.

**To disable trusted access using the console**

1. Sign in to the management account.

1. Open the Network Manager console at [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home).

1. From the navigation pane, choose **Reachability Analyzer**, **Settings**.

1. For **Trusted Access**, choose **Turn off trusted access**.

1. Do not close or navigate away from this page until you see a success notification indicating that trusted access is turned off. This can take several minutes.

**To disable trusted access using the AWS CLI**
From the management account, use the [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html) command.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Virtual Private Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vpc` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
