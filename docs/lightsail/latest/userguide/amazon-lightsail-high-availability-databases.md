---
source_url: https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-high-availability-databases.html
---

# High availability databases in Lightsail
<a name="amazon-lightsail-high-availability-databases"></a>

A Lightsail high availability managed database provides failover support with a primary database in one Availability Zone, and a secondary standby database in another. We recommend high availability databases for production workloads that experience heavy use and require data redundancy. For development and test purposes, you can use a standard database that isn't high availability.

To create a high availability database, select one of the high availability database plans available in Lightsail when creating your managed database. For more information, see [Create a database](amazon-lightsail-creating-a-database.md) . You can also change your standard database to a high availability database. Create a snapshot of your standard database, create a new database from the snapshot, and choose a high availability plan. For more information, see [Create a database from a snapshot](amazon-lightsail-creating-a-database-from-snapshot.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
