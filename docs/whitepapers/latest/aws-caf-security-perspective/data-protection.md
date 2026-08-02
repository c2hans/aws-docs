---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/data-protection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data protection
<a name="data-protection"></a>

**Note**
Maintain visibility and control over data, and how it is accessed and used in your organization.

 [https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) your data from unintended unauthorized access and potential unauthorized data changes, will help develop and drive the data protection component of your cloud security strategy. As you migrate data to the AWS Cloud, maintain visibility and control over how your data is being accessed and used throughout your organization. Before architecting any system, foundational practices that influence security should be in place. For example, [data classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html) provides a way to categorize organizational data based on levels of sensitivity. [Encryption](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/data-encryption.html) protects that data by way of rendering it unintelligible to unauthorized access. These tools and techniques support such objectives as preventing financial loss, and complying with regulatory obligations.

 Organizations will often look to compliance frameworks such as the [National Institute of Standards and Technology](https://aws.amazon.com/compliance/nist/) (NIST), [Center for internet Security](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-cis.html) (CIS), or their general industry for regulatory requirements and guidance on security controls that should be implemented. In this section, we will draw from the AWS Well-Architected Framework in the context of [Data Protection](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-dataprot.html).

## Start
<a name="data-protection-start"></a>

 To start building out a data protection strategy in AWS, focus on the following four elements.

 **Identify the data within your workloads.**

 Understand the type and classification of data your workloads are processing. What are the associated business processes, data owners, applicable legal and compliance requirements? Where are your data stored? These answers will help you identify the security controls that must be enforced to secure your environment. This may include classifications to indicate if the data are intended to be:
+  Publicly available,
+  Internal use only, such as customer personally identifiable information (PII), or
+  Intended for more restricted access, such as intellectual property, legally privileged, or marked sensitive.

 By carefully managing an appropriate data classification system and each workload's level of protection requirements, you can accurately map the controls and level of access and protection appropriate for your data. For example, public content is available for anyone to access, but internal or sensitive content may be encrypted and stored in a protected manner that requires authorized access to a key for decrypting the content.

 **Define data protection controls.**

 Use [https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/welcome.html](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/welcome.html) to separate AWS accounts per sensitivity and potentially community of interest. Use IAM policies, SCPs, AWS KMS, and [AWS CloudHSM](https://docs.aws.amazon.com/cloudhsm/latest/userguide/introduction.html) to define and implement your requirements for data classification and protection with encryption. For example, if you have a project with S3 buckets that contain highly critical data, or EC2 instances that process confidential data, they can be tagged with a "Project=ABC" tag. Only your immediate team knows what the project code means, and it provides a way to use attribute-based access control. If you are making authorization decisions based on tags, you should make sure that the permissions on the tags are defined appropriately using [tag policies in AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html).

 **Define data lifecycle management.**

 Base your defined lifecycle strategy on sensitivity level as well as legal and organization requirements. Include the duration for which you retain data, data destruction processes, data access management, data transformation, and data sharing. When choosing a data classification methodology, balance usability versus access. Always use a defense in depth approach and reduce human access to data and mechanisms for transforming, deleting, or copying data. For example, require users to strongly authenticate access to an application. Give the application, rather than the users, the requisite access permissions to perform "action at a distance." In addition, confirm that users come from a trusted network path and require access to the decryption keys. Use tools, such as dashboards and automated reporting, to give users information from the data, rather than giving them direct access to the data.

 **Automate identification and classification.**

 Automating the identification and classification of data can help you implement the correct controls. Rather than manual, use automation to reduce the risk of human error and exposure. Amazon Macie uses machine learning to automatically discover, classify, and protect sensitive data in AWS and recognizes sensitive data, such as PII or intellectual property. Macie provides you with dashboards and alerts that give visibility into how this data is being accessed or moved. To help you determine appropriate protection and retention controls, [https://docs.aws.amazon.com/whitepapers/latest/data-classification/welcome.html?secd_dp2](https://docs.aws.amazon.com/whitepapers/latest/data-classification/welcome.html?secd_dp2) your data based on criticality and sensitivity.

 **Summary**

 We draw from the four areas that should initially be focused on to develop the foundation in which other aspects of data protection will rely (such as encryption at rest or in transit).

 AWS has prescriptive guidance within the [https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html) and [https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/welcome.html) to help organizations explore developing a strategy to support their broader data protection initiatives in AWS.

 First, develop a data classification strategy, and discover and identify where and what data resides in your workloads on AWS. Then, tag your data, resources, and assets to allow for proper scoping of security controls. Developing a tagging strategy is equally important as the development of your data classification strategy and subsequent discovery of classified data. Tagging can be an effective scaling mechanism for implementing cloud management and governance strategies. It helps identify, protect, detect, and respond to events in AWS. Tags can simplify ABAC, as well as streamline automation and operations, grouping of resources for enhanced visibility, and provide effective cost management.

## Advance
<a name="data-protection-advance"></a>

 Now that the foundation has been set in AWS, protect resources that have been classified, discovered, and tagged. Think of data protection in AWS as layers, and build out a defense in depth approach to protect your resources. Don't limit your protection to a single control, whether it is for an EC2 instance hosting an application, an EBS volume, or a file containing sensitive information in Amazon S3. The AWS Well-Architected Framework provides similar guidance.

**Apply security at all layers**
Apply a defense in depth approach with multiple security controls. Apply to all layers (for example, edge of network, VPC, load balancing, every instance and compute service, operating system, application, and code).

 Focus your data protection controls on these core areas:

 **Identity and access management**

 Embracing least privilege is critical to the protection of data, both from accidental exposure, as well as from potential malicious activities. When [https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_controlling.html), use specific Amazon Resource Names (ARNs) and condition statements to limit over exposure to resources. Avoid using wildcard values whenever possible to reduce the overall permissions being granted to AWS entities. Enable AWS IAM Access Analyzer to monitor these access policies and alert you when it detects associate IAM policies not following protocol, or with access to external accounts.

 Different controls including access (using least privilege), backups (see [Reliability Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)), isolation, and versioning can all help protect your data at rest. Access to your data should be audited using detective mechanisms covered earlier in this whitepaper including AWS CloudTrail and service level logs, such as [S3 Access Logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html). You should inventory what data is publicly accessible, and plan for how you can reduce the amount of data available over time. [Amazon Glacier Vault Lock](https://docs.aws.amazon.com/amazonglacier/latest/dev/vault-lock.html) and [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) are capabilities providing mandatory access control. This means that once a vault policy is locked with the compliance option, not even the root user can change it until the lock expires. Access should also directly link to the organizations data classification strategy. This embraces the principal of least privilege, as well as proper scoping of business functions.

 **Resource policies**

 Many resources in AWS, such as [VPC Endpoints](https://wa.aws.amazon.com/wellarchitected/2020-07-02T19-33-23/wat.concept.vpc-endpoint.en.html), S3 buckets, and [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys), use [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based). These policies grant the specified principal permission to perform specific actions on that resource, and define under what conditions this applies. They complement Identity policies and offer additional layers of protection.

 **Encryption**

 A critical component of any data protection strategy is encryption of data at rest, in transit, and in use.

 *Data at rest* represents any data that you persist in non-volatile storage for any duration in your workload. This includes block storage, object storage, databases, archives, IoT devices, and any other storage medium on which data is persisted. Protecting your data at rest reduces the risk of unauthorized access, when encryption and appropriate access controls are implemented.

 *Data in transit* is any data that is sent from one system to another. This includes communication between resources within your workload as well as communication between other services and your end users. By providing the appropriate level of protection for your data in transit, you protect the confidentiality and integrity of your workload's data.

 *Data in use* refers to data that is not simply being passively stored in a stable destination, such as a central [data warehouse](https://aws.amazon.com/data-warehouse/). It is working its way through other parts of an IT architecture. Data in use may be in the process of being generated, amended or updated, erased, or viewed through various interface endpoints.

 Using encryption should be the only way to store sensitive data. AWS KMS integrates seamlessly with many AWS services to make it easier for you to encrypt all your data at rest. For example, in Amazon S3 you can set [https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html) on a bucket so that all new objects are automatically encrypted. Additionally, [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) and  [https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html) support the enforcement of encryption by setting default encryption. Use [https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html) to automatically check that you are using encryption, for [https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html](https://docs.aws.amazon.com/config/latest/developerguide/encrypted-volumes.html),  [https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html](https://docs.aws.amazon.com/config/latest/developerguide/rds-storage-encrypted.html), and [https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html](https://docs.aws.amazon.com/config/latest/developerguide/s3-default-encryption-kms.html).

 **Key management**

To support the encryption components listed preceding, usage of key management services such as AWS KMS is recommended. The KMS keys that you create are [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk). AWS services that use KMS keys to encrypt your service resources often create keys for you. KMS keys that AWS services create in your AWS account are [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk). KMS keys that AWS services create in a service account are [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk). Generate keys for specific applications, workloads, services, and environments of use AWS KMS Customer Managed Key (CMK). There should be different keys for Human Resources applications and Finance applications, and for Amazon S3 and Amazon RDS. And you should have different keys for development environments and production environments. Fine-grained access controls can be applied to keys to limit scope and any potential impact. More information about AWS KMS and best practices can be located in the [Security Best Practices for AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html)*,*

 **Logging, monitoring, and alerting**

 To confirm that the data protection controls are working as expected, it is important to set up detective controls, and then responsive controls as your maturity in cloud increases. Use automated tools to validate and enforce data at rest controls continuously. For example, verify that there are only encrypted storage resources. You can automate validation that all EBS volumes are encrypted using [https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html).  [https://aws.amazon.com/security-hub/](https://aws.amazon.com/security-hub/) can also verify a number of different controls through automated checks against security standards. Additionally, your AWS Config Rules can automatically [https://docs.aws.amazon.com/config/latest/developerguide/remediation.html#setup-autoremediation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html#setup-autoremediation).

 Audit the use of encryption keys to validate that the access control mechanisms on the keys are appropriately implemented. For example, any AWS service using an AWS KMS key logs each use in AWS CloudTrail. You can then query AWS CloudTrail and make sure that all uses of your keys are valid, by using a tool such as [Amazon CloudWatch Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html).

 Amazon GuardDuty automatically detects suspicious activity or attempts to move data outside of defined boundaries. For example, GuardDuty can detect S3 read activity that is unusual with the [https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#exfiltration-s3-objectreadunusual](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_finding-types-s3.html#exfiltration-s3-objectreadunusual) finding. In addition to Amazon GuardDuty, [https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), which capture network traffic information, can be used with Amazon EventBridge to trigger detection of abnormal connections, both successful and denied. [https://aws.amazon.com/blogs/storage/protect-amazon-s3-buckets-using-access-analyzer-for-s3](https://aws.amazon.com/blogs/storage/protect-amazon-s3-buckets-using-access-analyzer-for-s3) can assess *what* data is accessible to *who* in your [S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html).

 **Summary**

 Putting all of this guidance together, a real-world example would be a principal (human or machine) who must upload data to S3. This data will then need to be pulled down and processed by an application. As part of their [IAM role policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html), the principal would have access to Amazon S3. Through constraints in the policy, they would have access only to *specific* S3 buckets, with the ability to upload. This principal also has permissions to use a [Customer Managed Key (CMK) in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) to encrypt the data in Amazon S3. The CMK itself has a resource policy attached, permitting the principal to only invoke the encrypt API. This same resource policy also defines the application [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) and permits the decrypt API to be invoked as part of the download and processing by the application. The S3 bucket has a resource policy attached to only allow uploads from defined principals, and download from defined applications IAM roles. It also has restrictions to only select [VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) inside of the AWS account that is part of a defined [AWS Organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html). The bucket policy also only allows uploads if a specific [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) is defined as part of the PUT API.

 In the preceding example, if one control fails, the data is not exposed, and in many cases, if two controls fail, the data is *still* protected. This might happen if the S3 bucket was accidentally made public and the principal's account credentials were compromised. This is an example of a defense in depth approach.

## Excel
<a name="data-protection-excel"></a>

 **Excel**

 At this stage of cloud maturity, data protection best practices include enhancing the foundation that was initially set, iterating on the capabilities built upon that foundation, moving towards *shift left* culture in [DevOps](https://aws.amazon.com/devops/), and focusing on automated remediations.

 **Advanced permissions management**

 Protecting data depends on the permission structure that you have built. While basic IAM provisions are an essential part of the foundation for all data protection strategies, advanced topics of IAM should be implemented when possible. ABAC is an advanced permissions management model that scopes all permissions by the tags of resources and entities. For example, an IAM role with the tag `Project X` should only have access to resources also tagged with `Project X`. More advanced AWS services can be used to further analyze and refine AWS permissions within your environment to adhere to the principle of least privilege. If you are using AWS Organizations, SCPs prevent sensitive actions from being taken on your most critical resources unless stringent conditions are met. IAM Access Analyzer is a tool that can identify all external access into your AWS environment. It has policy generation and validation capabilities to help you further scope your AWS IAM policies. It uses machine learning (ML) to understand the minimum permissions needed by your everyday workloads. These tools should be leveraged to automatically redefine [IAM policies on principals](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html) based on access needs observed over time.

 **Advanced encryption**

 Beyond the concepts of encryption of data at rest and in transit, advanced encryption should focus on using specific ciphers and elliptic curves for varying data protection needs. You should consider [quantum cryptography protections](https://docs.aws.amazon.com/kms/latest/developerguide/pqtls.html), tokenization, format preserving encryption (FPE), and masking. These types of encryption concepts are meant to solve specific industry and regulatory needs in addition to enhancement of encryption protections. For example, use [Federal Information Processing Standard](https://aws.amazon.com/compliance/fips/) (FIPS) 140-2 L3 technologies for US government systems or regulated financial organizations, or use tokenization to meet [Payment Card Industry](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-pcidss.html) (PCI) requirements on secure storage of customer data. The hardware security modules (HSMs) used in AWS KMS have been awarded FIPS 140-2 Security Level 3 certification from the U.S. National Institute of Standards and Technology (NIST).

 **Key management**

 Another domain of data protection to further develop along with your organizations' cloud maturity is *key management*. Using AWS KMS, you can enforce automated key rotation schedules, confirm that resources are encrypted with distinct keys, define key policies to restrict which principals have admin permissions (delete, create keys) and use (encrypt, decrypt), and more. To meet other use cases, or for customers who want to control the generation of key material, AWS CloudHSM offers a managed hardware security module solution that allows you to generate and use your own keys within a dedicated hardware space on AWS. AWS CloudHSM can be connected to AWS KMS to create a [Custom Key Store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) where you can generate and manage keys inside of a FIPS 140-2 L3 boundary.

 **Replication, backups, and recovery**

 A robust data protection strategy should have measures in place to prevent unintended data deletion. Confirm that replication, backup, and recovery mechanisms are implemented so your data is resilient against unforeseen incidents of data loss. Carefully consider replication capabilities across AWS services that may handle your data and determine the best replication needs for your workloads. [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a service that allows you to centrally manage and automate backups across AWS services and hybrid workloads. Implement automated recovery plans for your resources in the event of unexpected failure so your workloads experience minimal downtime.

 **Dynamic data classification**

 As you expand on your [https://d1.awsstatic.com/whitepapers/compliance/AWS_Data_Classification.pdf](https://d1.awsstatic.com/whitepapers/compliance/AWS_Data_Classification.pdf) strategy, build out automated mechanisms to identify new types of data. This data is generated by using different datasets through a process commonly known as *data fusion*. This generally occurs when querying data across datasets or in [data lakes](https://aws.amazon.com/big-data/datalakes-and-analytics/what-is-a-data-lake/). For example, if you take one dataset of city names, and one dataset of customer last names, the resulting combined dataset now contains PII data. This new data must be classified and protected. Use tools like Amazon Macie to identify these new datasets and then apply data classification, tagging, and protective controls.

 **Data usage monitoring**

 As you start to acquire data in varying services such as Amazon EBS, Amazon EFS, Amazon S3, data lakes, data warehouses, it is increasingly important to monitor this data and its usage. Build mechanisms that allow for reporting, analytics, alerts, and automated remediation across data types and locations. Understand how, where, and by who your data is being used, to identify norms.

 **Summary**

 As part of advanced data protection operations in AWS, you will want to use all of the guidance outlined in this whitepaper. Add guidance and best practices that are applicable to your organizations regulatory and compliance needs. It is important that you create a defense in depth approach to data protection in AWS, and implement preventative, detective, and responsive mechanisms. Use mechanisms such as automated rescoping of IAM permissions based off of observed usage patterns, and auto enforcement of data classification and tagging. You can automate enforcement of encrypted resources, alerting on abnormal data usage, and backup and recovery as well. Mine logs and analytics to identify new patterns and iterate on your data protection policy. Automate wherever possible, and push into the development pipeline to enforce data protection and security early on. Finally, ascertain that your mechanisms remain agile, so when new services and features are released, you are able to explore in development and securely promote to production.
