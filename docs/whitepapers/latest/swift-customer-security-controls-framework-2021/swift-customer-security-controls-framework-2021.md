---
source_url: https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/swift-customer-security-controls-framework-2021.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# SWIFT Customer Security Controls Framework (v2022) on AWS
<a name="swift-customer-security-controls-framework-2021"></a>

Publication date: **July 21, 2021** ([Document Revisions](document-revisions.md))

## Abstract
<a name="abstract"></a>

 The [SWIFT Customer Security Programme](https://www.swift.com/myswift/customer-security-programme-csp) (CSP) was introduced to support SWIFT customers and drive industry-wide collaboration in the fight against cyber fraud. The CSP establishes a common set of security controls known as the Customer Security Controls Framework (CSCF) which is designed to help SWIFT users secure their local environments and to foster a more secure financial ecosystem.

 The SWIFT Customer Security Controls Framework (CSCF) consists of both mandatory and advisory security controls for SWIFT users. Mandatory security controls establish a security baseline for the entire community, and must be implemented by all users on their local SWIFT infrastructure. With the shift to cloud computing, Appendix G of the latest CSCF provides guidance for users using digital connectivity.

 The objective of this guide is to provide SWIFT customers with sufficient information and best practices to implement the CSCF security controls when implementing their [SWIFT Client Connectivity Stack on AWS](https://aws.amazon.com/quickstart/architecture/swift-client-connectivity/).

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## Introduction
<a name="introduction"></a>

 With the current business landscape created by the COVID-19 pandemic, the Society for Worldwide Interbank Financial Telecommunication (SWIFT) issued the v2021 guidance for its users to implement its updated Customer Security Programme (CSP) and Customer Security Controls Framework (CSCF).

 The latest CSP now requires a community-standard assessment for all users and all assessments submitted from 2021 onwards will require an independent assessment.

 This document provides guidance for SWIFT connectivity deployed on the AWS Cloud and is structured on the 7 Requirement sections described in the CSP.

 The latest v2022 guidance includes five changes from v2021. Three of the changes—Control 2.9, Control 6.2, and Control 6.3—are out of scope for Cloud Providers according to Appendix G of the CSP. A new advisory control(Control 1.5A) was added. It is nearly identical to Control 1.1 and the guidelines are the same. Finally, the scope of Control 1.2 has been extended to a new architecture type, but there are no changes to the AWS guidance.
