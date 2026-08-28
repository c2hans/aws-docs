---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/channel-groups.html
---

# Working with channel groups in AWS Elemental MediaPackage
<a name="channel-groups"></a>

A channel group is the top-level resource that consists of channels and origin endpoints associated with it. After you create a channel group, MediaPackage provides a fixed egress domain for its lifetime, regardless of any failures or upgrades that might occur. All channels and origin endpoints belonging to this channel group use the same egress domain. Direct your CDNs to this domain for stream delivery from MediaPackage.

For each channel group, you add channels that define the entry point for a content stream into MediaPackage. You then add origin endpoints to the channels that define the packaging options for the output stream.

**Topics**
+ [Creating a channel group](channel-group-create.md)
+ [Viewing channel group details](channel-group-view.md)
+ [Editing a channel group](channel-group-edit.md)
+ [Deleting a channel group](channel-group-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
