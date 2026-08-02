---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/wave-based-refactoring/discovery-phase.html
---

# Phase 1: Discovery
<a name="discovery-phase"></a>

The discovery phase focuses on collecting essential information about your organization to help inform the refactoring approach. The following recommendations can help you identify key business value drivers as well as the IT system capabilities that deliver that value to customers.

**Key focus areas**
+ Identifying key business purposes, including domains, subdomains, and the IT system capabilities that each requires
+ Classifying IT system capabilities into categories based on their level of importance to the organization
+ Creating a capability matrix to track the information collected during the discovery phase, so that it can be referenced during the analysis phase

## Step 1: Identify key business purposes
<a name="identify-key-business-purposes"></a>

Talk to key stakeholders to gather information about how the business is organized. Categorize the organization's structure based on specific business functions, core competencies, and value-added services.

## Step 2: Define domains and subdomains
<a name="define-domains-and-subdomains"></a>

Identify key parts of the business (*domains*) and sub-areas within each business (*subdomains*). Make sure that you collaborate with key stakeholders to ensure that every domains is fully covered, without any gaps.

**Note**
Domains are usually associated with different business functions. For example, a financial services organization might have wealth management and online trading domains, while a retailer might have online shopping and product delivery domains. These organization-specific domains are then usually comprised of many subdomains.

## Step 3: List the existing IT system capabilities
<a name="list-the-existing-it-system-capabilities"></a>

Create a spreadsheet that lists each domain's and subdomain's IT system capabilities, and identify all of the relevant metadata as columns in the spreadsheet. This document will serve as the foundation of the capabilities matrix that's used throughout the remainder of this refactoring approach. Make sure that you include a column that explains the value that each capability provides to both internal and external customers.

For example, your organization's capabilities list could include some or all of the following metadata columns:
+ Capability description
+ Dependencies
+ Complexity
+ Integrations
+ Priority
+ Business value
+ Technical stack
+ Required APIs
+ Transactions and analytical reporting

## Step 4: Categorize the existing IT system's capabilities
<a name="categorize-the-existing-it-systems-capabilities"></a>

Organize the capabilities listed in the capabilities matrix into the following category types:
+ **Core business differentiators** distinguish your organization's main products and services from those of your competitors. These differentiators are sometimes also called *core competencies*.
+ **Utility capabilities** are needed to support the core business differentiators, but may not be unique to your organization. This type of capability can often be purchased as a software as a service (SaaS) product.
+ **Generic capabilities** support both the utility capabilities and core business differentiators, but aren't unique to your organization. These generic capabilities are often technical or related to business operations and can usually be purchased from a vendor. For example, generic capabilities could include cloud-based compute, storage, or document processing services, or logging and monitoring services.
