---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/amazon-emr-hardware/capacity.html
---

# Estimating Amazon EMR cluster capacity
<a name="capacity"></a>

Although Amazon EMR is a resizable platform, it's important to right-size the clusters. Right-sizing avoids a slow cluster, if undersized, or higher costs, if the cluster is oversized. To anticipate these issues, you can calculate the number and type of nodes that will be needed for the workloads.

## Primary nodes
<a name="primary-nodes"></a>

This type of node is responsible for coordinating the distribution of data and processes. As mentioned before, the computational requirements for primary nodes are low. You can use a single primary node to manage your Amazon EMR cluster. However, you can use up to three primary nodes so that you don't have a single point of failure. If one primary node fails, Amazon EMR fails over to one of the other two primary nodes.

## Core and task nodes
<a name="core-and-task-nodes"></a>

The difference between core and task nodes is that task nodes do not store data; they only provide power to perform parallel computational tasks.

To calculate the number of core and task nodes, you must know the size of your data and your approximate memory usage.

### Core nodes
<a name="core-nodes.af270bd8-3327-5801-8e92-473826f25950"></a>

Core nodes are responsible for running tasks to process the data and also store data in the Hadoop Distributed File System (HDFS). To calculate the capacity of the core nodes, define the number of core nodes, and then multiply the number of nodes by the Amazon Elastic Block Store (Amazon EBS) storage of each node.

For example, if you define 10 core nodes to process 1 TiB of data, and you have an `m5.xlarge` instant type with 64 GiB of Amazon EBS storage, you have `10 nodes * 64 GiB`, or 640 GiB of capacity. Based on the HDFS [replication factor](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-instances-guidelines.html) of three, your data size is replicated three times in the nodes, so 1 TiB of data requires a capacity of 3 TiB. Because this example has only 640 GiB, you must increase the number of nodes or change the instance type until you have a capacity of 3 TiB.

The `m5.4xlarge` instance type has 256 GiB of storage. Changing to an `m5.4xlarge` instance type and selecting 12 instances provides enough capacity.

`12 instances * 256 GiB of storage = 3072 GiB = 3 TiB available`

### Task nodes
<a name="task-nodes.5436bd58-9328-5bae-b622-0df08e0ceca2"></a>

Task nodes only run tasks. They don't store data. To calculate the number of task nodes, you need an estimate of the memory usage. This capacity can be split into core and task nodes. To calculate the number of task nodes needed, you can subtract the memory provided by the core nodes that you calculated in the previous step from the memory usage.

To have an extended range of memory, it's a best practice to multiply the memory needed by three.

Suppose that you have 28 processes of 20 GiB each.

`3 * 28 processes * 20 GiB of memory = 1680 GiB of memory`

For this example, your core nodes have 64 GiB of memory (`m5.4xlarge` instances). Your core nodes provide `64 GiB * 12 nodes = 768 GiB of memory`, which is not enough in this example.

To find the shortage, subtract the core node memory from the total memory required.

`1680 GiB total memory – 768 GiB core node memory = 912 GiB memory shortage`.

Task nodes can provide the remaining 912 GiB of memory. For this example, your task nodes have 32 GiB of memory (`m5.2xlarge` instances). To obtain the number of task nodes needed, divide the memory shortage by the instance type memory

`912 GiB/32 GiB = 28.5 task nodes`

You can't have a fraction of a task node, so you need to round up to 29 task nodes.
