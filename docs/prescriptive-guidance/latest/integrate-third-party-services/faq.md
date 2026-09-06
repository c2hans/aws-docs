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
