---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-emr-hardware/storage.html
---

# Choosing the right storage
<a name="storage"></a>

Configure your cluster's [instance types and capacity](capacity.md). Core and task nodes need processing and compute power, but only the core nodes store data. Select the most cost-effective type of storage for your core nodes.

When using Amazon EMR for processing large amount of data, you have several options for moving data from Amazon S3. The best option depends on your workload. The following sections provide some key points to consider when deciding which storage type is the right choice for you.

## Hadoop Distributed File System
<a name="hdfs"></a>

Hadoop Distributed File System (HDFS) is a distributed, scalable, and portable file system for Hadoop. An advantage of HDFS is data awareness between the Hadoop cluster nodes managing the clusters and the Hadoop cluster nodes managing the individual steps.

## When to use HDFS in Amazon EMR
<a name="hdfs-in-emr"></a>

When you have iterative reads on the same dataset or Disk I/O intensive workloads, you can use HDFS for caching intermediate results and as hot storage for processing data. HDFS is ephemeral, which means it is reclaimed when the instances are terminated.

### EMR File System
<a name="emr-file-system.19857b8f-67a3-5d30-a911-8733111c6e46"></a>

EMR File System (EMRFS) is an implementation of HDFS that Amazon EMR clusters typically use for reading and writing regular files from Amazon EMR directly to Amazon S3.

You can use EMRFS when you read the dataset one time in each run. EMRFS decouples storage from compute, so you don't need to provision core nodes specifically to store data, and you don't need to pay for data replication in HDFS. This results in lower costs, and it provides availability of the data for multiple clusters. You also have the advantage of retaining data after shutting down the cluster.
