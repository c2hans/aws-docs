---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/tools-integration.html
---

# Tools integration
<a name="tools-integration"></a>

Most enterprises rely on ITSM tools to automate their on-premises operations. When these organizations move to the cloud, they need to maintain their existing ITSM tools and processes. Attempting to completely replace existing ITSM tools and retrain staff on new operational processes would be costly and time-consuming, and could significantly delay migration initiatives.

To address this need, AWS provides several integration patterns that enable enterprises to connect their existing ITSM tools with AWS services. These integration patterns allow organizations to maintain operational continuity while progressively adopting cloud capabilities. The following table outlines the common integration patterns between ITSM tools and AWS services. These patterns provide a practical approach to cloud adoption without disrupting existing operational processes.

|
|
| Scenario | Description and AWS tools |
| --- |--- |
| Self-service and self-provisioning | Enterprise users self-provision resources on AWS by using the [AWS Service Catalog](https://aws.amazon.com/servicecatalog/) connector in ITSM without the need to sign into the AWS Management Console. |
| CMDB integration | [AWS Config](https://aws.amazon.com/config/) and [AWS Systems Manager](https://aws.amazon.com/systems-manager/) provide native discovery services that monitor continuous integrations (CIs) on AWS. Resource configurations, compliance states, and changes can be automatically logged into a CMDB. |
| AMS–ITSM integration | [AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/) integration by using AWS Service Management Connector App version 2 provides flexibility to customize integrations for various needs. |
| Ticketing | Bi-directional integration between the [AWS Support API](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html) and ITSM enables tickets to seamlessly flow between AWS Enterprise Support and ITSM incidents. Integration with [OpsCenter.](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) |
| Monitoring | [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms trigger incidents in ITSM for remediation or workflow initiation.  |
| Migration acceleration using ITSM (MAUS) | You can use ITSM discovery modules or CMDB data to define your on-premises landscape for mass migration projects. Data mapping can be imported into [AWS Migration Portfolio Assessment](https://mpa.accelerate.amazonaws.com/) to automate migration portfolio analysis and business case validation. |
