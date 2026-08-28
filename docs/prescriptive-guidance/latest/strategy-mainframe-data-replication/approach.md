---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-mainframe-data-replication/approach.html
---

# Strategic approach for mainframe data replication
<a name="approach"></a>

Data replication from a mainframe to the AWS Cloud is a process that involves transferring data from your on-premises mainframe systems to the cloud environment.

Throughout the process, relevant stakeholders, such as mainframe data owners, security teams, and cloud architects, must actively participate to make sure that the migration is successful and compliant. Additionally, for guidance and implementation support, consider engaging [AWS Professional Services](https://aws.amazon.com/professional-services/) or [AWS Partners](https://aws.amazon.com/partners/work-with-partners/) who have mainframe modernization expertise.

This section describes a high-level strategic approach that you can use to plan and implement a mainframe data replication. It includes the following phases:

1. [Assess](#approach-assess)

1. [Mobilize](#approach-mobilize)

1. [Migrate and modernize](#approach-migrate)

1. [Optimize](#approach-optimize)

1. [Govern](#approach-govern)

## Assess
<a name="approach-assess"></a>

The assess phase forms the foundational cornerstone of any successful mainframe-to-cloud data migration strategy. During this initial stage, you conduct a comprehensive evaluation of the current mainframe environment, carefully analyzing workloads, data characteristics, and infrastructure capabilities. This systematic assessment helps identify which datasets are candidates for cloud replication. Through this analysis, you can develop a clear understanding of the scope and potential challenges.

Do the following in the assess phase:

1. Evaluate your mainframe workloads and identify which datasets should be replicated to the AWS Cloud.

1. Conduct a thorough analysis of the data sensitivity, compliance requirements, and performance considerations.

1. Assess your existing network infrastructure and bandwidth availability for data replication.

## Mobilize
<a name="approach-mobilize"></a>

In the mobilize phase, you develop a comprehensive replication strategy that addresses three fundamental aspects: the technical architecture for integration between mainframe systems and AWS services, the operational framework for maintaining data consistency and security, and the establishment of clear success metrics. You must carefully consider various replication frequencies, synchronization methods, and failover mechanisms while designing an architecture that implements robust security controls.

Do the following in the mobilize phase:

1. Develop a detailed data replication strategy that includes the following:
   + **Frequency** – Determine the frequency of data replication based on your business requirements, data volatility, and network bandwidth availability. Frequency options include the following:
     + *Real-time replication* is the process of copying the data to the cloud as soon as its created. This option is ideal for transactional data, where minimal latency is required.
     + *Near real-time replication* is the process of copying the data to the cloud with a slight delay. This option is suitable for high-priority data, where moderate latency is tolerated.
     + *Scheduled batch replication* is the process of copying the data to the cloud at a scheduled time. This option is appropriate for non-real-time data, where periodic updates are sufficient.
   + **Synchronization methods** – Choose appropriate synchronization methods that promote data consistency and minimize replication overhead. Synchronization options include the following:
     + *Change data capture (CDC)* is the process of tracking changes to a data source and recording metadata about the change. With this approach, you capture and replicate only the changed data. This option can reduce replication traffic and improve efficiency.
     + *Snapshot replication* is the process of creating a copy of a dataset at a point in time and then replicating that copy. You can periodically take snapshots of your mainframe data and then replicate it to the AWS Cloud. This option is suitable for less dynamic datasets.
   + **Failover mechanisms** – Implement failover mechanisms that promote continuous availability and data integrity. Options for failover mechanisms include the following:
     + *Active-passive failover* is a configuration that uses primary and secondary resources. The secondary resource is activated only when the primary resource fails. With this approach, you maintain a standby replica in the AWS Cloud, and it is automatically activated if the mainframe fails.
     + *Active-active replication* is method of data replication that allows multiple servers to handle read and write operations simultaneously. With this approach, you simultaneously replicate the mainframe data to multiple AWS Regions in the cloud. This approach is suitable if you need high availability and disaster recovery.

1. Design an architecture for integrating mainframe systems with AWS services, and design for data consistency and security. Your architecture should address the following:
   + **Integration with AWS services** – We recommend that your design accounts for the following:
     + **Replication tool** – Use [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) or third-party replication tools.
     + **Storage** – Store replicated data in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) because it provides scalability and durability.
     + **Data warehousing** – Use [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html) for data warehousing and analytics. This service can help you extract insights from the replicated mainframe data.
     + **Compute** – Deploy [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions or [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instances to process the replicated data and perform data transformations.
   + **Data consistency and security** – We recommend that your design accounts for the following:
     + **Encryption** – Encrypt data both in transit and at rest by using [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html).
     + **Access control** – Implement [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) roles and policies that control access to the replicated data. Restrict permissions based on user roles and responsibilities.
     + **Data validation** – Perform checks during replication to validate data consistency and integrity between the mainframe and cloud environments.
     + **Monitoring and auditing** – Use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) for monitoring the replication processes and auditing access to the replicated data.

1. Establish clear metrics for measuring the success of the replication process and its impact on application performance. Metrics can include the following:
   + **Data completeness** – Monitor the completeness of the replicated data compared to the source so that you can detect any missing or incomplete records.
   + **Application performance** – Track application response times and throughput before and after implementing the data replication so that you can identify any performance impacts.
   + **Cost efficiency** – Evaluate the cost effectiveness of data replication and AWS Cloud usage so that you can compare it against the costs for the on-premises infrastructure.

## Migrate and modernize
<a name="approach-migrate"></a>

During the migrate and modernize phase, you replicate the data from the mainframe to the cloud and then validate the replication. This critical phase involves implementing appropriate replication methods, deploying essential tools, and establishing secure data pathways between the mainframe and cloud environments. You must carefully orchestrate the integration of traditional mainframe systems with modern cloud services while maintaining robust security measures and ensuring data integrity throughout the transition process. Success in this phase requires a balanced approach to technical implementation, security compliance, and thorough validation of replication processes.

Do the following in the migrate and modernize phase:

1. Choose a replication method. There are several approaches to replicate mainframe data to AWS, including CDC and scheduled batch replication.

1. Deploy the data replication tools and configure the replication workflows between the mainframe and the cloud. You might use services and tools such as [Apache Kafka](https://kafka.apache.org/), [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html), [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html), or [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html).

1. Implement necessary security measures, such as encryption and access controls, to protect the data while in transit or at rest.

1. Test replication processes thoroughly to validate data integrity and reliability.

## Optimize
<a name="approach-optimize"></a>

The optimize phase helps you fine-tune the replication processes to achieve peak efficiency. This phase focuses on establishing a balanced framework that ensures optimal performance, cost-effectiveness, and operational resilience while maintaining the flexibility to scale.

Do the following in the optimize phase:

1. Continuously monitor the performance of the data replication process and adjust the configuration parameters as needed.

1. Optimize your AWS resources to minimize costs while meeting performance requirements.

1. Implement robust monitoring and alerting mechanisms that help you promptly detect and address any issues.

1. Plan for scalability to accommodate future growth in data volumes or additional data sources.

## Govern
<a name="approach-govern"></a>

The govern phase establishes the critical framework for maintaining control, compliance, and accountability in data management operations. This phase implements essential policies and procedures that help safeguard data assets and help you adhere to regulatory requirements and industry standards. Through structured governance mechanisms, you can create a secure and compliant environment that helps protect sensitive information.

Do the following in the govern phase:

1. Establish governance policies and procedures for managing the data replication processes and AWS Cloud usage.

1. Validate compliance with regulatory requirements and industry standards, such as General Data Protection Regulation (GDPR) and Health Insurance Portability and Accountability Act (HIPAA).

1. Conduct regular audits and reviews to validate adherence to governance and compliance guidelines.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
