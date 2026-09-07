---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/tagging-best-practices/introduction.html
---

# Using best practices when tagging for monitoring, reporting, and cost optimization
<a name="introduction"></a>

*Apoorva Patrikar, Amazon Web Services*

Tagging refers to the process of assigning metadata in the form of key-value pairs to the resources deployed on Amazon Web Services (AWS). Tagging is important for managing and identifying resources, monitoring, and housekeeping. The additional context that tags provide on files, code, and infrastructure can help you build dashboards for monitoring and process optimization.

This guide discusses the best practices and ontology for tagging all components of an application. The example focuses on data pipelines. However, you can extend same concept to any domain or application.

## Overview
<a name="overview"></a>

Tags are data about data files or resources. They provide additional business or technical information. For example, tags for data can provide information such as who the data belongs to, domain, department, and type. Tags for resources provide information about the process overall. For example, tags can provide the following:
+ Project name
+ Run type
+ Environment, such as dev, int, or prod
+ Data layer of operation, such as raw, trusted, or refined

Tags are key-value pairs that you can use to report current status or to understand the costs, performance, and success rates at every level of granularity. Tags can be categorized by different attributes, including the following:
+ Purpose
+ Owner
+ Environment
+ Project
+ Phase

The following image shows object tags implemented on Amazon Simple Storage Service (Amazon S3).

![Key-value pairs for tags shown on the console.](https://docs.aws.amazon.com/prescriptive-guidance/latest/tagging-best-practices/images/guide-img/fc2e4154-d614-4be6-b18a-2e052f9b7d57/images/0af01b87-1cbc-42b0-8cca-6c80f1bfb340.jpeg)

This guide covers how tagging can help you understand the metrics of an application after tags are applied to all the components, including the following:
+ Input files
+ Databases
+ Processing jobs
+ Output files

## Prerequisites
<a name="prerequisites"></a>

When you implement tagging, consider the following requirements:
+ When using tags for reporting purposes, you must activate the tags. For more information and instructions, see the [AWS Billing documentation](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/activating-tags.html). When using tags for other purposes, such as cleanup, automation, or retrieving a full list of services that belong to a certain category, it can be sufficient to assign tags to all the involved components.
+ Before you specify recommended or mandated tags, review the [AWS documentation](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) for information about the limitations and requirements.
