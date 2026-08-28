---
source_url: https://docs.aws.amazon.com/fsx/latest/WindowsGuide/new-smbshare-fails.html
---

# New-FSxSmbShare command fails with a one-way trust
<a name="new-smbshare-fails"></a>

Amazon FSx does not support executing the `New-FSxSmbShare` PowerShell command in cases where you have a one-way trust and the domain in which the user resides is not configured to trust the domain associated with Amazon FSx file system.

You can resolve this situation using one of following solutions:
+ The user executing the `New-FSxSmbShare` command needs to be in the same domain as the FSx file system.
+ You can use the fsmgmt.msc GUI to create shares on your file system. For more information, see [Managing file shares with the Shared Folders GUI](managing-file-shares.md#shared-folders-tool).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
