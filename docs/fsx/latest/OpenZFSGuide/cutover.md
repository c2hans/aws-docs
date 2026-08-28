---
source_url: https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/cutover.html
---

# Cutting over to your Amazon FSx for OpenZFS file system
<a name="cutover"></a>

To cut over to your FSx for OpenZFS file system, do the following:
+ Disconnect all clients that write to the source file system.
+ Perform an **rsync** or **Robocopy** final file sync to ensure there is no data loss when cutting over.
+ Connect all clients to your FSx for OpenZFS file system.

Now your FSx for OpenZFS file system is available with the data from the source file system and is available for clients to read and write to it. To make this data accessible to clients and applications, see [Accessing your data](accessing-your-data.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
