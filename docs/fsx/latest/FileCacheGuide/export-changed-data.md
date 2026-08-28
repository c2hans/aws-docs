---
source_url: https://docs.aws.amazon.com/fsx/latest/FileCacheGuide/export-changed-data.html
---

# Exporting changes to the data repository
<a name="export-changed-data"></a>

You can export data and metadata changes, including POSIX metadata, from Amazon File Cache to a linked Amazon S3 or NFS data repository. Associated POSIX metadata includes ownership, permissions, and timestamps. To export changes from the cache, use HSM commands. When you export a file or directory using HSM commands, your cache exports only data files and metadata that were created or modified since the last export. For more information, see [Exporting files using HSM commands](exporting-files-hsm.md).

**Important**
For Amazon File Cache to export your data to your linked data repository, it must be stored in a UTF-8 compatible format.

**Topics**
+ [Exporting files using HSM commands](exporting-files-hsm.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
