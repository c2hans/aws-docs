---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/integrate-third-party-services/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to frequently asked questions about integrating third-party services in the AWS Cloud.

## Is there a preferred architecture?
<a name="faq-preferred-architecture"></a>

No, you should select an architecture according to your integration requirements.

## How do I integrate with a third-party service that exists outside the AWS Cloud?
<a name="faq-outside-aws"></a>

In this case, the architectures in this guide are not applicable. You must establish connectivity using different mechanisms, for example, using AWS Site-to-Site VPN.

## Can I combine architectures together?
<a name="faq-combine-architectures"></a>

Yes, you can. For example, you could use an AWS Transit Gateway peering architecture for the majority of your VPCs and use VPC peering for specific VPCs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
