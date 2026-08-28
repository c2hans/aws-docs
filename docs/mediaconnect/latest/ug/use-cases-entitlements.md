---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/use-cases-entitlements.html
---

# MediaConnect use case: entitlements
<a name="use-cases-entitlements"></a>

Entitlements allow one AWS account holder to share content in a transport stream flow with other AWS account holders. For example, a sports company wants to share a flow (Baseball-Game) with a local TV station. A sports broadcaster (the originator) creates an entitlement on the Baseball-Game flow to allow access for the local TV station (the subscriber). The local TV station creates an AWS Elemental MediaConnect flow using an output from the Baseball-Game flow as the source.

The subscriber must set up their flow in MediaConnect in the same Region as the originator's flow.

This following illustration shows how to share content in a transport stream flow with another AWS subscriber. The output of the originator's flow can be used as the source of the subscriber's flow.

![This illustration shows how to share content with another AWS subscriber. The output of the originator's flow can be used as the source of the subscriber's flow.](http://docs.aws.amazon.com/mediaconnect/latest/ug/images/use-case-entitlementv2.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
