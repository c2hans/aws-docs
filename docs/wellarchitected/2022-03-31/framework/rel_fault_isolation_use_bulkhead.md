---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/rel_fault_isolation_use_bulkhead.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# REL10-BP04 Use bulkhead architectures to limit scope of impact
<a name="rel_fault_isolation_use_bulkhead"></a>

 Like the bulkheads on a ship, this pattern ensures that a failure is contained to a small subset of requests or clients so that the number of impaired requests is limited, and most can continue without error. Bulkheads for data are often called partitions, while bulkheads for services are known as cells.

 In a *cell-based architecture*, each cell is a complete, independent instance of the service and has a fixed maximum size. As load increases, workloads grow by adding more cells. A partition key is used on incoming traffic to determine which cell will process the request. Any failure is contained to the single cell it occurs in, so that the number of impaired requests is limited as other cells continue without error. It is important to identify the proper partition key to minimize cross-cell interactions and avoid the need to involve complex mapping services in each request. Services that require complex mapping end up merely shifting the problem to the mapping services, while services that require cross-cell interactions create dependencies between cells (and thus reduce the assumed availability improvements of doing so).

![Diagram showing Cell-based architecture](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/cell-based-architecture.png)

 In his AWS blog post, Colm MacCarthaigh explains how Amazon Route 53 uses the concept of [*shuffle sharding*](https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation/) to isolate customer requests into shards. A shard in this case consists of two or more cells. Based on partition key, traffic from a customer (or resources, or whatever you want to isolate) is routed to its assigned shard. In the case of eight cells with two cells per shard, and customers divided among the four shards, 25% of customers would experience impact in the event of a problem.

![Diagram showing a service divided into traditional shards](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/service-divided-into-traditional-shards.png)

 With shuffle sharding, you create virtual shards of two cells each, and assign your customers to one of those virtual shards. When a problem happens, you can still lose a quarter of the whole service, but the way that customers or resources are assigned means that the scope of impact with shuffle sharding is considerably smaller than 25%. With eight cells, there are 28 unique combinations of two cells, which means that there are 28 possible shuffle shards (virtual shards). If you have hundreds or thousands of customers, and assign each customer to a shuffle shard, then the scope of impact due to a problem is just 1/28th. That’s seven times better than regular sharding.

![Diagram showing a service divided into shuffle shards.](http://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/images/service-divided-into-shuffle-shards.png)

 A shard can be used for servers, queues, or other resources in addition to cells.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Use bulkhead architectures. Like the bulkheads on a ship, this pattern ensures that a failure is contained to a small subset of requests or users so that the number of impaired requests is limited, and most can continue without error. Bulkheads for data are often called partitions, while bulkheads for services are known as cells.
  +  [Well-Architected lab: Fault isolation with shuffle sharding](https://wellarchitectedlabs.com/reliability/300_labs/300_fault_isolation_with_shuffle_sharding/)
  +  [Shuffle-sharding: AWS re:Invent 2019: Introducing The Amazon Builders’ Library (DOP328)](https://youtu.be/sKRdemSirDM?t=1373)
  +  [AWS re:Invent 2018: How AWS Minimizes the Blast Radius of Failures (ARC338)](https://youtu.be/swQbA4zub20)
+  Evaluate cell-based architecture for your workload. In a cell-based architecture, each cell is a complete, independent instance of the service and has a fixed maximum size. As load increases, workloads grow by adding more cells. A partition key is used on incoming traffic to determine which cell will process the request. Any failure is contained to the single cell it occurs in, so that the number of impaired requests is limited as other cells continue without error. It is important to identify the proper partition key to minimize cross-cell interactions and avoid the need to involve complex mapping services in each request. Services that require complex mapping end up merely shifting the problem to the mapping services, while services that require cross-cell interactions reduce the autonomy of cells (and thus the assumed availability improvements of doing so).
  +  In his AWS blog post, Colm MacCarthaigh explains how Amazon Route 53 uses the concept of shuffle sharding to isolate customer requests into shards
    +  [Shuffle Sharding: Massive and Magical Fault Isolation](https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Shuffle Sharding: Massive and Magical Fault Isolation](https://aws.amazon.com/blogs/architecture/shuffle-sharding-massive-and-magical-fault-isolation)
+  [The Amazon Builders' Library: Workload isolation using shuffle-sharding](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/)

 **Related videos:**
+  [AWS re:Invent 2018: How AWS Minimizes the Blast Radius of Failures (ARC338)](https://youtu.be/swQbA4zub20)
+  [Shuffle-sharding: AWS re:Invent 2019: Introducing The Amazon Builders’ Library (DOP328)](https://youtu.be/sKRdemSirDM?t=1373)

 **Related examples:**
+  [Well-Architected lab: Fault isolation with shuffle sharding](https://wellarchitectedlabs.com/reliability/300_labs/300_fault_isolation_with_shuffle_sharding/)
