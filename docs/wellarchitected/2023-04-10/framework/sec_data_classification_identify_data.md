---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_data_classification_identify_data.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC07-BP01 Identify the data within your workload
<a name="sec_data_classification_identify_data"></a>

It’s critical to understand the type and classification of data your workload is processing, the associated business processes, where the data is stored, and who is the data owner. You should also have an understanding of the applicable legal and compliance requirements of your workload, and what data controls need to be enforced. Identifying data is the first step in the data classification journey.

**Benefits of establishing this best practice:**

 Data classification allows workload owners to identify locations that store sensitive data and determine how that data should be accessed and shared.

 Data classification aims to answer the following questions:
+ **What type of data do you have?**

  This could be data such as:
  +  Intellectual property (IP) such as trade secrets, patents, or contract agreements.
  +  Protected health information (PHI) such as medical records that contain medical history information connected to an individual.
  +  Personally identifiable information (PII), such as name, address, date of birth, and national ID or registration number.
  +  Credit card data, such as the Primary Account Number (PAN), cardholder name, expiration date, and service code number.
  +  Where is the sensitive data is stored?
  +  Who can access, modify, and delete data?
  +  Understanding user permissions is essential in guarding against potential data mishandling.
+ **Who can perform create, read, update, and delete (CRUD) operations? **
  +  Account for potential escalation of privileges by understanding who can manage permissions to the data.
+ **What business impact might occur if the data is disclosed unintentionally, altered, or deleted? **
  +  Understand the risk consequence if data is modified, deleted, or inadvertently disclosed.

By knowing the answers to these questions, you can take the following actions:
+  Decrease sensitive data scope (such as the number of sensitive data locations) and limit access to sensitive data to only approved users.
+  Gain an understanding of different data types so that you can implement appropriate data protection mechanisms and techniques, such as encryption, data loss prevention, and identity and access management.
+  Optimize costs by delivering the right control objectives for the data.
+  Confidently answer questions from regulators and auditors regarding the types and amount of data, and how data of different sensitivities are isolated from each other.

 **Level of risk exposed if this best practice is not established**: High

## Implementation guidance
<a name="implementation-guidance"></a>

 Data classification is the act of identifying the sensitivity of data. It might involve tagging to make the data easily searchable and trackable. Data classification also reduces the duplication of data, which can help reduce storage and backup costs while speeding up the search process.

 Use services such as Amazon Macie to automate at scale both the discovery and classification of sensitive data. Other services, such as Amazon EventBridge and AWS Config, can be used to automate remediation for data security issues such as unencrypted Amazon Simple Storage Service (Amazon S3) buckets and Amazon EC2 EBS volumes or untagged data resources. For a complete list of AWS service integrations, see the [EventBridge documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-types.html).

 [Detecting PII](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html) in unstructured data such as customer emails, support tickets, product reviews, and social media, is possible by [using Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/), which is a natural language processing (NLP) service that uses machine learning (ML) to find insights and relationships like people, places, sentiments, and topics in unstructured text. For a list of AWS services that can assist with data identification, see [Common techniques to detect PHI and PII data using AWS services](https://aws.amazon.com/blogs/industries/common-techniques-to-detect-phi-and-pii-data-using-aws-services/).

 Another method that supports data classification and protection is [AWS resource tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html). Tagging allows you to assign metadata to your AWS resources that you can use to manage, identify, organize, search for, and filter resources.

 In some cases, you might choose to tag entire resources (such as an S3 bucket), especially when a specific workload or service is expected to store processes or transmissions of already known data classification.

 Where appropriate, you can tag an S3 bucket instead of individual objects for ease of administration and security maintenance.

### Implementation steps
<a name="implementation-steps"></a>

**Detect sensitive data within Amazon S3: **

1.  Before starting, make sure you have the appropriate permissions to access the Amazon Macie console and API operations. For additional details, see [Getting started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html).

1.  Use Amazon Macie to perform automated data discovery when your sensitive data resides in [Amazon S3](https://aws.amazon.com/s3/).
   +  Use the [Getting Started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html) guide to configure a repository for sensitive data discovery results and create a discovery job for sensitive data.
   +  [How to use Amazon Macie to preview sensitive data in S3 buckets.](https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/)

      By default, Macie analyzes objects by using the set of managed data identifiers that we recommend for automated sensitive data discovery. You can tailor the analysis by configuring Macie to use specific managed data identifiers, custom data identifiers, and allow lists when it performs automated sensitive data discovery for your account or organization. You can adjust the scope of the analysis by excluding specific buckets (for example, S3 buckets that typically store AWS logging data).

1.  To configure and use automated sensitive data discovery, see [Performing automated sensitive data discovery with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd-account-manage.html).

1.  You might also consider [Automated Data Discovery for Amazon Macie](https://aws.amazon.com/blogs/aws/automated-data-discovery-for-amazon-macie/).

**Detect sensitive data within Amazon RDS: **

 For more information on data discovery in [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/) databases, see [Enabling data classification for Amazon RDS database with Macie](https://aws.amazon.com/blogs/security/enabling-data-classification-for-amazon-rds-database-with-amazon-macie/).

**Detect sensitive data within DynamoDB: **
+  [Detecting sensitive data in DynamoDB with Macie](https://aws.amazon.com/blogs/security/detecting-sensitive-data-in-dynamodb-with-macie/) explains how to use Amazon Macie to detect sensitive data in [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) tables by exporting the data to Amazon S3 for scanning.

**AWS Partner solutions: **
+  Consider using our extensive AWS Partner Network. AWS Partners have extensive tools and compliance frameworks that directly integrate with AWS services. Partners can provide you with a tailored governance and compliance solution to help you meet your organizational needs.
+  For customized solutions in data classification, see [Data governance in the age of regulation and compliance requirements](https://aws.amazon.com/big-data/featured-partner-solutions-data-governance-compliance/).

 You can automatically enforce the tagging standards that your organization adopts by creating and deploying policies using AWS Organizations. Tag policies let you specify rules that define valid key names and what values are valid for each key. You can choose to monitor only, which gives you an opportunity to evaluate and clean up your existing tags. After your tags are in compliance with your chosen standards, you can turn on enforcement in the tag policies to prevent non-compliant tags from being created. For more details, see [Securing resource tags used for authorization using a service control policy in AWS Organizations](https://aws.amazon.com/blogs/security/securing-resource-tags-used-for-authorization-using-service-control-policy-in-aws-organizations/) and the example policy on [preventing tags from being modified except by authorized principals](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_examples_tagging.html#example-require-restrict-tag-mods-to-admin).
+  To begin using tag policies in [AWS Organizations](https://aws.amazon.com/organizations/), it’s strongly recommended that you follow the workflow in [Getting started with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html) before moving on to more advanced tag policies. Understanding the effects of attaching a simple tag policy to a single account before expanding to an entire organizational unit (OU) or organization allows you to see a tag policy’s effects before you enforce compliance with the tag policy. [Getting started with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html) provides links to instructions for more advanced policy-related tasks.
+  Consider evaluating other [AWS services and features](https://docs.aws.amazon.com/whitepapers/latest/data-classification/using-aws-cloud-to-support-data-classification.html#aws-services-and-features) that support data classification, which are listed in the [Data Classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html) whitepaper.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Getting Started with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/getting-started.html)
+  [Automated data discovery with Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/discovery-asdd.html)
+  [Getting started with tag policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies-getting-started.html)
+  [Detecting PII entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-pii.html)

 **Related blogs:**
+  [How to use Amazon Macie to preview sensitive data in S3 buckets.](https://aws.amazon.com/blogs/security/how-to-use-amazon-macie-to-preview-sensitive-data-in-s3-buckets/)
+  [Performing automated sensitive data discovery with Amazon Macie.](https://aws.amazon.com/blogs/aws/automated-data-discovery-for-amazon-macie/)
+  [Common techniques to detect PHI and PII data using AWS Services](https://aws.amazon.com/blogs/industries/common-techniques-to-detect-phi-and-pii-data-using-aws-services/)
+  [Detecting and redacting PII using Amazon Comprehend](https://aws.amazon.com/blogs/machine-learning/detecting-and-redacting-pii-using-amazon-comprehend/)
+  [Securing resource tags used for authorization using a service control policy in AWS Organizations](https://aws.amazon.com/blogs/security/securing-resource-tags-used-for-authorization-using-service-control-policy-in-aws-organizations/)
+  [Enabling data classification for Amazon RDS database with Macie](https://aws.amazon.com/blogs/security/enabling-data-classification-for-amazon-rds-database-with-amazon-macie/)
+  [Detecting sensitive data in DynamoDB with Macie](https://aws.amazon.com/blogs/security/detecting-sensitive-data-in-dynamodb-with-macie/)

 **Related videos:**
+  [Event-driven data security using Amazon Macie](https://www.youtube.com/watch?v=onqA7MJssoU)
+  [Amazon Macie for data protection and governance](https://www.youtube.com/watch?v=SmMSt0n6a4k)
+  [Fine-tune sensitive data findings with allow lists](https://www.youtube.com/watch?v=JmQ_Hybh2KI)
