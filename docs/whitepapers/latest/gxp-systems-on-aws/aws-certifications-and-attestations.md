---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/aws-certifications-and-attestations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# AWS Certifications and Attestations
<a name="aws-certifications-and-attestations"></a>

 The AWS global infrastructure is designed and managed according to security best practices as well as a variety of security compliance standards. With AWS, you can be assured that you are building web architectures on top of some of the most secure computing infrastructure in the world. The IT infrastructure that AWS provides to you is designed and managed in alignment with security best practices and a variety of IT security standards including the following that life science customers may find most relevant:
+  [SOC 1, 2, 3](https://aws.amazon.com/compliance/soc-faqs/)
+  ISO [9001](https://aws.amazon.com/compliance/iso-9001-faqs/) / ISO [27001](https://aws.amazon.com/compliance/iso-27001-faqs/) / ISO [27017](https://aws.amazon.com/compliance/iso-27017-faqs/) / ISO [27018](https://aws.amazon.com/compliance/iso-27018-faqs/)
+  [HITRUST](https://aws.amazon.com/compliance/hitrust/)
+  [FedRAMP](https://aws.amazon.com/compliance/fedramp/)
+  [CSA Security, Trust & Assurance Registry (STAR)](https://aws.amazon.com/compliance/csa/)

 There are no specific certifications for GxP compliance for cloud services to date, however the controls and guidance described by this whitepaper, in conjunction with additional resources supplied by AWS provide information on AWS service GxP-compatibility, which will assist you in designing and building your own GxP-compliant solutions.

 AWS provides on-demand access to security and compliance reports and select online agreements through [AWS Artifact](https://aws.amazon.com/artifact/), with reports accessible via AWS customer accounts under NDA. AWS Artifact is a go-to central resource for compliance related information and is a place that you can go to find additional information on the AWS compliance programs described further below.

## SOC 1, 2, 3
<a name="soc-1-2-3"></a>

 AWS System and Organization Controls (SOC) Reports are independent third-party examination reports that demonstrate how AWS achieves key compliance controls and objectives. The purpose of these reports is to help you and your auditors understand the AWS controls established to support operations and compliance.

 The SOC 1 reports are designed to focus on controls at a service organization that are likely to be relevant to an audit of a user entity’s financial statements. The AWS SOC 1 report is designed to cover specific key controls likely to be required during a financial audit, as well as covering a broad range of IT general controls to accommodate a wide range of usage and audit scenarios. The AWS SOC1 control objectives include security organization, employee user access, logical security, secure data handling, physical security and environmental protection, change management, data integrity, availability and redundancy and incident handling.

 The SOC 2 report is an attestation report that expands the evaluation of controls to the criteria set forth by the American Institute of Certified Public Accountants (AICPA) Trust Services Principles. These principles define leading practice controls relevant to security, availability, processing integrity, confidentiality, and privacy applicable to service organizations such as AWS. The AWS SOC 2 is an evaluation of the design and operating effectiveness of controls that meet the criteria for the security and availability principles set forth in the AICPA’s Trust Services Principles criteria. This report provides additional transparency into AWS security and availability based on a pre-defined industry standard of leading practices and further demonstrates the commitment of AWS to protecting customer data. The SOC2 report information includes outlining AWS controls, a description of AWS Services relevant to security, availability and confidentiality as well as test results against controls. You will likely find the SOC 2 report to be the most detailed and relevant SOC report as it relates to GxP compliance.

 AWS publishes a Service Organization Controls 3 (SOC 3) report. The SOC 3 report is a publicly-available summary of the AWS SOC 2 report. The report includes the external auditor’s assessment of the operation of controls (based on the AICPA’s Security Trust Principles included in the SOC 2 report), the assertion from AWS management regarding the effectiveness of controls, and an overview of AWS Infrastructure and Services.

## FedRAMP
<a name="fedramp"></a>

 The Federal Risk and Authorization Management Program (FedRAMP) is a US government-wide program that delivers a standard approach to the security assessment, authorization, and continuous monitoring for cloud products and services. FedRAMP uses the NIST Special Publication 800 series and requires cloud service providers to receive an independent security assessment conducted by a third-party assessment organization (3PAO) to ensure that authorizations are compliant with the Federal Information Security Management Act (FISMA).

 For AWS Services in Scope for FedRAMP assessment and authorization, see [https://aws.amazon.com/compliance/services-in-scope/](https://aws.amazon.com/compliance/services-in-scope/)

## ISO 9001
<a name="iso-9001"></a>

 ISO 9001:2015 outlines a process-oriented approach to documenting and reviewing the structure, responsibilities, and procedures required to achieve effective quality management within an organization. Specific sections of the standard contain information on topics such as:
+  Requirements for a quality management system (QMS), including documentation of a quality manual, document control, and determining process interactions
+  Responsibilities of management
+  Management of resources, including human resources and an organization’s work environment
+  Service development, including the steps from design to delivery
+  Customer satisfaction
+  Measurement, analysis, and improvement of the QMS through activities like internal audits and corrective and preventive actions

 The AWS ISO 9001:2015 certification directly supports customers who develop, migrate and operate their quality-controlled IT systems in the AWS cloud. You can leverage AWS compliance reports as evidence for your own ISO 9001:2015 programs and industry-specific quality programs, such as GxP in life sciences and ISO 131485 in medical devices.

## ISO/IEC 27001
<a name="isoiec-27001"></a>

 ISO/IEC 27001:2013 is a widely-adopted global security standard that sets out requirements and best practices for a systematic approach to managing company and customer information that’s based on periodic risk assessments appropriate to ever-changing threat scenarios. In order to achieve the certification, a company must show it has a systematic and ongoing approach to managing information security risks that affect the confidentiality, integrity, and availability of company and customer information.

 This widely-recognized international security standard specifies that AWS do the following:
+  We systematically evaluate AWS information security risks, taking into account the impact of threats and vulnerabilities.
+  We design and implement a comprehensive suite of information security controls and other forms of risk management to address customer and architecture security risks.
+  We have an overarching management process to ensure that the information security controls meet our needs on an ongoing basis.

 AWS has achieved ISO 27001 certification of the Information Security Management System (ISMS) covering AWS infrastructure, data centers, and services.

## ISO/IEC 27017
<a name="isoiec-27017"></a>

 ISO/IEC 27017:2015 provides guidance on the information security aspects of cloud computing, recommending the implementation of cloud-specific information security controls that supplement the guidance of the ISO/IEC 27002 and ISO/IEC 27001 standards. This code of practice provides additional information security controls implementation guidance specific to cloud service providers.

 The AWS attestation to the ISO/IEC 27017:2015 standard not only demonstrates an ongoing commitment to align with globally-recognized best practices, but also verifies that AWS has a system of highly precise controls in place that are specific to cloud services.

## ISO/IEC 27018
<a name="isoiec-27018"></a>

 ISO 27018 is the first International code of practice that focuses on protection of personal data in the cloud. It is based on ISO information security standard 27002 and provides implementation guidance on ISO 27002 controls applicable to public cloud Personally Identifiable Information (PII). It also provides a set of additional controls and associated guidance intended to address public cloud PII protection requirements not addressed by the existing ISO 27002 control set.

 AWS has achieved ISO 27018 certification, an internationally recognized code of practice, which demonstrates the commitment of AWS to the privacy and protection of your content.

## HITRUST
<a name="hitrust"></a>

 The Health Information Trust Alliance Common Security Framework (HITRUST CSF) leverages nationally and internationally accepted standards and regulations such as GDPR, ISO, NIST, PCI, and HIPAA to create a comprehensive set of baseline security and privacy controls.

 HITRUST has developed the HITRUST CSF Assurance Program, which incorporates the common requirements, methodology, and tools that enable an organization and its business partners to take a consistent and incremental approach to managing compliance. Further, it allows business partners and vendors to assess and report against multiple sets of requirements.

 Certain AWS services have been assessed under the HITRUST CSF Assurance Program by an approved HITRUST CSF Assessor as meeting the HITRUST CSF Certification Criteria. The certification is valid for two years, describes the AWS services that have been validated, and can be accessed at [https://aws.amazon.com/compliance/hitrust/](https://aws.amazon.com/compliance/hitrust/). You may look to leverage the AWS HITRUST CSF certification of AWS services to support your own HITRUST CSF certification, in complement to your GxP compliance programs.

## CSA Security, Trust & Assurance Registry (STAR)
<a name="csa-security-trust-assurance-registry-star"></a>

 In 2011, the [Cloud Security Alliance (CSA) launched STAR](https://cloudsecurityalliance.org/press-releases/2011/08/04/csa-announces-star/), an initiative to encourage transparency of security practices within cloud providers. The CSA Security, Trust & Assurance Registry (STAR) is a free, publicly accessible registry that documents the security controls provided by various cloud computing offerings, thereby helping users assess the security of cloud providers they currently use or are considering.

 AWS participates in the voluntary CSA Security, Trust & Assurance Registry (STAR) Self-Assessment to document AWS compliance with CSA-published best practices. AWS publishes the completed [CSA Consensus Assessments Initiative Questionnaire (CAIQ)](https://d1.awsstatic.com/whitepapers/compliance/CSA_Consensus_Assessments_Initiative_Questionnaire.pdf) on the AWS website.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
