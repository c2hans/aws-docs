---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/graph-snapshots.html
---

# Graph snapshots
<a name="graph-snapshots"></a>

 Neptune Analytics provides you the ability to create a named snapshot of your analytics graph, and also the ability to restore from existing graph snapshots. A graph snapshot is a compacted deep copy of your entire graph. Snapshots are created asynchronously, and do not affect the performance of your running graph. You can restore a snapshot into a new graph at any time.

**Topics**
+ [Creating a graph snapshot](graph-snapshots-creating.md)
+ [Listing existing graph snapshots](graph-snapshots-listing.md)
+ [Restoring from a graph snapshot](graph-snapshots-restoring.md)
+ [Deleting a graph snapshot](graph-snapshots-deleting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
