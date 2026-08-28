---
source_url: https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication-configure.html
---

# Configure multi-Region replication for Amazon Keyspaces (for Apache Cassandra)
<a name="multiRegion-replication-configure"></a>

You can use the console, Cassandra Query Language (CQL), or the AWS Command Line Interface to create and manage multi-Region keyspaces and tables in Amazon Keyspaces.

This section provides examples of how to create and manage multi-Region keyspaces and tables. All tables that you create in a multi-Region keyspace automatically inherit the multi-Region settings from the keyspace.

For more information about supported configurations and features, see [Amazon Keyspaces multi-Region replication usage notes](multiRegion-replication_usage-notes.md).

**Topics**
+ [Configure the IAM permissions required to create multi-Region keyspaces and tables](howitworks_replication_permissions.md)
+ [Configure the IAM permissions required to add an AWS Region to a keyspace](howitworks_replication_permissions_addReplica.md)
+ [Create a multi-Region keyspace in Amazon Keyspaces](keyspaces-mrr-create.md)
+ [Add an AWS Region to a keyspace in Amazon Keyspaces](keyspaces-multi-region-add-replica.md)
+ [Check the replication progress when adding a new Region to a keyspace](keyspaces-multi-region-replica-status.md)
+ [Create a multi-Region table with default settings in Amazon Keyspaces](tables-mrr-create-default.md)
+ [Create a multi-Region table in provisioned mode with auto scaling in Amazon Keyspaces](tables-mrr-create-provisioned.md)
+ [Update the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-autoscaling.md)
+ [View the provisioned capacity and auto scaling settings for a multi-Region table in Amazon Keyspaces](tables-mrr-view.md)
+ [Turn off auto scaling for a table in Amazon Keyspaces](tables-mrr-autoscaling-off.md)
+ [Set the provisioned capacity of a multi-Region table manually in Amazon Keyspaces](tables-mrr-capacity-manually.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
