---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/write-to-your-region.html
---

# Write to your Region mode (mixed primary)
<a name="write-to-your-region"></a>

The *write to your Region* write mode, illustrated in the following diagram, works with MREC tables. It assigns different data subsets to different home Regions and allows write operations to an item only through its home Region. This mode is active-passive but assigns the active Region based on the item. Every Region is primary for its own non-overlapping dataset, and write operations must be guarded to ensure proper locality.

This mode is similar to *write to one Region* except that it enables lower-latency write operations, because the data associated with each user can be placed in closer network proximity to that user. It also spreads the surrounding infrastructure more evenly between Regions and requires less work to build out infrastructure during a failover scenario, because all Regions have a portion of their infrastructure already active.

![Write to your Region write mode](http://docs.aws.amazon.com/prescriptive-guidance/latest/dynamodb-global-tables/images/guide-img/a90e395c-d4d5-48a9-a714-90406b23d110/images/1d3532d5-dc62-4a9e-aec0-a9132b60780f.png)

You can determine the home Region for items in several ways:
+ Intrinsic: Some aspect of the data, such as a special attribute or a value embedded within its partition key, makes its home Region clear. This technique is described in the blog post [Use Region pinning to set a home Region for items in an Amazon DynamoDB global table](https://aws.amazon.com/blogs/database/use-region-pinning-to-set-a-home-region-for-items-in-an-amazon-dynamodb-global-table/).
+ Negotiated: The home Region of each dataset is negotiated in some external manner, such as with a separate global service that maintains assignments. The assignment might have a finite duration after which it's subject to renegotiation.
+ Table-oriented: Instead of creating a single replicating global table, you create the same number of global tables as replicating Regions. Each table's name indicates its home Region. In standard operations, all data is written to the home Region while other Regions keep a read-only copy. During a failover, another Region temporarily adopts write duties for that table.

For example, imagine that you're working for a gaming company. You need low-latency read and write operations for all gamers around the world. You assign each gamer to the Region that's closest to them. That Region takes all their read and write operations, ensuring strong read-after-write consistency. However, when a gamer travels or if their home Region suffers an outage, a complete copy of their data is available in alternative Regions, and the gamer can be assigned to a different home Region.

As another example, imagine that you're working at a video conferencing company. Each conference call's metadata is assigned to a particular Region. Callers can use the Region that's closest to them for lowest latency. If there's a Region outage, using global tables allows quick recovery because the system can move the processing of the call to a different Region where a replicated copy of the data already exists.

To summarize:
+ *Write to any Region* mode is suitable for MRSC tables and idempotent calls to MREC tables.
+ *Write to one Region* mode is suitable for non-idempotent calls to MREC tables.
+ *Write to your Region* mode is suitable for non-idempotent calls to MREC tables, where it's important to have clients write to a Region that's close to them.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
