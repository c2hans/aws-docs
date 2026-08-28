---
source_url: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lifecycle.html
---

# Amazon EBS snapshot lifecycle
<a name="ebs-snapshot-lifecycle"></a>

The lifecycle of an Amazon EBS snapshot starts with the creation process. You create snapshots from Amazon EBS volumes. You can use snapshots to restore new Amazon EBS volumes. You can create copies of snapshots either in the same Region, or in different Regions. You can share snapshots with other AWS accounts, either publicly or privately. Those accounts can restore volumes from the shared snapshots, or they can create copies of the shared snapshots in their own account. If you don't need immediate access to a snapshot, you can archive it to save on storage costs.

The following image shows actions that you can perform on your snapshots as part of the snapshot lifecycle.

![Snapshot lifecycle](http://docs.aws.amazon.com/ebs/latest/userguide/images/snapshot-lifecycle.png)

**Topics**
+ [Create snapshots](ebs-creating-snapshot.md)
+ [View snapshot information](ebs-describing-snapshots.md)
+ [Copy a snapshot](ebs-copy-snapshot.md)
+ [Share a snapshot](ebs-modifying-snapshot-permissions.md)
+ [Archive snapshots](snapshot-archive.md)
+ [Delete a snapshot](ebs-deleting-snapshot.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EBS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ebs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
