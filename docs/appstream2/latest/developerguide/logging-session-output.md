---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/logging-session-output.html
---

# Logging Session Script Output
<a name="logging-session-output"></a>

When this option is enabled in the configuration file, WorkSpaces Applications automatically captures the output from the session script that is written to the standard out. This output is uploaded to an Amazon S3 bucket in your account. You can review the log files for troubleshooting or debugging purposes.

**Note**
The log files are uploaded when the session script returns a value, or the value set in **WaitingTime** has elapsed, whichever comes first.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
