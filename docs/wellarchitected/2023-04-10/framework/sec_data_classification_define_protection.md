---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_data_classification_define_protection.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC07-BP02 Define data protection controls
<a name="sec_data_classification_define_protection"></a>

 Protect data according to its classification level. For example, secure data classified as public by using relevant recommendations while protecting sensitive data with additional controls.

By using resource tags, separate AWS accounts per sensitivity (and potentially also for each caveat, enclave, or community of interest), IAM policies, AWS Organizations SCPs, AWS Key Management Service (AWS KMS), and AWS CloudHSM, you can define and implement your policies for data classification and protection with encryption. For example, if you have a project with S3 buckets that contain highly critical data or Amazon Elastic Compute Cloud (Amazon EC2) instances that process confidential data, they can be tagged with a `Project=ABC` tag. Only your immediate team knows what the project code means, and it provides a way to use attribute-based access control. You can define levels of access to the AWS KMS encryption keys through key policies and grants to ensure that only appropriate services have access to the sensitive content through a secure mechanism. If you are making authorization decisions based on tags you should make sure that the permissions on the tags are defined appropriately using tag policies in AWS Organizations.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>
+  Define your data identification and classification schema: Identification and classification of your data is performed to assess the potential impact and type of data you store, and who can access it.
  +  [AWS Documentation](https://docs.aws.amazon.com/)
+  Discover available AWS controls: For the AWS services you are or plan to use, discover the security controls. Many services have a security section in their documentation.
  +  [AWS Documentation](https://docs.aws.amazon.com/)
+  Identify AWS compliance resources: Identify resources that AWS has available to assist.
  +  [https://aws.amazon.com/compliance/](https://aws.amazon.com/compliance/?ref=wellarchitected)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [AWS Documentation](https://docs.aws.amazon.com/)
+  [Data Classification whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html)
+  [Getting started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html)
+  [AWS Compliance](https://aws.amazon.com/compliance/)

 **Related videos:**
+  [Introducing the New Amazon Macie](https://youtu.be/I-ewoQekdXE)
