---
source_url: https://docs.aws.amazon.com/codecommit/latest/userguide/troubleshooting-cf.html
---

# Troubleshooting configuration errors and AWS CodeCommit
<a name="troubleshooting-cf"></a>

The following information might help you troubleshoot configuration errors you might see when connecting with AWS CodeCommit repositories.

**Topics**
+ [Configuration error: Cannot configure AWS CLI credentials on macOS](#troubleshooting-cf1)

## Configuration error: Cannot configure AWS CLI credentials on macOS
<a name="troubleshooting-cf1"></a>

**Problem:** When you run `aws configure` to configure the AWS CLI, you see a `ConfigParseError` message.

**Possible fixes:** The most common cause for this error is that a credentials file already exists. Browse to \~/.aws and look for a file named `credentials`. Rename or delete that file, and then run **aws configure** again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodeCommit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codecommit` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
