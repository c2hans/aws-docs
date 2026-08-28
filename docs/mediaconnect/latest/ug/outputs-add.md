---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-add.html
---

# Adding outputs to a MediaConnect flow
<a name="outputs-add"></a>

For transport stream flows, you can add up to 50 outputs. However, for optimal performance, follow the guidance offered in [Best practices](best-practices.md). Every output must have a name, a [protocol](protocols.md), an IP address, and a port.

**Note**
If you intend to set up an entitlement for an output, don't create the output. Instead, [grant an entitlement](entitlements-grant.md). When the subscriber creates a flow using your content as the source, the service creates an output on your flow.

The method you use to add an output to a flow is dependent on the type of output that you want to add:
+ [Standard output (transport stream flow)](outputs-add-standard.md) – Sends compressed content to any destination that is not a virtual private cloud (VPC) that you configured using Amazon Virtual Private Cloud.
+ [VPC output (transport stream flow)](outputs-add-vpc.md) – Sends compressed content to a VPC that you configured using Amazon Virtual Private Cloud.
+ [NDI® output (transport stream flow)](outputs-add-ndi.md) – Sends high-quality, low-latency content over IP networks so that it can be received by the production systems within your VPC network.
+ [VPC output (CDI flow)](outputs-add-vpc.md) – Sends uncompressed content to a VPC that you configured using Amazon Virtual Private Cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
