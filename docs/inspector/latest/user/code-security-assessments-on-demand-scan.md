---
source_url: https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-on-demand-scan.html
---

# Performing an on-demand scan
<a name="code-security-assessments-on-demand-scan"></a>

 You can perform an on-demand for your projects. When you perform an on-demand scan, a union of all your configured scan configurations is applied to your selected project. If your account is the delegated administrator account for an organization, you can perform an on-demand scan for projects that belong to member accounts. The following procedure describes how to perform an on-demand scan in the Amazon Inspector console.

**To perform an on-demand scan**

1.  Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home).

1.  From the navigation pane, choose **Code security**.

1.  Choose **Code repositories**.

1.  Select the project you want to scan, and then choose **On-demand** scan.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
