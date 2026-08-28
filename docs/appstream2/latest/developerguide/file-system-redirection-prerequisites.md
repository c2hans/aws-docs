---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/file-system-redirection-prerequisites.html
---

# Prerequisites for File System Redirection
<a name="file-system-redirection-prerequisites"></a>

To enable WorkSpaces Applications file redirection:
+ You must use an image that uses a version of the WorkSpaces Applications agent released on or after August 8, 2019. For more information, see [WorkSpaces Applications Agent Release Notes](agent-software-versions.md).
+ Your users must have WorkSpaces Applications client version 1.0.480 or later installed. For more information, see [WorkSpaces Applications Windows Client Release Notes](client-release-versions.md).
+ File upload and download must be enabled on the stack that your users access for streaming sessions. See the following procedure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
