---
source_url: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/fsrm-file-management.html
---

# File Management Tasks
<a name="fsrm-file-management"></a>

Amazon FSx for Windows File Server does not support FSRM file management tasks. However, you can achieve common use cases such as data archiving and retention policies by using native PowerShell commands from client machines that have network access to your file system.

For example, you can use PowerShell scripts on client machines to:
+ Move or archive files based on age or last access time
+ Delete classified files that exceed a retention period
+ Copy files to archive storage based on classification properties

You can access files properties using the `Get-FsrmClassification` command and take actions based on the values.

To access FSRM classification properties or other FSRM metadata from client-side PowerShell scripts, the client machine must also have FSRM installed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
