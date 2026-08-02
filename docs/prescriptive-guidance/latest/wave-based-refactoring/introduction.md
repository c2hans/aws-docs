---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/wave-based-refactoring/introduction.html
---

# Modernize applications by using a wave-based refactoring approach
<a name="introduction"></a>

*Ramanna Avancha, Amazon Web Services*

This guide provides a framework for modernizing legacy, on-premises applications and databases to a cloud-native architecture by using a wave-based refactoring approach.

Organizations that take on legacy application or database cloud migration projects must first understand their system's pain points, processes, workflows, capabilities, and dependencies. This guide shows how you can use a phased approach to answering these key questions. Then, leverage AWS microservices and serverless architectures to incrementally roll out changes to production in waves.

There are three phases to developing a wave-based modernization model that are covered in this guide:
+ Phase 1: Discovery
+ Phase 2: Analysis
+ Phase 3: Wave-based implementation

## Overview
<a name="summary"></a>

The following diagram shows a waved-based implementation framework for modernizing legacy, on-premises applications and databases to a cloud-native architecture.

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/wave-based-refactoring/images/guide-img/ff06808b-a33a-4b93-bb44-da440c04ac7a/images/bc1155b8-6f99-4dca-a343-a1e538b8863b.png)

The diagram shows the following workflow:

1. The discovery phase focuses on collecting essential information about your organization, including its key value drivers and how its IT system's capabilities are classified. This information is used to help inform the specific refactoring approach that your organization will implement.

1. The analysis phase focuses on organizing the information that's gathered during the discovery phase. By analyzing your IT system's dependencies and business processes, you can then decompose the IT solution into independent domains and services.

1. The wave-based implementation phase focuses on selecting AWS microservices to replace specific functionalities of the legacy system, and then implementing those services in waves. The microservice selection process uses a series of prioritization criteria that categorize capabilities based on their business priority, number of dependencies, and level of complexity.

**Note**
The AWS services shown in the diagram are for example purposes only. There are many other AWS services that can be used for each implementation phase.

## Targeted business outcomes
<a name="targeted-business-outcomes"></a>

This guide helps you do the following:
+ Apply a consistent approach when decomposing the capabilities of legacy IT systems and analyzing your organization's cloud modernization requirements.
+ Identify AWS services to become the foundation of your organization's modernized, cloud-native applications.
