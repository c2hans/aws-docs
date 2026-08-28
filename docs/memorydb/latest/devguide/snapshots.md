---
source_url: https://docs.aws.amazon.com/memorydb/latest/devguide/snapshots.html
---

# Snapshot and restore
<a name="snapshots"></a>

MemoryDB clusters automatically back up data to a Multi-AZ transactional log, but you can choose to create point-in-time snapshots of a cluster either periodically or on-demand. These snapshots can be used to recreate a cluster at a previous point or to seed a brand new cluster. The snapshot consists of the cluster's metadata, along with all of the data in the cluster. All snapshots are written to Amazon Simple Storage Service (Amazon S3), which provides durable storage. At any time, you can restore your data by creating a new MemoryDB cluster and populating it with data from a snapshot. With MemoryDB, you can manage snapshots using the AWS Management Console, the AWS Command Line Interface (AWS CLI), and the MemoryDB API.

**Topics**
+ [Snapshot constraints](snapshots-constraints.md)
+ [Snapshot costs](snapshots-costs.md)
+ [Scheduling automatic snapshots](snapshots-automatic.md)
+ [Making manual snapshots](snapshots-manual.md)
+ [Creating a final snapshot](snapshots-final.md)
+ [Describing snapshots](snapshots-describing.md)
+ [Copying a snapshot](snapshots-copying.md)
+ [Exporting a snapshot](snapshots-exporting.md)
+ [Restoring from a snapshot](snapshots-restoring.md)
+ [Seeding a new cluster with an externally created snapshot](snapshots-seeding-redis.md)
+ [Tagging snapshots](snapshots-tagging.md)
+ [Deleting a snapshot](snapshots-deleting.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon MemoryDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query memorydb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
