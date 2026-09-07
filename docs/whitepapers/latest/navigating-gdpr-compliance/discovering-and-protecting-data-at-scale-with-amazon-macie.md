---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/discovering-and-protecting-data-at-scale-with-amazon-macie.html
---

# Discovering and Protecting Data at Scale with Amazon Macie
<a name="discovering-and-protecting-data-at-scale-with-amazon-macie"></a>

Article 32 of the GDPR states that “[…] the controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including inter alia as appropriate: […]

(b) the ability to ensure the ongoing confidentiality, integrity, availability and resilience of processing systems and services;

[…]

(d) a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing.”

Having an ongoing data classification process is critical for adjusting security data processing to the nature of data. If your organization manages sensitive data, monitor where it resides, protect it properly, and provide evidence that you are enforcing data security and privacy as required to meet regulatory compliance requirements. To help the customer identify and protect their sensitive data at scale, AWS offers [Amazon Macie](https://aws.amazon.com/macie), a fully managed data security and data privacy service that uses pattern matching and machine learning models for detection of Personally Identifiable Information (PII) to discover and protect sensitive data stored in S3 buckets. Amazon Macie scans these buckets and provides a data categorization of them using managed data identifiers that are designed to detect several categories of sensitive data. Amazon Macie can detect PII such as full name, email address, birth date, national identification number, taxpayer identification or reference number, and more. The customer can define custom data identifiers that reflect their organization’s particular scenarios (for example, customer account numbers or internal data classification).

Amazon Macie continually evaluates the objects inside the buckets and automatically provides a summary of findings (Figure 4) for any unencrypted or publicly accessible data discovered that match with the defined data category. This data can include alerts for any unencrypted, publicly accessible objects or buckets shared with AWS accounts outside those you have defined in AWS Organizations. Amazon Macie is integrated with other AWS services, such as [AWS Security Hub](https://aws.amazon.com/security-hub/), to generate actionable security findings and provide an automatic and reactive action to the finding (Figure 5).

![Macie findings dashboard showing sensitive data objects detected in various resources with high severity.](https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/images/macie-findings-dashboard.png)

*Figure 4 – Data inspections and finding example *

In order to prevent sensitive data accidental disclosure, coming from log data in-transit such as credit card numbers or government ID’s logged by your systems, and applications, [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides data protection account level policy. Account level policies work in combination with log group level policies, allowing you to select patterns of sensitive log data to detect and protect broadly across all log groups in an AWS account. By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks according to the policy.
