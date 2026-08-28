---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/source-adding.html
---

# Adding a second source to an existing MediaConnect flow
<a name="source-adding"></a>

For transport stream flows, you can add a second source for failover. Both sources on the flow must use the same protocol. (However, you can have one source that uses RTP and the other that uses RTP-FEC.) For more information about source failover, see [Source failover](source-failover.md).

The method you use to add a second source to a flow is dependent on the type of source that you want to use:
+ [Standard source](source-adding-standard.md) – Uses content from any source that is not a VPC source or an entitled source.
+ [VPC source](source-adding-vpc.md) – Uses content that comes from a VPC that you configure.

MediaConnect doesn't support two sources on the following types of flow:
+ Flows with an entitled source
+ Flows with a CDI source
+ Flows with an NDI® source

 For redundancy with ST 2110 JPEG XS sources, you can specify two inbound VPC interfaces on an individual media stream. For redundancy with CDI sources, create a second flow.

From the MediaConnect console, you can view Amazon CloudWatch metrics to [monitor the source health](monitor-source-health.md) of an active flow.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
