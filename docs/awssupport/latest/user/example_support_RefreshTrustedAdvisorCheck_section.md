---
source_url: https://docs.aws.amazon.com/awssupport/latest/user/example_support_RefreshTrustedAdvisorCheck_section.html
---

# Use `RefreshTrustedAdvisorCheck` with a CLI
<a name="example_support_RefreshTrustedAdvisorCheck_section"></a>

The following code examples show how to use `RefreshTrustedAdvisorCheck`.

------
#### [ CLI ]

**AWS CLI**
**To refresh an AWS Trusted Advisor check**
The following `refresh-trusted-advisor-check` example refreshes the Amazon S3 Bucket Permissions Trusted Advisor check in your AWS account.

```
aws support refresh-trusted-advisor-check \
    --check-id {{"Pfx0RwqBli"}}
```
Output:

```
{
    "status": {
        "checkId": "Pfx0RwqBli",
        "status": "enqueued",
        "millisUntilNextRefreshable": 3599992
    }
}
```
For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) in the *AWS Support User Guide*.
+  For API details, see [RefreshTrustedAdvisorCheck](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/refresh-trusted-advisor-check.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Requests a refresh for the specified Trusted Advisor check.**

```
Request-ASATrustedAdvisorCheckRefresh -CheckId "checkid1"
```
+  For API details, see [RefreshTrustedAdvisorCheck](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Requests a refresh for the specified Trusted Advisor check.**

```
Request-ASATrustedAdvisorCheckRefresh -CheckId "checkid1"
```
+  For API details, see [RefreshTrustedAdvisorCheck](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using AWS Support with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Support. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awssupport` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
