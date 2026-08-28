---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-architectures-to-address-personal-data-processing-requirements/hybrid-architectures-to-address-personal-data-processing-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Hybrid Architectures to Address Personal Data Processing Requirements
<a name="hybrid-architectures-to-address-personal-data-processing-requirements"></a>

Publication date: **August 2, 2023** ([Document history](document-revisions.md))

 This document was created to assist customers that have presence or business in countries which have no AWS infrastructure ([AWS Region](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html)) to develop hybrid cloud architectures by using the reference architecture diagrams provided in this whitepaper. These architectures can be used as building blocks in cases where customers decide to use AWS as a hybrid platform. The architectures can work independently, or integrate with other solutions and AWS services using existing data flow or API.

## Introduction
<a name="introduction"></a>

 Personal data processing requirements, applied in most countries around the globe, set up rules related to the processing of data involving an identified or identifiable natural (living) person. Most requirements set up data collection, hosting, transfer, or processing rules, bounded by country borders. If a cloud provider has no local infrastructure in a given country, this means it blocks customer workloads and personal data processing requirements from using cloud infrastructure. A possible solution is using *hybrid architecture*, which addresses the requirements using country-based infrastructure to host sensitive data, and uses cloud infrastructure for other workloads.

 This document can be used by customers in most [Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) to address personal data processing requirements. Some Regions, such as CEE, Africa, and Asia, have similar requirements to what is considered in the document. Requirements for some Regions would necessitate a re-design of the proposed architectures. It is the customer’s responsibility to address any data protection requirements for their country or Region.

**Note**
 AWS Outposts is not available in some countries as of March 2023.

 **Disclaimer:** In this document, AWS provides patterns, or concepts, of architectures. These patterns don’t address all possible requirements and should be considered as examples. You may need to redesign these architectures, or combine them with other components to address your use cases. AWS does not provide legal advice, and this document is not to be understood as legal advice or assurance. Compliance involving these architecture implementations is the responsibility of the customer.

 You can use AWS services with the confidence that your customer data stays in the AWS Region you select. A small number of AWS services involve the transfer of customer data; for example, to develop and improve those services, where you can [opt-out of the transfer](https://aws.amazon.com/compliance/privacy-features/#AWS_services_that_allow_customers_to_opt-out_of_transfers_of_customer_data), or because [transfer is an essential part of the service](https://aws.amazon.com/compliance/privacy-features/#AWS_services_that_transfer_customer_data_as_an_essential_function_of_the_service).

**Note**
Customers who do not have sensitive data that is subject to regulation can use the AWS Cloud *without* relying on local resource and building hybrid architectures.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The Six Pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
