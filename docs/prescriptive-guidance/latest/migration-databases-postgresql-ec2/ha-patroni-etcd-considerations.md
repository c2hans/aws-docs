---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/ha-patroni-etcd-considerations.html
---

# Patroni and etcd
<a name="ha-patroni-etcd-considerations"></a>

We recommend [Patroni](https://github.com/zalando/patroni) as a solution for providing HA with automatic failover management. Patroni is an open-source automatic failover manager for PostgreSQL databases. You can use Patroni as a template to create your own customized HA solution by using Python and a distributed configuration store, such as [etcd](https://github.com/etcd-io/etcd), for maximum accessibility.

Patroni also provides APIs to check the status of the PostgreSQL service and the roles of each DB instance or node. You must install Patroni on each DB instance for it to work with etcd (distributed configuration store).

By default, Patroni configures PostgreSQL for asynchronous replication. Choosing your replication method is dependent on your business considerations. Patroni is one of the best tools for setting up HA because it's highly configurable. Here are some of the advantages of using Patroni:

1. It's easy to switch between different modes of replication (synchronous and asynchronous).

1. Patroni has a rich REST API. Patroni uses this API for itself to perform failovers during the leader race by using [HAProxy](https://www.haproxy.org/) or another load balancer to perform HTTP health checks.

1. Patroni must temporarily step down from managing the cluster, while still retaining the cluster state in the Distributed Configuration Store (DCS). For example, you don't want a failover to happen during a manual maintenance window. Patroni offers pause and resume commands so that you can avoid unwanted downtime.

1. To avoid the split-brain problem, Patroni must ensure that PostgreSQL won't accept any transaction commits after the leader key expires in the DCS. Patroni also supports devices like Watchdog to avoid the split-brain problem. For more information on the split-brain problem and Watchdog, see [Watchdog support](https://patroni.readthedocs.io/en/latest/watchdog.html?highlight=split-brain#watchdog-support) in the Patroni documentation.

## Architecture
<a name="architecture-ha-patroni-etcd"></a>

The following diagram shows the architecture for setting up HADR for your on-premises PostgreSQL database on Amazon EC2 by using Patroni and etcd.

![Patroni architecture](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-databases-postgresql-ec2/images/guide-img/d9d57133-1a8b-4b7f-bbe9-e908969d06b9/images/d12a60c9-7866-48e1-92f8-461c4c65ed77.png)

The diagram shows the following workflow:

1. Create EC2 instances.

1. Install a PostgreSQL database.

1. Install and configure Patroni on EC2 instances.

1. Create and configure a Network Load Balancer.

1. Configure each PostgreSQL database in etcd** **(for Patroni) to get HA.

## Patroni
<a name="ha-patroni-etcd-limitations"></a>

We recommend that you consider the following before starting your migration by using Patroni:
+ Users must have PostgreSQL administration and DCS expertise to use Patroni.
+ Patroni has a steep learning curve and many configuration options to choose from.
+ You must have extra ports dedicated to Patroni.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
