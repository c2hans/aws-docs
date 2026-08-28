---
source_url: https://docs.aws.amazon.com/mgn/latest/ug/mgn-connector.html
---

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# MGN Connectors
<a name="mgn-connector"></a>

MGN connectors enable you to run commands on multiple source servers. Use connectors for large-scale migrations with multiple operating system types and versions, which may be distributed across multiple data centers. A connector can also help:
+ Verify the prerequisites are met for installation of the MGN replication agent on the source servers.
+ Install the MGN replication agents on the source servers.

You can install the MGN connector in your source environment and use it to perform actions on source servers in your data center.

This feature, combined with the post-launch action framework, offers automation across the entire deployment process.

**Note**
The MGN connector is not supported for IPv6.

**Topics**
+ [Prerequisites for installing the MGN connector](mgn-connector-prerequisites.md)
+ [Architecture overview for MGN connector](mgn-connector-architecture.md)
+ [IAM roles needed for the MGN connector](mgn-connector-permissions.md)
+ [Set up the MGN Connector](mgn-connector-setup-instructions.md)
+ [Installing the MGN connector on a secured network](mgn-connector-installing-secured-network.md)
+ [Manage your MGN Connectors](mgn-connector-main.md)
+ [Review details about your MGN connectors](connector-details.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transform MGN. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
