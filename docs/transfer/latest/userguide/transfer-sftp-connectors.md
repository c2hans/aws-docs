---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/transfer-sftp-connectors.html
---

# Using SFTP connectors
<a name="transfer-sftp-connectors"></a>

This topic describes how to perform the supported file operations using your SFTP connector. You can also find example commands to perform these operations by selecting your connector's details on the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/).

After you have created an SFTP connector, you can use it to perform the following file operations on the remote SFTP server that it's associated with.
+ Send files from Amazon S3 to the remote SFTP server.
+ Retrieve files from the remote SFTP server to Amazon S3.
+ List files and sub-folders from a directory on the remote SFTP server.
+ Delete, rename or move files and directories on the remote SFTP server.

For details on creating connectors, see [Creating SFTP connectors](configure-sftp-connector.md).

**Topics**
+ [Transfer files](transfer-files-and-track.md)
+ [List contents of a remote directory](sftp-connector-list-dir.md)
+ [Move, rename, or delete files or directories on the remote server](move-delete-remote-files.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
