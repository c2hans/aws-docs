---
source_url: https://docs.aws.amazon.com/whitepapers/latest/patterns-for-ingesting-saas-data-into-aws-data-lakes/patterns-for-ingesting-saas-data-into-aws-data-lakes.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Patterns for Ingesting SaaS Data into AWS Data Lakes
<a name="patterns-for-ingesting-saas-data-into-aws-data-lakes"></a>

Publication date: **March 4, 2022** ([Document Revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 Today, many organizations generate and store data in [Software as a service](https://en.wikipedia.org/wiki/Software_as_a_service) (SaaS)-based applications. They want to ingest this data in a central repository (often a data lake) so that they can analyze it though a single pane of glass and derive insights from it. However, because different SaaS applications provide different mechanisms of extracting the data, a single approach does not always work.

 This paper outlines different patterns using Amazon Web Services (AWS) services to ingest SaaS data into a data lake on AWS.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems on AWS. Using the Framework allows you to learn architectural best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud.

 In the [SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html), we enable customers to review and improve their cloud-based architectures and better understand the business impact of their design decisions. We address general design principles as well as specific best practices and guidance in five conceptual areas that we define as the pillars of the Well-Architected Framework.

## Introduction
<a name="introduction"></a>

 With the growing ecosystem of SaaS-based applications, many organizations face the challenge of collecting all this data into a centralized location for analytics. Often this centralized location is a data lake, and in AWS Cloud, [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) becomes the centralized storage for this data lake. However, an ingestion mechanism must be in place get all the SaaS data into Amazon S3. This paper explores different options to use in AWS, along with usage patterns and considerations to make when selecting a particular ingestion mechanism.
