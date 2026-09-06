---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/build-e2e-data-driven-applications.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Architectural Patterns to Build End-to-End Data Driven Applications on AWS
<a name="build-e2e-data-driven-applications"></a>

Publication date: **August 3, 2022** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 [According to Forbes](https://www.forbes.com/sites/forbestechcouncil/2020/12/03/data-is-essential-to-digital-transformation/?sh=164bd28126c9), 85% of businesses want to be data driven, but only 37% have been successful. Most of the organizations that try to use data to modernize and innovate struggle with finding the proven architectural patterns that customers have implemented to build data-driven applications. Successful customers use multiple Amazon Web Services (AWS) services between event-driven Internet of Things (IoT) to collect and manage billions of devices and purpose-built databases. This allows them to save costs, grow and innovate faster, and use data analytics to get the fastest insights on all their data and artificial intelligence/machine learning (AI/ML) to help them innovate for the future.

 In this whitepaper, we present some commonly used data-driven applications and proven architectural patterns based on successful customer implementation. This enables customers who are looking to build those data driven applications to accelerate time to solution.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 In the [Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/analytics-lens.html), we describe a collection of customer-proven best practices for designing well-architected analytics workloads.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 There are more than 200 services provided by AWS. Customers can use this diverse set of choices to select the correct tool for the right job, but sometimes it can be confusing to map to different use cases. There are some services with overlapping capabilities, and customers often struggle to find a proven pattern when they’re developing their data-driven applications. Some customers take the approach of doing multiple proof of concepts (POCs), which is time consuming, and might still fail to instill confidence in whether a set of services is a proven pattern based on other AWS customer implementations.

 This whitepaper brings together the most commonly used data-driven applications and architectural patterns that other AWS customers have proven to be successful in their implementations. These architecture reference patterns provide guidance to quickly select a proven architectural pattern and further modify it to meet your application needs. In some cases, these architecture patterns can be used without modification, thereby minimizing the need to POC extensively, and accelerate time to solution.

 The architecture reference patterns covered in this whitepaper also provide thought leadership for you to create a future state strategy to modernize your data-driven applications. It helps you look through the lens of how various AWS data services, such as AWS IOT for event-driven IOT data collection, manage billions of devices and purpose-built databases to save costs, modernize databases for the cloud, and innovate faster. Use analytics to get fastest insights on all your data, from big data processing, data warehousing to visualization, and AI/ML, to build and operationalize ML and AI applications to innovate for the future.
