---
source_url: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-of-on-premises-applications-to-aws/abstract-and-introduction.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Disaster Recovery of On-Premises Applications to AWS
<a name="abstract-and-introduction"></a>

Publication date: **January 19, 2022** ([Document history](document-history.md))

## Abstract
<a name="abstract"></a>

This whitepaper outlines the best practices for planning, implementing, and maintaining disaster recovery for on-premises applications using AWS. It lays out the differences between disaster recovery and other resilience strategies, and describes the steps of building a disaster recovery plan. It also offers different approaches for mitigating risks and meeting recovery time objectives (RTO), and meeting recovery point objectives (RPO) by using AWS as the disaster recovery site. This whitepaper covers how to use AWS as a disaster recovery site for on-premises applications.

Refer to [Disaster Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) for information about disaster recovery for AWS-hosted workloads.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

### What is disaster recovery?
<a name="what-is-disaster-recovery"></a>

 Disaster recovery is the process of preparing for and recovering from a disruptive event.

### What is a disaster?
<a name="what-is-a-disaster"></a>

 In the context of a company’s IT environment, a disaster is an event that partially or completely disrupts the operations of one or more applications. A disaster normally requires human intervention to *fail over* to secondary copies of applications in order to maintain their functionality.

 The four main categories of a disaster:
+  **Human errors** – Unintentional actions leading to a security breach such as inadvertent misconfiguration of the software or a database
+  **Malicious attacks** – Unauthorized actions that affect a victim’s system such as a denial-of-service (DoS) or ransomware attack
+  **Natural disasters** – Environmental factors that cause a system failure such as earthquakes or floods
+  **Technical failures** – A malfunction of software, hardware, or a facility such as a power failure or a network connectivity failure

 There are several factors to consider when planning your response to a specific disaster:
+  **Expected duration of the disaster** – How soon will the application recover and how likely is the disaster to resolve on its own?
+  **Size of impact (also known as blast radius)** – Which applications are affected and to what extent is their functionality impaired?
+  **Geographic impact** – May be regional, national, continental, or global.
+  **Tolerance of downtime** – How significant is the impact of the application not functioning?

### Why disaster recovery?
<a name="why-disaster-recovery"></a>

 A properly planned and implemented disaster recovery solution helps mitigate the following issues that can be caused by a disaster:
+  **Direct and indirect financial loss** – The impact of direct financial loss is mostly relevant for applications that are critical for any revenue-generating processes. For example, external-facing IT systems that are provided to customers for a fee or internal IT systems that process data relevant for revenue generation. Indirect financial loss includes, for example, customers switching to a competing product and the cost of work needed to resume normal operation after the disaster is over.
+  **Reputational damage** – In addition to financial loss, downtime caused by unexpected incidents can significantly harm a company’s reputation. A short recovery period aided by a disaster recovery solution can help avoid irreversible damage to the corporate image.
+  **Failure to abide by compliance standards** – Multiple compliance standards, including System and Organization Controls (SOC), the Payment Card Industry (PCI) Data Security Standard, and the Health Insurance Portability and Accountability Act (HIPAA), require a disaster recovery plan. Some standards even add very specific requirements, such as minimal physical distance between the source site and the disaster recovery site.
