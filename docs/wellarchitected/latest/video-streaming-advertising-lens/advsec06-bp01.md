---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec06-bp01.html
---

# ADVSEC06-BP01 Verify your advertising workload remains adherent to data protection regulations
<a name="advsec06-bp01"></a>

 Maintaining compliance is essential to operate and grow your solution. Data encryption is a key requirement for several compliance programs; you can utilize AWS KMS to facilitate data encryption and key management for your solution. KMS allows for the creation and management of cryptographic keys which can be used to encrypt data at rest and in transit. It simply integrates with other AWS services and maintains an audit trail for key usage. KMS also maintains validation and certifications from multiple compliance regimes including FIPS, PCI DSS, and HIPAA.

## Implementation guidance
<a name="ig-advsec06-bp01"></a>

 To assist with data governance consider using Amazon Macie. Macie can automatically scan and identify sensitive data across AWS environments. The service can categorize data based on content type and sensitivity level. Based on the data classification Macie provides a risk score for different datasets and storage locations. Amazon Macie can assist to meet regulatory requirements including GDPR, CCPA, HIPAA, by generating detailed reports on data types and locations for regulatory audits.

## Key AWS services
<a name="key-aws-services-9"></a>
+  AWS KMS
+  Amazon Macie

## Resources
<a name="resources-14"></a>
+  [Compliance validation for Macie](https://docs.aws.amazon.com/macie/latest/user/compliance-validation.html)
+  [Compliance validation for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/kms-compliance.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
