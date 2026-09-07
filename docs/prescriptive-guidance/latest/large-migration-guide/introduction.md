---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/introduction.html
---

# Guide for AWS large migrations
<a name="introduction"></a>

*Wally Lu, Tuhin Mukherjee, Damien Renner, and Senay Swinney, Amazon Web Services*

**Note**
Before reading this guide, we recommend reading [Strategy and best practices for AWS large migrations](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.html). The strategy discusses best practices for large migrations and provides use cases from customers across various industries. This guide describes a high-level, phased approach for implementing those best practices.

This guide provides an overview of the phased approach for large migrations, which consists of three phases: assess, mobilize, and migrate and modernize. The primary purpose of this guide is to describe the migrate part of the third phase, migrate and modernize, and its two stages, initialize and implement:
+ In stage 1, *initialize*, you prepare your platform and people for a large migration. You also define the standard operating procedures (or *runbooks*) for the large migration. The runbooks and automations simplify and accelerate implementation of the large migration in stage 2.
+ In stage 2, *implement*, you migrate servers at scale and closely manage and monitor the progress to implement continuous improvements.

## Guidance for large migrations
<a name="guidance-large-migrations"></a>

Migrating 300 or more servers is considered a large migration. The people, process, and technology challenges of a large migration project are typically new to most enterprises. This document is part of an AWS Prescriptive Guidance series about large migrations to the AWS Cloud. This series is designed to help you apply the correct strategy and best practices from the outset, to streamline your journey to the cloud.

The following figure shows the other documents in this series. Review the strategy first, then the guides, and then proceed to the playbooks. To access the complete series, see [Large migrations to the AWS Cloud](https://aws.amazon.com/prescriptive-guidance/large-migrations/).

![The structure of the AWS large migration document series](https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/images/guide-img/a7434c46-8e52-4896-84b2-cc91433b5072/images/957191af-912b-4dd6-be03-c10b4930de5b.png)

## About the tools
<a name="abouttools"></a>

A *health-check matrix* is attached to this guide. You can use this tool to assess the health of your migration project throughout the migration. This tool helps you apply best practices and evaluate the efficiency and progress of your large migration project throughout its life cycle.

Additionally, each of the playbooks in this documentation series include templates and tools that can help you build each workstream.

## Attachments
<a name="attachments-a7434c46-8e52-4896-84b2-cc91433b5072"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
