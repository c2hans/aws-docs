---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Ransomware Risk Management on AWS Using the NIST Cyber Security Framework (CSF)
<a name="ransomware-risk-management-on-aws-using-nist-csf"></a>

Publication date: **August 30, 2021** ([Document history](document-revisions.md))

 Today, many Chief Information Security Officers (CISOs) and cybersecurity practitioners are looking for effective security controls that will provide their organizations with the ability to identify, protect, detect, respond, and recover from ransomware events. The National Institute of Standards and Technology (NIST) has published practice guides and guidance to create a standards-based risk management framework to serve this need. This paper outlines the AWS services you can use to help you achieve the prescribed security controls.

 This document is intended for cybersecurity professionals, risk management officers, or other organization-wide decision makers considering the implementation of security controls to manage the risks associated with ransomware and other destructive events using the NIST cybersecurity framework in their organization. For details on how to configure the AWS services identified in this document and in the associated [customer workbook](https://d1.awsstatic.com/whitepapers/compliance/AWS_Services_and_Customer_Responsibility_Matrix_for_Alignment_to_the_CSF.904afea676185b9af4329bc3ed40cf2126c74118.xlsx) (file download), contact your [AWS Solutions Architect](https://aws.amazon.com/contact-us/).

## Introduction
<a name="introduction"></a>

 Organizations have the responsibility to protect the data they hold and safeguard their systems. This can be challenging, as technology changes in size and complexity, and as resources and workforces become more limited. Organizations must remain vigilant, as outside parties may attempt to gain unauthorized access to sensitive data through ransomware.

 Ransomware refers to a business model and a wide range of associated technologies that bad actors use to extort money. The bad actors use a range of tactics to gain unauthorized access to their victims’ data and systems, including exploiting unpatched vulnerabilities, taking advantage of weak or stolen credentials, and using social engineering. Access to the data and systems is restricted by the bad actors, and a ransom demand is made for the “safe return” of these digital assets.

 There are several methods such actors use to restrict or eliminate legitimate access to resources, including encryption and deletion, modified access controls, and network-based denial of service attacks. In some cases, even after data access is restored, bad actors have demanded a “second ransom,” promising that its payment guarantees the deletion of victims’ sensitive data, instead of selling it or publicly releasing it.

 Ransomware attacks are typically opportunistic in nature, targeting end users through emails, embedding malicious code within websites, or gaining access through unpatched systems. Ransomware can cost organizations a significant amount of resources in response and recovery, as well as impact their ability to operate.

 To help entities establish a holistic defense, the [National Institute of Standards and Technology](https://www.nist.gov/news-events/news/2021/06/ransomware-risk-management-preliminary-draft-nistir-8374-available-comment) (NIST) developed the Framework for Improving Critical Infrastructure Cybersecurity (NIST Cybersecurity Framework, or CSF). See [*NIST Cybersecurity Framework (CSF): Aligning to the NIST CSF in the AWS Cloud*](https://d1.awsstatic.com/whitepapers/compliance/NIST_Cybersecurity_Framework_CSF.pdf?did=wp_card&trk=wp_card) for additional information.

 NIST subsequently published additional draft guidance and practice guides for organizations specific to ransomware.

 NIST's National Cybersecurity Center of Excellence (NCCoE) has published Practice Guides to demonstrate how organizations can develop and implement security controls to combat the data integrity challenges posed by ransomware and other destructive events. These are described in:
+  NIST Special Publication (SP) 1800-11, [Data Integrity: Recovering from Ransomware and Other Destructive Events](https://csrc.nist.gov/publications/detail/sp/1800-11/final)
+  SP 1800-25, [Data Integrity: Identifying and Protecting Assets Against Ransomware and Other Destructive Events](https://csrc.nist.gov/publications/detail/sp/1800-25/final),
+  SP 1800-26, [Data Integrity: Detecting and Responding to Ransomware and Other Destructive Events](https://csrc.nist.gov/publications/detail/sp/1800-26/final)

 In addition, the draft NISTIR 8374, [Cybersecurity Framework Profile for Ransomware Risk Management](https://csrc.nist.gov/CSRC/media/Publications/nistir/draft/documents/NIST.IR.8374-preliminary-draft.pdf), provides guidance on how to defend against the threat, what to do in the event of an event, and how to recover from it. This framework can be used by organizations to improve their risk posture. It can also help organizations seeking to implement a risk management framework that deals with ransomware threats.

 This whitepaper outlines the security controls recommended by NIST related to ransomware risk management, and maps those technical capabilities to AWS services and implementation guidance. While this whitepaper is primarily focused on managing the risks associated with ransomware, the security controls and AWS services outlined are consistent with general security best practices.

## Are you Well-Architected?
<a name="are-you-well-architected"></a>

 The [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) helps you understand the pros and cons of the decisions you make when building systems in the cloud. The six pillars of the Framework allow you to learn architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems. Using the [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/), available at no charge in the [AWS Management Console](https://console.aws.amazon.com/wellarchitected), you can review your workloads against these best practices by answering a set of questions for each pillar.

 For more expert guidance and best practices for your cloud architecture—reference architecture deployments, diagrams, and whitepapers—refer to the [AWS Architecture Center](https://aws.amazon.com/architecture/).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
