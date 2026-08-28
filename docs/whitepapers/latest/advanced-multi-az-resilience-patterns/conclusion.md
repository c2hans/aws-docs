---
source_url: https://docs.aws.amazon.com/whitepapers/latest/advanced-multi-az-resilience-patterns/conclusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Conclusion
<a name="conclusion"></a>

 This paper provided an overview of gray failures, how they manifest, and outlined why you need to build observability and evacuation tooling to mitigate those types of events when they occur. In the next section, you reviewed multi-AZ observability and three approaches you can implement to detect single Availability Zone impact. In the last section, this paper presented two general approaches for performing Availability Zone evacuation. The first approach uses data plane actions to prevent work from being routed to the impacted Availability Zone while the second approach uses control plane actions to prevent capacity from being provisioned in the impacted Availability Zone. Together, these two approaches achieve the two outcomes that Availability Zone evacuation intends.

 The recovery patterns described in this paper will likely be part of a larger monitoring and fault recovery solution. This approach to dealing with single-Availability Zone gray failures requires engineering work to build the instrumentation necessary to detect them as well as the tooling to respond to them. However, for many workloads, this approach can be a simpler and less costly alternative to building multi-Region architectures. Additionally, it can help achieve smaller RPOs and RTOs (which increases the workload’s availability) when compared to multi-Region DR.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
