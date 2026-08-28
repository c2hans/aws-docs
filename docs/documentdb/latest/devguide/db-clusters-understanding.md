---
source_url: https://docs.aws.amazon.com/documentdb/latest/devguide/db-clusters-understanding.html
---

# Understanding clusters
<a name="db-clusters-understanding"></a>

Amazon DocumentDB separates compute and storage, and offloads data replication and backup to the cluster volume. A cluster volume provides a durable, reliable, and highly available storage layer that replicates data six ways across three Availability Zones. Replicas enable higher data availability and read scaling. Each cluster can scale up to 15 replicas.

| Noun | Description | API Operations (Verbs) |
| --- | --- | --- |
| Cluster | Consists of one or more instances and a cluster storage volume that manages the data for those instances. | `create-db-cluster`<br />`delete-db-cluster`<br />`describe-db-clusters`<br />`modify-db-cluster` |
| Instance | Reading and writing data to the cluster storage volume is done via instances. In a given cluster, there are two types of instances: primary and replica. A cluster always has one primary instance and can have 0–15 replicas. | `create-db-instance`<br />`delete-db-instance`<br />`describe-db-instances`<br />`modify-db-instance`<br />`describe-orderable-db-instance-options`<br />`reboot-db-instance` |
| Cluster volume | A virtual database storage volume that spans three Availability Zones, with each Availability Zone having two copies of the cluster data. | N/A |
| Primary instance | Supports both read and write operations, and performs all data modifications to the cluster volume. Each cluster has one primary instance. | N/A |
| Replica instance | Supports only read operations. Each Amazon DocumentDB cluster can have up to 15 replica instances in addition to the primary instance. Multiple replicas distribute the read workload. By locating replicas in separate Availability Zones, you can also increase database availability. | N/A |
| Cluster endpoint | An endpoint for an Amazon DocumentDB cluster that connects to the current primary instance for the cluster. Each Amazon DocumentDB cluster has a cluster endpoint and one primary instance. | N/A |
| Reader endpoint | An endpoint for an Amazon DocumentDB cluster that connects to one of the available replicas for that cluster. Each Amazon DocumentDB cluster has a reader endpoint. If there is more than one replica, the reader endpoint directs each connection request to one of the Amazon DocumentDB replicas. | N/A |
| Instance endpoint | An endpoint for an instance in an Amazon DocumentDB cluster that connects to a specific instance. Each instance in a cluster, regardless of instance type, has its own unique instance endpoint. | N/A |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
