---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/welcome.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Genomics Data Transfer, Analytics, and Machine Learning using AWS Services
<a name="welcome"></a>

**Publication date: November 23, 2020 ([Document Revisions](document-revisions.md))**

## Abstract
<a name="abstract"></a>

Precision medicine is “an emerging approach for disease treatment and prevention that takes into account individual variability in genes, environment, and lifestyle for each person,” according to the Precision Medicine Initiative. This approach allows doctors and researchers to identify and tailor treatments for groups of patients to improve patient outcomes. Precision medicine is powered by studying genomics data from hundreds of thousands of people refining the understanding of normal and disease diversity. The challenge is to turn the genomics data from many large-scale efforts like biobanks, research studies, and biopharma, into useful insights and patient-centric treatments in a rapid, reproducible, and cost-effective manner. The key to enabling scientific discovery is to combine different data streams, ensure global accessibility and availability, and allow high-performance data processing while keeping this sensitive data secure. “The responsible and secure sharing of genomic and health data is key to accelerating research and improving human health,” is a stated objective for the Global Alliance for Genomics and Health (GA4GH). This approach requires technical knowledge and ever-growing compute and storage resources. One of the ways that AWS is enabling this objective is to host many genomics datasets in the [Registry of Open Data on AWS](https://registry.opendata.aws/).

Raw genomics data is typically processed through a series of steps as part of a pipeline to transform into a form that is ready for analysis. Each step of the secondary analysis workflow could have different compute and memory requirements; some of the steps could be as simple as adding a set of annotations, or as computationally intensive as aligning raw reads to a reference genome. The requirements at this stage are to process the data in a cost effective, scalable, efficient, consistent, and reproducible manner across large datasets.

Once the data is processed, the next step is to query and mine genomic data for useful insights including discovering new biomarkers or drug targets. At this tertiary analysis stage, the goal is to prepare these large datasets so they can be queried easily and in an interactive manner to answer relevant scientific questions, or to use them to build complex machine learning models that can be utilized to analyze population or disease-specific datasets. The aim is accelerating the impact of genomics in the multi-scale and multi-modal data of precision medicine.

The genomics market is highly competitive, so having a development lifecycle that allows for fast adoption of new methods and technologies is critical. This paper answers some of the critical questions that many organizations that work with genomics data have, by showing how to build a next-generation sequencing (NGS) platform from instrument to interpretation using AWS services. We provide recommendations and reference architectures for developing the platform including: 1) transferring genomics data to the AWS Cloud and establishing data access patterns, 2) running secondary analysis workflows, 3) performing tertiary analysis with data lakes, and 4) performing tertiary analysis using machine learning. Solutions for three of the reference architectures in this paper are provided in AWS Solutions Implementations. These solutions leverage continuous delivery (CD), allowing you to develop the solution to fit your organizational need.

## Are you Well-Architected?
<a name="wa"></a>

The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/?actwpp_AWSGDFWAF_HTML) helps you understand the pros and cons of the decisions you make when building systems on AWS. Using the Framework allows you to learn architectural best practices for designing and operating reliable, secure, efficient, and cost-effective systems in the cloud.

In the [Machine Learning Lens](https://aws.amazon.com/architecture/machine-learning/?actwpp_AWSGDFML_HTML), we focus on how to design, deploy, and architect your machine learning workloads in the AWS Cloud. This lens adds to the best practices described in the Well-Architected Framework.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
