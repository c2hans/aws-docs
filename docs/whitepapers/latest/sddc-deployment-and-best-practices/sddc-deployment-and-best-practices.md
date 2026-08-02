---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sddc-deployment-and-best-practices/sddc-deployment-and-best-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SDDC Deployment and Best Practices Guide on AWS
<a name="sddc-deployment-and-best-practices"></a>

Publication date: **May 20, 2021** ([Document revisions](document-revisions.md))

 This guide is intended for IT infrastructure architects, administrators, and IT professionals who are planning to implement a VMware Cloud Software Defined Data Center (SDDC). It contains the steps and considerations required to stand up an SDDC as well as leveraging best practices and recommendations.

 The information is written for readers who have used [vSphere](https://www.vmware.com/products/vsphere.html) in an on-premises environment and are familiar with virtualization concepts.

 A moderate knowledge of Amazon Web Services (AWS) is useful, but is not required.

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

 To prepare for deployment, you should understand design decisions and gather necessary information. This deployment guide provides planning considerations and step-by-step instructions.

 This guide covers the following planning considerations:
+  Architecture
+  Personnel
+  Account requirements
+  AWS infrastructure
+  Network planning

 Additionally, the guide provides you with step-by-step instructions to activate VMware Cloud on AWS and create your first SDDC.

## Introduction
<a name="introduction"></a>

To prepare for deployment, you should understand design decisions and gather necessary information. This deployment guide provides planning considerations and step-by-step instructions.

This guide covers the following planning considerations:
+ Architecture
+ Personnel
+ Account requirements
+ AWS infrastructure
+ Network planning

Additionally, the guide provides you with step-by-step instructions to activate VMware Cloud on AWS and create your first SDDC.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).
