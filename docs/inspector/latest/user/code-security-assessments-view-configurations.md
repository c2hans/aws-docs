---
source_url: https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-view-configurations.html
---

# Viewing scan configurations
<a name="code-security-assessments-view-configurations"></a>

 The following procedure describes how to view scan configurations in the Amazon Inspector console.

**Note**
 When you view your scan configuration at the organization level, some of the details in the **Code Security** screen will differ to reflect your AWS account.

**To view details for a scan configuration**

1.  Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1.  From the navigation pane, choose **Code Security**.

1.  Choose **Configurations** to view a list of your scan configurations. If you're the delegated administrator, the list include your organization’s scan configurations. You can see the name of each scan configuration and who created each scan configuration (AWS account ID or organization ID). You can also view which scanning types and scan analysis type are applied to the configuration. You can even filter your scan configuration by different fields in the search bar.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
