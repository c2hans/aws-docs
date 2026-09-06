---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-financial-services-guidance-australia/appendix-2-key-aspects-of-cpg-234.html
---

# Appendix 2: Key aspects of CPG 234
<a name="appendix-2-key-aspects-of-cpg-234"></a>

 CPG 234 Information Security (CPG 234) provides APRA's guidance on particular areas to assist ARIs in the management of information security. CPG 234 doesn't create enforceable requirements on an ARI but addresses areas where APRA identifies weaknesses as part of its ongoing supervisory activities.

 CPG 234 sets out risk management principles and best practice standards to guide ARIs in the following areas:
+  Considerations for the Board
+  Roles and responsibilities
+  Information security capability
+  Policy framework
+  Information asset identification and classification
+  Implementation of controls
+  Incident management
+  Testing control effectiveness
+  Internal audit
+  Notification

 CPG 234 also provides additional specific guidance in the form of the following attachments:
+  Security principles
+  Training and awareness
+  Identity and access
+  Software security
+  Cryptographic techniques
+  Customer security
+  Testing techniques
+  Reporting

 AWS has produced an [AWS CPG 234 Workbook](https://us-east-1.console.aws.amazon.com/artifact/v2/reports/details/report-rdeQ9sV6KVvQXAm0?region=us-east-1) that documents relevant controls and guidance (referencing the AWS Well-Architected Framework) for each of the CPG 234 guidelines. The Workbook covers the 10 sections and 8 attachments within CPG 234 by APRA, and where AWS can provide information as part of the shared responsibility model, that information is mapped against the relevant section of CPG 234.

 The following is a sample of the AWS response to CPG 234's *Implementation of controls* section:

|   **Guideline**   |   **Responsibility**   |   **Response**   |
| --- | --- | --- |
|  **54-55:** <br /> **Cryptographic techniques to restrict access**  |  AWS <br /> AWS control objective  |  Data security and privacy – Key generation <br /> AWS establishes and manages cryptographic keys for required cryptography employed within the system boundary. AWS produces, controls, and distributes symmetric cryptographic keys using U.S. National Institute of Standards and Technology (NIST)- approved key management technology and processes in the AWS information system. An AWS-developed secure key and credential manager is used to create, help protect, and distribute symmetric keys, and is used to secure and distribute: +   AWS credentials needed on hosts  <br />+   RSA public/private keys  <br />+   X.509 Certificates  <br /> Cryptographic keys are securely stored and periodically rotated.  |
|  **54-55:** <br /> **Cryptographic techniques to restrict access**  |  Customer <br /> Well-Architected Framework  |  Well-Architected – Question and Best Practice: SEC-9 – How do you protect your data at rest? +   Implement secure key management  <br /> Encryption keys must be stored securely and rotated with strict access control, for example, by using a key management service such as [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms). Consider using different keys for segregation of different data classification levels and retention requirements.  |

 ARIs can obtain a copy of the AWS CPG 234 Workbook through the AWS Artifact portal.

 ARIs should review the AWS responses in the AWS APRA CPG 234 Workbook and enrich them with the ARI's own company-wide controls.
