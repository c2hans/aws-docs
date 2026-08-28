---
source_url: https://docs.aws.amazon.com/mediapackage/latest/userguide/channels.html
---

# Working with channels in AWS Elemental MediaPackage
<a name="channels"></a>

A channel is part of a channel group and represents the entry point for a content stream into MediaPackage. After you create a channel, MediaPackage provides ingest endpoint domains for its lifetime, regardless of any failures or upgrades that might occur.

Upstream encoders such as AWS Elemental MediaLive send content to the channel. When MediaPackage receives a content stream, it packages the content and outputs the stream from an origin endpoint that you create on the channel. Each incoming set of adaptive bitrate (ABR) streams has one channel. A channel group can have multiple channels.

For supported live inputs and codecs, see [Supported inputs and outputs](supported-inputs.md).

**Topics**
+ [Creating a channel](channels-create.md)
+ [Viewing channel details](channels-view.md)
+ [Editing a channel](channels-edit.md)
+ [Resetting channel history](channel-reset.md)
+ [Deleting a channel](channels-delete.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaPackage V2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediapackage` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
