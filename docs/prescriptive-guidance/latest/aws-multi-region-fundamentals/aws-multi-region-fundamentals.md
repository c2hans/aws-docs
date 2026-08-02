---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-multi-region-fundamentals/aws-multi-region-fundamentals.html
---

# AWS multi-Region fundamentals
<a name="aws-multi-region-fundamentals"></a>

*John Formento, Amazon Web Services*

This advanced, 300-level guide is intended for cloud architects and senior leaders who build workloads on AWS and are interested in using a multi-Region architecture to improve resilience for their workloads. This guide assumes baseline knowledge of AWS infrastructure and services. It outlines common multi-Region use cases, shares fundamental multi-Region concepts and implications around design, development, and deployment, and provides prescriptive guidance to help you better determine whether a multi-Region architecture is right for your workloads.

## Are you Well-Architected?
<a name="waf"></a>

The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when you build systems in the cloud. The six pillars of the Framework provide architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. You can use the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), which is available at no charge on the [AWS Management Console](https://console.aws.amazon.com/wellarchitected/), to review your workloads against these best practices by answering a set of questions for each pillar.

For additional expert guidance and best practices for your cloud architecture, including reference architecture deployments, diagrams, and technical guides, see the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

Each [AWS Region](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html) consists of multiple independent and physically separate Availability Zones within a geographic area. Strict logical separation between the software services in each Region is maintained. This purposeful design ensures that an infrastructure or service failure in one Region doesn't result in a correlated failure in another Region.

Most AWS users can achieve their resilience objectives for a workload in a single Region by using multiple Availability Zones or Regional AWS services. However, a subset of users pursue multi-Region architectures for three reasons:
+ They have high availability and continuity of operations requirements for their highest tier workloads and want to establish a bounded recovery time from impairments that impact resources in a single Region.
+ They need to satisfy [data sovereignty](https://purdue.edu/critical-data-studies/collaborative-glossary/data-sovereignty.php) requirements (such as adherence to local laws, regulations, and compliance) that require workloads to operate within a certain jurisdiction.
+ They need to improve performance and customer experience for the workload by running the workloads in locations that are closest to their end users.

This guide focuses on high availability and continuity of operations requirements, and helps you navigate the considerations for adopting a multi-Region architecture for a workload. It describes fundamental concepts that apply to design, development, and deployment of a multi-Region workload, and provides a prescriptive framework to help you determine whether a multi-Region architecture is the right choice for a particular workload. You need to ensure that a multi-Region architecture is the right choice for your workload because these architectures are challenging, and if the multi-Region architecture isn't built correctly, it's possible for the overall availability of the workload to decrease.
