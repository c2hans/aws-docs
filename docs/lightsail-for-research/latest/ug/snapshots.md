---
source_url: https://docs.aws.amazon.com/lightsail-for-research/latest/ug/snapshots.html
---

# Backup virtual computers and disks with Lightsail for Research snapshots
<a name="snapshots"></a>

Snapshots are a point-in-time copy of your data. You can create snapshots of your Amazon Lightsail for Research virtual computers and storage disks, and use them as baselines to create new computers or for data backup.

A snapshot contains all of the data that's needed to restore your computer (from the moment when the snapshot was taken). When you create a new virtual computer from a snapshot, it begins as an exact replica of the original computer that was used to create the snapshot.

Because your resources might fail at any time, we recommend creating frequent snapshots to avoid permanent data loss.

**Topics**
+ [Create snapshots of Lightsail for Research virtual computers or disks](create-snapshot.md)
+ [View and manage virtual computer and disk snapshots in Lightsail for Research](view-snapshots.md)
+ [Create a virtual computer or disk from a snapshot](create-computer-from-snapshot.md)
+ [Delete a snapshot in the Lightsail for Research console](delete-snapshot.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail for Research. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail-for-research` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
