---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/gettingStarted-connecting-private-link-considerations.html
---

# Considerations when using AWS PrivateLink for Neptune Analytics
<a name="gettingStarted-connecting-private-link-considerations"></a>

 Amazon VPC considerations apply to AWS PrivateLink for Neptune Analytics. For more information, see [ Interface endpoint considerations](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#vpce-interface-limitations) and [AWS PrivateLink quotas](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-limits-endpoints.html) in the AWS PrivateLink guide. Additionally, the following restrictions apply:

1.  The AWS PrivateLink for Neptune Analytics control plane i.e. `neptune-graph` service does not support [ VPC endpoint policies](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html). However, AWS PrivateLink for Neptune Analytics data plane i.e. `neptune-graph-data` service supports VPC endpoint policies.

1.  The AWS PrivateLink for Neptune Analytics supports [Federal Information Processing Standard (FIPS)](https://aws.amazon.com/compliance/fips/) endpoints in US East (N. Virginia), US East (Ohio), and US West (Oregon) for control plane API operations under the service name `neptune-graph-fips`. FIPS endpoints are not supported in any AWS region for AWS PrivateLink for data plane API operations.

1.  Transport Layer Security (TLS) 1.1 is **not** supported.

1.  Private and Hybrid Domain Name System (DNS) services are **not** supported.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
