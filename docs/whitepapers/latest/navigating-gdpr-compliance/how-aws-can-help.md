---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/how-aws-can-help.html
---

# How AWS Can Help
<a name="how-aws-can-help"></a>

**Table 1 – How AWS can help you navigate GDPR compliance **

| **Area** | **Description** | **AWS Services and Tools** |
| --- | --- | --- |
| Strong Compliance Framework | Appropriate technical and organizational measures may need to include “the ability to ensure the ongoing confidentiality, integrity, availability, and resilience of the processing systems and services.” | The framework is validated by following certifications and attestations:<br />SOC 1 / SSAE 16 / ISAE 3402 (formerly SAS 70) / SOC 2 / SOC 3 PCI DSS Level 1 ISO 9001 / ISO 27001 / ISO 27017 / ISO 27018 / ISO 27701 NIST FIPS 140-2 Cloud Computing Compliance Criteria Catalog (C5) |
| Data Access Control | The controller “…shall implement appropriate technical and organizational measures for ensuring that, by default, only personal data which are necessary for each specific purpose of the processing are processed.” | AWS Identity and Access Management (IAM) <br />Amazon Cognito <br />AWS Shield and AWS WAF <br />AWS Resource Access Manager<br />Amazon CloudFront<br />AWS Organizations <br />AWS CloudTrail |
| Monitoring, Logging and Records of Processing | “Each controller and, where applicable, the controller’s representative, shall maintain a record of processing activities under its responsibility.” “…the controller and the processor shall implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk […]” | AWS Config <br />Amazon CloudWatch <br />AWS Control Tower <br />Amazon GuardDuty <br />Amazon Detective <br />Amazon Inspector <br />Amazon Macie <br />AWS Systems Manager <br />AWS Security Hub <br />AWS Security Lake<br />Amazon Security Lake<br />AWS Tools and SDKs |
| Protecting your Data on AWS | Organizations must “implement appropriate technical and organizational measures to ensure a level of security appropriate to the risk, including […] the pseudonymization and encryption of personal data.” | AWS Certificate Manager <br />AWS CloudHSM <br />AWS Nitro Systems |
| Data Protection Impact Assessment (DPIA) | AWS provides services and resources that assist customers in completing their DPIA when using AWS services. The GPDR determines the customer is responsible for determining if a DPIA is required, for choosing an assessment methodology, and for performing the assessment. | AWS Service Terms<br />AWS Artifact<br />AWS Compliance Programs |
| Data Transfer Impact Assessment (DTIA) | The Annex to this whitepaper provides more information for customers that want to perform an assessment on data transfers when using AWS services. | AWS Service Terms<br />AWS Privacy Features<br />AWS Sub-Processors webpages |
| PII Data Discovery | Organizations must identify and classify personal data to implement appropriate protection measures and demonstrate GDPR compliance. AWS provides tools to automatically discover, classify, and monitor personal data across AWS services. | Amazon Macie for automated sensitive data discovery and classification<br />AWS Glue Data Catalog for data inventory and classification<br />Amazon EMR for large-scale data processing and analysis<br />AWS CloudWatch Logs pattern matching for log analysis |
