---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/distribution-from-medialive.html
---

# Distributing content from an AWS Elemental MediaLive Multiplex
<a name="distribution-from-medialive"></a>

An AWS Elemental MediaLive [multiplex](https://docs.aws.amazon.com/medialive/latest/ug/eml-multiplex.html) creates a UDP transport stream (TS) that carries multiple programs, also known as a multi-program transport stream (MPTS). When you create a multiplex, MediaLive automatically grants an entitlement in MediaConnect for your account. Create a flow based on that entitlement and distribute the content from that flow.

**To distribute content from a MediaLive multiplex (console)**

1. In MediaLive, [create a multiplex](https://docs.aws.amazon.com/medialive/latest/ug/multiplex-create.html).

   MediaLive creates a MediaConnect entitlement that uses the multiplex as the source. The name of the entitlement includes `multiplex` and the name you chose for the multiplex.

1. In MediaConnect, [create a flow based on the new entitlement](entitlements-subscriber.md).

1. [Add outputs](outputs-add.md) to distribute the content.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
