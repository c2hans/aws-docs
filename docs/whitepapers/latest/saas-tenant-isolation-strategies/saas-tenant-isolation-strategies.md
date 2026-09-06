---
source_url: https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SaaS Tenant Isolation Strategies: Isolating Resources in a Multi-Tenant Environment
<a name="saas-tenant-isolation-strategies"></a>

Publication date: **August 1, 2020** ([Document history](document-revisions.md))

 Tenant isolation is fundamental to the design and development of software as a service (SaaS) systems. It enables SaaS providers to reassure customers that—even in a multitenant environment—their resources cannot be accessed by other tenants. This paper will look at the full range of strategies that are commonly used by SaaS companies to ensure that their systems are successfully isolating tenant resources while still realizing the value proposition of the SaaS delivery model.

## Introduction
<a name="introduction"></a>

 Tenant isolation is one of the foundational topics that every software as a service (SaaS) provider must address. As independent software vendors (ISVs) make the shift toward SaaS and adopt a shared infrastructure model to achieve cost and operational efficiency, they also have to take on the challenge of determining how their multi-tenant environments will ensure that tenants are prevented from accessing another tenant’s resources. Crossing this boundary in any form would represent a significant and potentially un-recoverable event for a SaaS business.

 While the need for tenant isolation is viewed as essential to SaaS providers, the strategies and approaches to achieving this isolation are not universal. There are a wide range of factors that can influence how tenant isolation is realized in any SaaS environment. The domain, compliance, deployment model, and the selection of AWS services all bring their own unique set of considerations to the tenant isolation story.

 In this whitepaper, we’ll outline many of the common patterns and strategies that are used to implement tenant isolation on AWS. The goal here is to capture some of the common themes and challenges that span the various SaaS architecture models and AWS technologies, while highlighting the various approaches to achieving tenant isolation in each of these environments. This paper should equip you with a collection of insights that will help you select the combination of isolation strategies that best align with the realities of your environment and business model.
