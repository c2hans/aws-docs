---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/multi-tenancy-amazon-neptune/introduction.html
---

# Multi-tenancy guidance for ISVs running Amazon Neptune databases
<a name="introduction"></a>

*Brian O'Keefe, Veeresham Gande, Dana Owens, and Nima Seifi, Amazon Web Services*

Multi-tenancy is a computer systems architecture where a single instance of an application serves multiple customers. Each customer is referred to as a *tenant*. In a multi-tenant architecture, these instances of the application operate in a shared environment where each tenant is physically co-located on the same infrastructure but is logically separated.

As an independent software vendor (ISV), you can use Amazon Neptune to power applications that require navigation across highly connected data. You might be managing a cloud-based software as a service (SaaS) application in your account and providing tenants with subscriptions. Tenants can then access the service over the internet or privately over AWS PrivateLink. The economics of this model work for both parties, because the tenant gets access to software that's less expensive than it would be for them to purchase, build, and maintain. As the ISV, you can charge more for the subscription than it costs you to create and maintain the software. The question is how do you scale your business to multiple tenants.

Multi-tenancy provides ISVs with important economical and operational benefits. The multi-tenant architecture gives your organization a better return on investment (ROI). Multi-tenancy also simplifies operational requirements so that your organization can move more quickly and reduce the cost of delivering the software to your tenants.

This document provides guidance on effectively running a multi-tenant ISV application using Amazon Neptune. This guidance is based on best practices gained over years of supporting ISVs' successful delivery of SaaS solutions to their customers. Evaluating this guidance in the context of your organization's goals and architectural principles will help you find ways to optimize your solution.

**Note**
This document does not provide an exhaustive list of best practices. It supplements the document [Applying the AWS Well-Architected Framework for Amazon Neptune](https://docs.aws.amazon.com/prescriptive-guidance/latest/neptune-well-architected-framework/introduction.html) by providing additional specific guidance for multi-tenancy ISV workloads. We recommend reviewing the considerations in both documents when designing your solution.
