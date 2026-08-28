---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-direct-connect-for-amazon-connect/amazon-connect-region-selection-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Connect Region selection considerations
<a name="amazon-connect-region-selection-considerations"></a>

 Amazon Connect Region selection is contingent upon data governance requirements, use case, services available in each Region, and latency in relation to your agents, contacts, and external transfer endpoint geography.
+  **Agent location and network** — CCP connectivity traverses the wide area network (WAN), so it is important that the workstation has the lowest latency and fewest [hops](https://en.wikipedia.org/wiki/Hop_(networking)) possible, specifically to the AWS Region where your resources and Amazon Connect instance are hosted. For example, [hub-and-spoke](https://en.wikipedia.org/wiki/Spoke%E2%80%93hub_distribution_paradigm) networks that need to make several hops to reach an edge router can add latency and reduce the quality of experience.

   When you set up your instance and agents, make sure to create your instance in the Region that is geographically closest to the agents. If you need to set up an instance in a specific Region to comply with company policies or other regulations, choose the configuration that results in the fewest network hops between your agents' computers and your Amazon Connect instance.
+  **Location of your callers** — Because calls are anchored to your Amazon Connect Region endpoint, they are subject to public switched telephone network (PSTN) latency. Ideally your callers and transfer endpoints are geographically located as closely as possible to the AWS Region where your Amazon Connect instance is hosted for lowest latency.

   For optimal performance, and to limit the latency for your customers when they call in to your contact center, create your Amazon Connect instance in the Region that is geographically closest to where your customers call from. You might consider creating multiple Amazon Connect instances and provide contact information to customers for the number that is closest to where they call from.

   External transfers from Amazon Connect remain anchored to your Amazon Connect Region endpoint for the duration of the call. Per-minute usage continues to accrue until the call is disconnected by the recipient of the transferred call. The call is not recorded after the agent drops or the transfer completes. The contact record data and associated call recording of a transferred call are generated after the call is ended. Whenever possible, don't transfer calls that could be transferred back into Amazon Connect, known as circular transfers, to avoid compounding PSTN latency.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
