---
source_url: https://docs.aws.amazon.com/whitepapers/latest/applying-security-practices-to-network-workload-for-csps/welcome.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Applying Security Practices to a Network Workload on AWS for Communications Service Providers
<a name="welcome"></a>

Publication date: **June 30, 2023** ([Document revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 This whitepaper provides recommendations to Communication Service Providers (CSPs) on securing their telecommunications (telco) network workload on Amazon Web Services (AWS). These recommendations are based on the [Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) of the [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html), and focus on AWS infrastructure and services. The Security Pillar provides guidance to help customers apply best practices in the design, delivery, and maintenance of an AWS workload. The information in this whitepaper informs how customers can introduce security controls into their workloads. By implementing these recommendations, CSPs can improve the security of their telco workload on AWS and help achieve their security goals and requirements.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The seven pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

## Introduction
<a name="introduction"></a>

 Running telecommunications (telco) network workloads on the public cloud enables CSPs to use the benefits of cloud computing for cost savings, elasticity, pay-as-you-go pricing, and supporting a global footprint. In addition, the underlying infrastructure of the public cloud is independently certified against many international frameworks. This provides a proven secure foundation on which to host workloads, lowering the overall security burden compared to on-premises deployments where CSPs are typically responsible for the security of the entire stack.

 CSPs are looking for actionable guidance to design and manage the security of their workloads environments where they don't own the infrastructure. Another consideration for CSPs contemplating the public cloud is compliance. CSPs generate increasing amounts of data containing personally identifiable information (PII), or subscriber data subject to regional and global regulations. Regulations in telco have a strong focus on security and require CSPs to implement state-of-the-art security measures to run and operate telecommunications and data processing systems. This whitepaper discusses domain security, data protection, and data privacy to help protect the data of telco network workloads on AWS. It provides guidance on how to manage, govern, and operate network workloads in AWS by recommending design principles, architectural concepts, and security controls that helps CSPs align with regulatory and compliance requirements.
