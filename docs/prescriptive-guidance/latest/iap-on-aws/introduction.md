---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/iap-on-aws/introduction.html
---

# Implementing IaP on AWS
<a name="introduction"></a>

*Kirsten Kissmeyer, Amazon Web Services*

This guide explores approaches for managing your AWS infrastructure as a product (IaP). IaP provides a higher level of abstraction and control than infrastructure as code (IaC) but uses IaC methods to achieve its goals. The guide also explores AWS services and tools for managing IaP and highlights how each tool can support your objectives for managing your infrastructure. The information in this guide is based on learnings from an AWS Service Catalog enablement initiative for a very large financial sector company.

This guide is intended for users who want to develop functional AWS Cloud infrastructure services that can easily be allocated and authorized as needed for different organizational users, business units, and third parties.

## Why manage infrastructure as products?
<a name="why-manage-infrastructure-as-products"></a>

The advantage of managing your infrastructure resources as products is that you can package consumer capabilities as a set of resources that have standardized definitions and configurations. Products provide a convenient way for an organization to manage and control how AWS capabilities are allocated and consumed. A product might be restricted to only designated [organizational units (OUs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html) or to individuals who need those functional capabilities. A product can be restricted to specific AWS Regions as well.

A product provisioning model also lets you encapsulate and update the definition of a product from a central location. You can then distribute product updates on a one-time or scheduled basis, as its implementation changes over time.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

Organizations always look for better ways to manage and provision their AWS infrastructure. Your objectives might include:
+ Achieving a high degree of agility, reliability, fault tolerance, and centralized control, where single points of configuration satisfy compliance with evolving internal and external standards.
+ A low-touch or push-button mechanism to distribute infrastructure in a centralized way, while allowing self-serve access when needed for specific teams or individuals.
+ The ability to provision AWS infrastructure and services to internal staff, client accounts, and partner OU accounts. You might also want to control which OUs or organizations have access to specific infrastructure components in specific Regions.
+ If you use third-party tools (such as ServiceNow) or custom tools to manage requests to access and provision your enterprise assets and infrastructure, easy integration between your AWS infrastructure and these tools.
+ The ability to provision AWS infrastructure to dozens or even hundreds of target accounts at the same time.
+ Support for provisioning multiple AWS resources to provide a single capability.
+ The ability to create new accounts with required infrastructure within a tight schedule.
+ Access to an inventory of the infrastructure that you have provisioned, and the ability to update or remove infrastructure components.
+ Approaches and technologies that make the provisioning and maintenance process easier, faster, and more secure and reliable.
