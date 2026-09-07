---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-financial-services-guidance-australia/operational-resilience-aws-and-the-shared-responsibility-model.html
---

# Operational resilience, AWS and the Shared Responsibility Model
<a name="operational-resilience-aws-and-the-shared-responsibility-model"></a>

 AWS and the financial services industry share a common interest in maintaining operational resilience capabilities; for example, the ability to provide continuous service despite disruptions. Continuity of services, especially for critical functions, is a key prerequisite for financial stability. AWS recognizes that financial institutions that use AWS need to comply with sector-specific regulatory obligations and internal requirements regarding operational resilience, such as CPS 230.

 At AWS, we define operational resilience as the ability to provide continuous service through people, processes, and technology that are aware of and adaptable to constant change. It is a real-time, execution-oriented norm embedded in the culture of AWS that is distinct from traditional approaches in information security, business continuity, disaster recovery, and crisis management, which rely primarily on centralized, hierarchical programs focused on documentation development and maintenance.

 However, operational resilience is a shared responsibility; AWS is responsible for making sure that the services used by our customers - the building blocks for their applications - are continuously available and making sure that we are prepared to handle a wide range of events that could affect our cloud infrastructure. AWS customers are responsible for designing, testing, and deploying their applications on AWS in a manner that achieves the availability and resiliency they need, including those mission-critical applications that require that AWS services are available when customers need them, even upon the occurrence of a service impairment and/or disruption.

![Diagram showing the AWS shared responsibility model](https://docs.aws.amazon.com/whitepapers/latest/aws-financial-services-guidance-australia/images/shared-responsibility-model.png)

 The AWS Shared Responsibility Model is fundamental to understanding the respective roles of AWS and its customers within the context of cloud services. AWS is responsible for the resiliency of the hardware, software, networking, and facilities that run the services offered by AWS.

 The responsibility of AWS customers is determined by the AWS services they select, because the service selection determines the amount of configuration work that customers must perform as part of their resiliency responsibilities. For example, a service such as [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2) requires customers to perform all the necessary resiliency configuration and management tasks. Customers that deploy Amazon EC2 instances are responsible for [deploying Amazon EC2 instances across multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/use-fault-isolation-to-protect-your-workload.html) (such as AWS Availability Zones), and can [implement self-healing](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-to-withstand-component-failures.html) architectures using services such as Amazon EC2 Auto Scaling, and using [resilient workload architecture best practices](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/workload-architecture.html) for applications installed on the Amazon EC2 instances.

 For abstracted services, such as [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/) and [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), AWS operates the infrastructure layer, the operating system, and environments, and customers access the endpoints to store and retrieve data. Customers are responsible for managing resiliency of their data, including backup, versioning and replication strategies, classifying their assets, and using identity and access management tools to apply the appropriate permissions.

## Resilience of the cloud
<a name="resilience-of-the-cloud"></a>

 AWS infrastructure and services operate under several compliance standards and industry certifications across geographies and industries. Customers can use the AWS compliance certifications to validate the implementation and effectiveness of internal controls at AWS, including security best practices and certifications.

 The AWS compliance program is based on the following actions:
+  **Validating** that AWS services and facilities across the globe maintain a ubiquitous control environment that is operating effectively. The AWS control environment encompasses the people, processes, and technology necessary to establish and maintain an environment that supports the operating effectiveness of the AWS control framework. AWS has integrated applicable cloud-specific controls identified by leading cloud computing industry bodies into the AWS control framework. AWS monitors these industry groups to identify leading practices that customers can implement, and to better assist customers with managing their control environment.
+  **Demonstrating** the AWS compliance posture to help customers assess compliance with industry and government requirements. AWS engages with external certifying bodies and independent auditors to provide customers with information regarding the policies, processes, and controls that have been established and operated by AWS. ARIs can use this information to perform their control evaluation and verification procedures.
+  **Monitoring** through security controls that AWS remains aligned with global standards and best practices.

## Resilience in the cloud
<a name="resilience-in-the-cloud"></a>

 AWS customers are responsible for their resilience in the cloud and assume the responsibility and management of the guest operating system (including updates and security patches) and other associated application software, in addition to applicable network security controls. Customers should carefully consider the services they choose because their responsibilities vary depending on the services used, the integration of those services into their IT environment, and applicable laws and regulations.

 It is important to note that when using AWS services, customers maintain control over their content and are responsible for managing critical content security requirements, including:
+  The content that they choose to store on AWS.
+  The AWS services that are used with the content.
+  The country and AWS Region where they store their content.
+  The format and structure of their content and whether it is masked, anonymized, or encrypted.
+  How their data is encrypted, and where the keys are stored.
+  Who has access to their content, and how those access rights are granted, managed, and revoked.

 AWS provides tools and information to assist customers assessing controls in their extended IT environment. For more information, see the [AWS Compliance Center](https://aws.amazon.com/compliance), [Amazon Web Services' Approach to Operational Resilience in the Financial Sector and Beyond](https://docs.aws.amazon.com/pdfs/whitepapers/latest/aws-operational-resilience/aws-operational-resilience.pdf#aws-operational-resilience), [Shared Responsibility Model for Resiliency](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/shared-responsibility-model-for-resiliency.html), and the [AWS Well Architected Framework](https://aws.amazon.com/architecture/well-architected/). Contact your AWS representative to discuss how the AWS FSI Compliance team, the AWS Partner Network, as well as AWS Solution Architects, and Professional Services teams can assist.
