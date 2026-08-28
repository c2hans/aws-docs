---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-troubleshooting-utils.html
---

# EC2 Windows troubleshooting utilities
<a name="windows-troubleshooting-utils"></a>

The `EC2WinUtil` driver provides the following types of troubleshooting support for your Windows instance.

**Crash call stacks**
`EC2WinUtil` collects basic crash information from your instance and writes it out to the serial console. The following list includes some of the key details that the utility writes to the console.
+ Identification of the module that generated the fault.
+ The Windows error code associated with the event.
+ A stack trace of the most recent calls.
With these details, you can perform initial root cause analysis and determine if further analysis is needed. Output to the serial console also enables AWS to track crash trends for Amazon EC2 drivers, and diagnose large scale crash events.
`EC2WinUtil` doesn't collect any customer data in its crash call stacks.

For driver release notes, see [EC2 Windows Utility Driver version history](ec2winutil-driver-version-history.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
