---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-operational-resilience/aws-operational-resilience.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Web Services' Approach to Operational Resilience in the Financial Sector & Beyond
<a name="aws-operational-resilience"></a>

Publication date: *March 2019*

**Updated April 2, 2021** ([Document history](document-revisions.md))

 The purpose of this paper is to describe how Amazon Web Services (AWS) and our customers in the financial services industry achieve operational resilience using AWS services. The primary audience of this paper is organizations with an interest in how AWS and our financial services customers can operate services in the face of constant change, ranging from minor weather events to cyber issues.

## Introduction
<a name="introduction"></a>

 AWS provides information technology (IT) services and building blocks that all types of businesses, public authorities, universities, and individuals utilize to become more secure, innovative, and responsive to their own needs and the needs of their customers. AWS offers IT services in categories ranging from compute, storage, database, and networking to artificial intelligence and machine learning. AWS standardizes its services and makes them available to all customers, including financial institutions. Across the world, financial institutions have used AWS services to build their own applications for mobile banking, regulatory reporting and market analysis.

 AWS and the financial services industry share a common interest in maintaining operational resilience; for example, the ability to provide continuous service despite disruption. Continuity of service, especially for critical economic functions, is a key prerequisite for financial stability. AWS recognizes that financial institutions, which use AWS services, need to comply with sector-specific regulatory obligations and internal requirements regarding operational resilience.

 These obligations and requirements are found, inter alia, in IT guidelines (U.S. Federal Financial Institution Examination Council (FFIEC) IT Handbook; see [https://ithandbook.ffiec.gov](https://ithandbook.ffiec.gov/)) and cyber resilience guidance (Committee on Payments and Market Infrastructures and Board of the International Organization of Securities Commissions (CPMI-IOSCO), Guidance on cyber resilience for financial market infrastructures (June 2016); see [https://www.bis.org/cpmi/publ/ d146.pdf](https://www.bis.org/cpmi/publ/d146.pdf))

Financial institution customers are able to rely on AWS to provide resilient infrastructure and services, while at the same time designing their applications in a manner that meets regulatory and compliance obligations. This dual approach to operational resilience is something that we call *shared responsibility*.

### What does operational resilience mean at AWS?
<a name="what-does-operational-resilience-mean-at-aws"></a>

 Operational resilience is the ability to provide continuous service through people, processes, and technology that are aware of and adaptive to constant change. It is a real-time, execution- oriented norm embedded in the culture of AWS that is distinct from traditional approaches in Business Continuity, Disaster Recovery, and Crisis Management, which rely primarily on centralized, hierarchical programs focused on documentation development and maintenance.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
