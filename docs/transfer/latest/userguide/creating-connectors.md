---
source_url: https://docs.aws.amazon.com/transfer/latest/userguide/creating-connectors.html
---

# AWS Transfer Family SFTP connectors
<a name="creating-connectors"></a>

An AWS Transfer Family SFTP connector establishes a connection with a remote SFTP server to transfer files between Amazon storage and a remote server, using the SFTP protocol. You can send files from Amazon S3 to an external, partner-owned SFTP server, retrieve files from a partner's SFTP server to Amazon S3 or list, delete, rename or move files on the remote server. SFTP connectors support two egress types: service managed (using AWS managed infrastructure) and VPC (routing through your VPC using Amazon VPC Lattice ). Using SFTP connectors, you can build automated, event-driven file transfer workflows in AWS .

The following video provides a brief introduction to Transfer Family SFTP connectors.

[![AWS Videos](http://img.youtube.com/vi/Gm-FMGrVpAg/0.jpg)](http://www.youtube.com/watch?v=Gm-FMGrVpAg)

**Topics**
+ [Creating SFTP connectors](configure-sftp-connector.md)
+ [VPC connectivity for SFTP connectors](sftp-connectors-vpc-overview.md)
+ [Using SFTP connectors](transfer-sftp-connectors.md)
+ [Monitoring SFTP connectors](track-connector-progress.md)
+ [Managing SFTP connectors](manage-sftp-connectors.md)
+ [Scaling and quotas for SFTP connectors](scale-and-limits-sftp-connector.md)
+ [Reference architectures using SFTP connectors](reference-architectures.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
