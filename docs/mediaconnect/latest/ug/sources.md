---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/sources.html
---

# Managing sources in MediaConnect
<a name="sources"></a>

 A source in MediaConnect can be anything that provides a live video feed, such as the following:
+ An on-premises encoder
+ Another AWS Elemental MediaConnect flow
+ An AWS Elemental MediaLive output
+ A playout system (cloud-based or on-premises)

For a list of supported protocols that you can use for your source, see [Protocols](protocols.md).

From the MediaConnect console, you can view Amazon CloudWatch metrics to [monitor the source health](monitor-source-health.md) of an active flow.

**Topics**
+ [Using NDI® sources in a MediaConnect flow](sources-using-ndi.md)
+ [Adding a second source to an existing MediaConnect flow](source-adding.md)
+ [Updating the source of a MediaConnect flow](source-update.md)
+ [Source failover on a MediaConnect flow](source-failover.md)
+ [Managing tags on a MediaConnect source](sources-manage-tags.md)
+ [Removing a source from a MediaConnect flow](source-remove.md)
+ [Source ports on MediaConnect flows](source-ports.md)
+ [Determining a source's peer IP address](source-ip-address.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
