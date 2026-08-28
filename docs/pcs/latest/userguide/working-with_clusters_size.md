---
source_url: https://docs.aws.amazon.com/pcs/latest/userguide/working-with_clusters_size.html
---

# Cluster size in AWS PCS
<a name="working-with_clusters_size"></a>

AWS PCS provides highly available and secure clusters, while automating key tasks such as patching, node provisioning, and updates.

When you create a cluster, you select a size for it based on two factors:
+  The number of compute nodes it will manage
+  The number of jobs tracked by the controller at any given time

**Note**
The job count includes running, pending, and recently completed jobs. Completed jobs remain tracked by the controller for a short period before being purged. During high job throughput, this can cause the total tracked job count to exceed the number of active jobs you observe.

**Important**
You can't change the cluster size after you create the cluster. If you need to change the size, you must create a new cluster.

| Slurm cluster size | Number of instances managed | Number of jobs tracked by the controller |
| --- | --- | --- |
| Small | Up to 32 | Up to 256 |
| Medium | Up to 512 | Up to 8192 |
| Large | Up to 2048 | Up to 16384 |

**Examples**
+ If your cluster will have up to 24 managed instances and run up to 100 jobs, choose **Small**.
+ If your cluster will have up to 24 managed instances and run up to 1000 jobs, choose **Medium**.
+ If your cluster will have up to 1000 managed instances and run up to 100 jobs, choose **Large**.
+ If your cluster will have up to 1000 managed instances and run up to 10,000 jobs, choose **Large**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
