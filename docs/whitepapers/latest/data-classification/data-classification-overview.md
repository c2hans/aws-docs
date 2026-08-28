---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Data classification overview
<a name="data-classification-overview"></a>

 Data classification is a foundational step in cybersecurity risk management. It involves identifying the types of data that are being processed and stored in an information system owned or operated by an organization. It also involves making a determination on the sensitivity of the data and the likely impact should the data face compromise, loss, or misuse.

 To ensure effective risk management, organizations should consider classifying data by working backward from the contextual use of the data, and creating a categorization scheme that takes into account whether a given use case results in significant impact to an organization’s operations (for example, if data is confidential, it needs to have integrity, and/or be available).

 As used in this document, the term “classification” implies a holistic approach inclusive of taxonomy, schemes, and categorization of data for confidentiality, integrity, and availability.

## Data classification value
<a name="data-classification-value"></a>

 Data classification has been used for decades to help organizations make determinations for safeguarding sensitive or critical data with appropriate levels of protection. Regardless of whether data is processed or stored in on premises systems or in the cloud, data classification may be a suggested starting point for determining the appropriate level of controls for the confidentiality, integrity, and availability of data based on risk to the organization.

 For example, data that is considered confidential should be treated with a higher standard of care than data consumed by the general public. Data classification allows organizations to evaluate data based on sensitivity and business impact, which then helps the organization assess risks associated with different types of data.

 Standards organizations, such as the International Standards Organization (ISO) and the National Institute of Standards and Technology (NIST), recommend data classification schemes so information can be effectively managed and secured according to its relative risk and criticality, advising against practices that treat all data equally. According to these organizations, each data classification level should be associated with a recommended baseline set of security controls that help provide protection against vulnerabilities, threats, and risks commensurate with the designated protection level.

 It is important to note the risks with over-classifying data. Sometimes organizations err by broadly classifying large disparate sets of data at the same sensitivity level. This over-classification can incur unwarranted expenses by putting into place costly controls that can additionally impact business operations. This approach can also divert attention to less critical datasets and limit business use of the data through unnecessary compliance requirements due to over-classification.

## Data classification process
<a name="data-classification-process"></a>

 Customers often seek tangible recommendations when it comes to establishing data classification policies. These steps help not only in the development phase, but can be used as measures when reassessing if datasets are in the appropriate tier with corresponding protections.

 The following paragraphs recommend a step-by-step approach, based on guidance supported by international standards that customers can consider when developing data classification policies:

1.  **Establishing a data catalog** *—* Conducting an inventory of the various data types that exist in the organization, how they are used, and whether any of it is governed by a compliance regulation or policy. Once the inventory is complete, group the data types into one of the data classification levels the organization has adopted. [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) lets you store, annotate, and share metadata in the AWS Cloud while providing comprehensive audit and governance capabilities, with schema change tracking and data access controls.

1.  **Assessing business critical functions and conduct an impact** **assessment** — An important aspect in determining the appropriate level of security for data sets is to understand the criticality of that data to the business. Following an assessment of business-critical functions, customers can conduct an impact assessment for each data type.

1.  **Labeling information** *—* Undergo a quality assurance assessment to ensure that assets and data sets are appropriately labeled in their respective classification buckets. Additionally, it may be necessary to create secondary labels for data sub-types to differentiate particular sets of data within a tier based on privacy or security compliance requirements. Using services such as  [Amazon SageMaker AI](https://aws.amazon.com/sagemaker) and [AWS Glue](https://aws.amazon.com/glue) provide insight, and can support data labeling activities.

1.  **Handling of assets** *—* When data sets are assigned a classification tier, data is handled according to the handling guidelines appropriate for that level, which include specific security controls. These handling procedures should be documented but also adjust as technology changes. (Refer to *Customer considerations for implementing data classification schemes* later in this document for additional information on data handling.)

1.  **Continuous monitoring** *—* Continue to monitor the security, usage and access patterns of systems and data. This can be done through automated (preferred) or manual processes to identify external threats, maintain normal system operations, install updates, and track changes to the environment.

 For guidance on how this process can be supported by AWS services, refer to the *Leveraging the AWS Cloud to support data classification* section of this document.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
