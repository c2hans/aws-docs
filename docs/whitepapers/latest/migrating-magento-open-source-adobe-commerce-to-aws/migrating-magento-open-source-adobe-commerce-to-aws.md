---
source_url: https://docs.aws.amazon.com/whitepapers/latest/migrating-magento-open-source-adobe-commerce-to-aws/migrating-magento-open-source-adobe-commerce-to-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Migrating Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service to AWS
<a name="migrating-magento-open-source-adobe-commerce-to-aws"></a>

Publication date: **July 19, 2023** ([Document history](document-revisions.md))

 Adopting AWS for the Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service installation presents many benefits such as increased business agility, flexibility, and reduced costs. This whitepaper outlines the benefits of cloud hosting and considerations for migrating Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service installation to AWS. It also provides guidance for an organization that plans to AWS their cloud footprint. The content targets technical leaders and business leaders responsible for deploying and managing on-premises Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service or enterprise edition on AWS.

## Introduction
<a name="introduction"></a>

 Creating a new or migrating an existing on-premises Magento Open Source or Adobe Commerce on Cloud Infrastructure Self-Service setup to Amazon Web Services (AWS) cloud presents an opportunity to transform your organization by lowering costs, increasing agility, and delivering it reliably and globally. This whitepaper presents a cloud migration strategy and considerations when migrating Magento to AWS.

 This whitepaper provides general guidance for cloud migration with specific steps related to migrating Magento open-source installation to cloud and use of the AWS Terraform Quick Start to deploy Magento open-source edition on the AWS Cloud. In addition, the paper provides AWS reference architecture guidance to enable an organization that wants to install Magento enterprise edition on AWS. The first section of the whitepaper describes the reasons to migrate to the cloud and the common challenges that organizations face when migrating to the cloud. Next, the migration process and the migration strategies that organizations can choose from as well as deployment options are discussed. Lastly, the whitepaper concludes by discussing steps necessary to deploy the Quick Start along with security and compliance, architectural components, connectivity and a strategy you can adopt for migration.

 The TerraForm guide is for IT infrastructure architects, administrators, and DevOps professionals who are planning to implement or extend their Magento Open Source community editions workloads on the AWS Cloud using the [Terraform Quick Start on Amazon Web Services (AWS)](https://github.com/aws-ia/terraform-adobe-magento).

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
