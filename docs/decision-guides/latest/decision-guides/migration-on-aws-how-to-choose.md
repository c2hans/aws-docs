---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/migration-on-aws-how-to-choose.html
---

# Choosing AWS migration services and tools
<a name="migration-on-aws-how-to-choose"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Purpose** | Help determine which AWS migration and transfer services are the best fit for your organization. |
| **Last updated** | October 16, 2025 |
| **Covered services** |  +  [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html) <br />+  [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) <br />+  [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html) <br />+  [Direct Connect](https://aws.amazon.com/directconnect/getting-started/) <br />+  [DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) <br />+  [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-getting-started.html) <br />+  [AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up.html) <br />+  [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/setting-up.html) <br />+  [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html)   |

## Introduction
<a name="intro"></a>

Migration and modernization in the Amazon Web Services (AWS) Cloud involves the process of relocating an organization's digital infrastructure, applications, and data to AWS. This shift allows you to not only modernize applications, but also use the range of scalable and secure cloud services and infrastructure offered by AWS to reduce reliance on physical hardware and optimize resource allocation.

The migration process typically begins with a comprehensive assessment of your existing IT assets and requirements, followed by strategic planning and architecture design to ensure an optimal transition. This may involve re-hosting, re-platforming, or re-architecting applications to best use AWS services.

Once you have a migration plan in place, data is transferred to AWS, and applications are deployed in the cloud environment. Post-migration, ongoing management, monitoring, and optimization are crucial to maximize benefits.

AWS offers a wide range of tools, resources, and support to help with this process, catering to diverse migration strategies, such as lift-and-shift, re-platforming, and refactoring. This guide is designed to help you choose the right tools and services to do your migration.

[![AWS Videos](http://img.youtube.com/vi/9FjxnEoH5wg?start=134&end=436/0.jpg)](http://www.youtube.com/watch?v=9FjxnEoH5wg?start=134&end=436)

## Understand
<a name="understand"></a>

Moving applications and data from on-premises infrastructure to AWS involves a strategic progression through key phases.

It starts with a phase of assessment and mobilization, where you [build a business case for migrating to the cloud](https://d1.awsstatic.com/AWS_Navigating_the_Cloud_Migration_and_Modernization_Executive_Guidance.pdf).

![Diagram showing AWS data migration services](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/migration-approach.png)

An assessment takes a snapshot of your current on-premises footprint to fine-tune licensing, view server and application dependencies, and deliver recommendations for migration and modernization scenarios.

In the mobilize phase, you’ll build a strategy for optimizing infrastructure selection, creating landing zones and establishing cloud best practices within your team to begin a migration.

Here's more detail on each of those phases.

**Assess and mobilize**

The first phase of migrating on-premises workloads to AWS involves assessing your existing infrastructure and understanding the specific requirements. You can use tools such as [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) to create an inventory of applications and dependencies, or request a free [migration assessment](https://pages.awscloud.com/GLOBAL-entstrategy-PT-AWS-Migration-Evaluator-Request-2023-interest.html) to build your business case. This initial step is crucial for formulating a comprehensive migration strategy. The [AWS Migration Acceleration Program (MAP)](https://aws.amazon.com/migration-acceleration-program/) can also help in the development of such a strategy.

**Migrating applications and databases**

In this phase, applications and databases are moved to AWS, and the migration strategy is executed. AWS provides services like MGN for large-scale application migration and [AWS Database Migration Service (AWS DMS)](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html) for seamless migration of databases. AWS Transform uses generative AI and agentic AI capabilities to automate, accelerate, and optimize the migration process. Transform orchestrates migration for VMware workloads, mainframes, and .NET applications. Organizations might choose to re-host (lift-and-shift) or re-architect applications for optimal performance in the cloud. The [AWS Serverless Application Model (AWS SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) aids in building serverless applications.

**Hybrid cloud storage**

To provide a smoother transition, you might choose to adopt a hybrid cloud storage approach during migration. [AWS Storage Gateway](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up.html) can be used to provide integration of on-premises environments with cloud storage, enabling a unified data management strategy. This hybrid model is designed to offer data accessibility and availability, and help minimize disruptions during the migration process.

**Online data transfer**

For continuous operations, online data transfer mechanisms play a pivotal role. [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html), for instance, enables efficient and secure transfer of large datasets between on-premises environments and AWS storage services. This ensures minimal downtime and maintains data integrity throughout the migration.

By navigating through these phases, you can realize the benefits of AWS, and make best use of the scalability, security, and services it provides, while minimizing disruptions to ongoing business operations.

## Consider
<a name="consider"></a>

In the domain of migration and transfer to AWS, organizations face a spectrum of challenges and concerns that AWS services are strategically designed to address. In the following, we will explore some of the criteria to consider for a timely, secure, and cost-effective migration to AWS.

------
#### [ Diverse migration scenarios ]

Migrating on-premises workloads to AWS demands a nuanced approach, primarily due to the diverse migration scenarios organizations encounter. These scenarios range from simple lift-and-shift migrations, where existing applications are moved with minimal changes, to more complex re-platforming or re-architecting, which involve optimizing applications for AWS services. Hybrid cloud deployments are another common scenario, allowing organizations to maintain on-premises infrastructure while leveraging AWS capabilities.

Organizations must assess their speciﬁc needs, balancing factors like downtime tolerance, cost-eﬃciency, and data integrity. Data sensitivity, compliance requirements, and industry regulations also inﬂuence migration strategies.

AWS offers a suite of tools and services to address this diversity, providing organizations with the flexibility to choose the most suitable migration approach for their unique circumstances. Navigating these diverse scenarios effectively ensures a successful transition to AWS, unlocking the full potential of cloud computing while aligning with organizational goals and constraints.

------
#### [ Minimizing downtime ]

Minimizing downtime is a critical consideration in migrating on-premises workloads to AWS, because any interruption in business operations can result in significant financial and operational setbacks. To achieve minimal downtime, organizations employ several strategies.

First, they often opt for gradual migration approaches, such as the lift-and-shift method, where existing workloads are moved to AWS with minimal modification. This minimizes downtime but might not fully leverage all of the capabilities AWS offers.

Second, implementing hybrid cloud solutions can maintain business continuity during migration. By keeping critical components on-premises while migrating non-essential workloads to AWS, companies can mitigate downtime risks.

Moreover, AWS offers tools like AWS DataSync and AWS Snowball to facilitate efficient data transfer, reducing the time data spends in transit during migration, thereby minimizing downtime.

Finally, thorough testing and validation of the migration plan are essential to identify potential issues before they impact production systems, ensuring a smoother transition with minimal disruption. Overall, minimizing downtime is a top priority in the migration process to AWS, enabling businesses to maintain operational efficiency throughout the migration journey.

------
#### [ Large data transfer challenges ]

Large data transfer poses a significant challenge in migrating on-premises workloads to AWS. When dealing with massive datasets, bandwidth limitations and time constraints become major concerns. AWS provides solutions to address these challenges.

For online data transfer, services like AWS DataSync employ optimized protocols to maximize data transfer speeds, reducing the time required to move data to the cloud. However, this method might be insufficient for extremely large datasets or environments with limited bandwidth.

Direct Connect provides a dedicated private network connection from your premises to AWS, offering consistent and high-bandwidth connectivity for large data transfers, especially when ongoing, high-volume data movement is required. For migrating databases, including large databases, AWS DMS can help.

Strategically combining these data transfer options helps organizations efficiently migrate large volumes of data to AWS while minimizing disruption to business operations and ensuring data integrity.

------
#### [ Database compatibility and heterogeneity ]

Database compatibility and heterogeneity present significant challenges during the migration of on-premises workloads to AWS. Organizations often rely on various database management systems, and ensuring seamless compatibility with AWS services is crucial.

To address these complexities, AWS offers tools like AWS Database Migration Service (AWS DMS) and DMS Schema Conversion (DMS SC). AWS DMS supports the migration of a wide range of databases to AWS, facilitating data replication with minimal downtime. DMS SC helps convert database schemas, ensuring that they are compatible with AWS database services, which can vary in structure and behavior.

Additionally, AWS provides managed database services like Amazon RDS and Amazon Aurora, which are compatible with popular database engines, simplifying the migration process.

Organizations must carefully assess their database landscape, plan for potential incompatibilities, and choose the right AWS database service or conversion approach to maintain data integrity and functionality during migration.

------
#### [ File transfer workloads ]

Migrating file transfer workloads from on-premises environments to AWS requires thoughtful planning to ensure seamless data movement and continuity of operations. File transfer workloads often involve large volumes of critical data, which necessitates a well-executed strategy.

AWS offers services like AWS Transfer Family, which includes AWS Transfer for SFTP and AWS Transfer for FTPS, allowing organizations to easily migrate and manage file transfer workloads securely in the cloud. These services provide compatibility with existing file transfer protocols, reducing migration complexities.

Organizations can also leverage AWS DataSync for efficient, high-speed data transfers. It helps synchronize on-premises file systems with AWS storage services, minimizing downtime and ensuring data consistency.

Furthermore, optimizing network connectivity and bandwidth is crucial for maintaining file transfer performance during migration. Direct Connect and [AWS VPN solutions](https://aws.amazon.com/vpn/) can help establish reliable connections between on-premises environments and AWS, addressing potential challenges related to latency and bandwidth limitations.

In summary, a well-structured plan, the right AWS services, and a focus on network optimization are key considerations to ensure a smooth migration of file transfer workloads to AWS, preserving data integrity and minimizing disruption.

------
#### [ Visibility and monitoring ]

Visibility and monitoring are crucial during migration to ensure a smooth transition of on- premises workloads to AWS.

AWS Transform plays a pivotal role in this regard by offering a centralized platform for tracking and managing the migration and modernization journey. This tool provides organizations with real-time insights into the progress of their migration projects, allowing them to identify any bottlenecks or issues promptly. It offers visibility into the health and performance of migrated resources, ensuring that applications run smoothly in the cloud environment.

Furthermore, AWS Transform enhances security by providing visibility into access control and auditing through AWS Identity and Access Management (IAM) and AWS CloudTrail. This ensures that security measures are maintained throughout the migration process.

In essence, AWS Transform empowers organizations to make informed decisions, optimize their migration strategy, and maintain the integrity of their workloads. Its role in enhancing visibility and monitoring is instrumental in achieving a successful and secure migration to AWS.

------
#### [ Application capability ]

It can be challenging to ensure that applications, especially legacy applications, are compatible with the cloud environment. Ensuring that existing applications seamlessly function within the AWS Cloud environment is essential for a smooth transition. This often involves assessing and, if necessary, modifying applications to align with AWS services and infrastructure. AWS Transform aids in this process.

Compatibility challenges can arise due to differences in operating systems, dependencies, or network configurations. Therefore, meticulous testing and validation are vital to identify and resolve any compatibility issues prior to migration. By addressing application compatibility proactively, organizations can minimize disruptions, maintain business continuity, and fully harness the benefits of the scalable and secure cloud infrastructure in AWS.

------
#### [ Dependency mapping ]

Dependency mapping, a crucial aspect of migrating on-premises workloads to AWS, involves identifying the intricate relationships and interdependencies between applications. These connections can be complex, encompassing data flows, service dependencies, and communication patterns.

AWS offers AWS Transform to assist in this process. This service automatically discovers, maps, and documents dependencies, providing organizations with a clear understanding of how different components interact.

By accurately mapping dependencies, organizations can make informed decisions about migration strategies, ensuring that all associated elements are moved together to maintain functionality. This reduces the risk of post-migration issues and helps organizations plan for the sequencing of migration activities, minimizing disruptions and downtime.

------
#### [ Performance optimization ]

Performance optimization is a vital consideration when migrating on-premises workloads to AWS. It involves assessing and enhancing the efficiency and speed of applications in the cloud environment. This process often starts with a thorough analysis of the existing application's performance characteristics, including resource utilization, latency, and scalability.

AWS provides various tools and services to aid in performance optimization, such as Amazon CloudWatch for monitoring, AWS Auto Scaling for dynamic resource allocation, and Elastic Load Balancing for distributing traffic. Additionally, AWS Trusted Advisor and AWS Compute Optimizer offer recommendations for cost optimization and performance improvement.

------
#### [ Security and compliance ]

Security and compliance are paramount when migrating on-premises workloads to AWS. Organizations must maintain data integrity, confidentiality, and compliance with industry regulations during and after migration. AWS offers a robust set of security services, including AWS Identity and Access Management (IAM), AWS Key Management Service (AWS KMS), and AWS Security Hub CSPM, to help organizations establish strong security postures.

Compliance with standards such as GDPR, HIPAA, and PCI DSS is simplified through AWS compliance programs and extensive documentation. AWS Artifact provides access to compliance reports, while AWS Config helps monitor and maintain compliance.

Furthermore, AWS provides tools like IAM and AWS Key Management Service (AWS KMS) for fine-grained control over access and encryption of data. To safeguard workloads during migration and beyond, it's essential to implement security best practices and conduct regular audits, ensuring a secure and compliant environment in AWS.

------
#### [ Testing and validation ]

Thorough testing is essential to validate that migrated applications function as expected in the new cloud environment. This includes performance testing, functionality testing, and security testing to identify and address any issues or discrepancies.

AWS offers a range of tools and services, such as AWS CodeBuild and AWS CodeDeploy, for automated testing and deployment of applications in the cloud.

Comprehensive testing and validation not only mitigate potential risks but also provide the confidence that the migrated workloads will perform as expected, minimizing disruptions and ensuring a successful transition to AWS. Regular testing and ongoing validation post-migration are also essential to adapt to changing business needs and maintain optimal performance and security.

------
#### [ Cost management ]

Managing costs effectively during and after migration is crucial for budget considerations. Organizations must carefully plan and optimize their cloud spending to maximize cost efficiency. AWS offers tools like AWS Cost Explorer and AWS Budgets to monitor and forecast expenses.

Cost management involves selecting the right AWS pricing models, such as On-Demand, Reserved Instances, or Savings Plans, based on workload usage patterns. Right-sizing resources and leveraging auto-scaling capabilities can help align costs with actual demand, avoiding overprovisioning.

Additionally, AWS Trusted Advisor and AWS Compute Optimizer provide recommendations for cost optimization, and AWS Cost Anomaly Detection can identify unusual spending patterns.

By proactively managing costs, organizations can harness the benefits of the scalability and flexibility in AWS while ensuring that their migration remains within budgetary constraints. Cost management is an ongoing process, and regular monitoring and adjustment are essential to control and optimize cloud expenditure over time.

------

## Choose
<a name="choose"></a>

Now that you have reviewed the key criteria to consider in your migration to AWS you are ready to start planning your migration and choosing the appropriate AWS services to assist in your migration. Here are some things to consider:
+ You must assess your existing infrastructure and create an inventory of assets to mobilize resources effectively.
+ Will you be choosing a lift-and-shift strategy, re-platforming (that is, on-premises database to Amazon RDS), or modernizing your workloads by re-architecting?
+ Will you operate in a hybrid mode, with some workloads remaining on-premises?
+ What are your data transfer needs?

The following table walks you through the relevant services on AWS that will help you to achieve a successful migration.

****

| Migration category | What is it optimized for? | Migration services |
| --- |--- |--- |
| Assess and mobilize | These services are optimized to accelerate decision-making and discover on-premises assets to plan your AWS migration. | [Experience-Based Acceleration (EBA)](https://aws.amazon.com/experience-based-acceleration/)<br />[AWS Migration Acceleration Program](https://aws.amazon.com/migration-acceleration-program/)<br />[Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/)<br />[AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) |
|  Migrate your applications  |  These services are optimized to simplify and expedite the migration on on-premises servers and databases to AWS.  |  [AWS Transform MGN](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html) [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) [DMS Schema Conversion](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SchemaConversion.html) [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html)  |
| --- |--- |--- |
| Hybrid cloud storage | These services are optimized for on-premises applications that require low-latency data access or rapid data transfer to the cloud. | [AWS Storage Gateway](https://docs.aws.amazon.com/storagegateway/)<br />[Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) |
|  Online data transfer  |  These services are optimized to make it simple and easy to transfer your data into and out of AWS via online methods.  |  [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/setting-up.html) [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html) [Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)  |
| --- |--- |--- |

## Use
<a name="use"></a>

To explore how to use and learn more about each of the available AWS migration and transfer services, we have provided a pathway to explore how each of the services work. The following sections provide links to in-depth documentation, hands-on tutorials, and resources to get you started.

------
#### [ AWS Transform ]
+  **What is AWS Transform?**

  This guide provides an overview of AWS Transform.

   [Explore the guide](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html)
+  **Getting started with AWS Transform for VMware migration**

  This guide will help you get started with migrating your VMware environment to Amazon EC2 with AWS Transform.

   [Read the guide](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware.html)
+  **Modernize your mainframe applications with AWS Transform**

  This guide will help you modernize your mainframe applications with AWS Transform.

   [Read the guide](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe.html)
+  **Modernize your .NET applications with AWS Transform**

  This guide will help you modernize your .NET applications with AWS Transform.

   [Read the guide](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html)

------
#### [ AWS Transform MGN ]
+  **Introduction to AWS Transform MGN**

  This short video (1:35) gives a brief introduction to AWS Transform MGN

   [Watch the video](https://www.youtube.com/watch?v=KVV5Hd70Uc8)
+  **Getting started with AWS Transform MGN**

  This guide will help you get started with MGN including how to use it with AWS Migration Hub.

   [Explore the guide](https://docs.aws.amazon.com/mgn/latest/ug/getting-started.html)
+  **How to use AWS Transform MGN for lift-and-shift migrations**

  This blog posts shows you how to simplify your lift-and-shift migration using AWS Transform MGN.

   [Read the blog post](https://aws.amazon.com/blogs/aws/how-to-use-the-new-aws-application-migration-service-for-lift-and-shift-migrations/)
+  **Automate setup of AWS Transform MGN and Elastic Disaster Recovery**

  This blog post discusses how to combine AWS Transform MGN and AWS Elastic Disaster Recovery Service to increase the resilience of your migrated workloads.

   [Read the blog post](https://aws.amazon.com/blogs/mt/automate-setup-of-aws-application-migration-service-and-elastic-disaster-recovery/)
+  **AWS Transform MGN best practices**

  This blog post shares best practices for accelerating and successfully implementing your migration using a highly automated list-and-shift solution, AWS Transform MGN.

   [Read the blog post](https://aws.amazon.com/blogs/mt/aws-application-migration-service-best-practices/)

------
#### [ AWS Database Migration Service ]
+  **Getting started with AWS Database Migration Service**

  In this guide, you will learn how to perform a database migration with AWS DMS.

   [Explore the guide](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_GettingStarted.html)
+  **Getting started with DMS Schema Conversion**

  In this tutorial, you will learn how to set up DMS Schema Conversion, create a migration project, and connect to your data providers.

   [Explore the guide](https://docs.aws.amazon.com/dms/latest/userguide/getting-started.html)
+  **Database migration step-by-step walkthroughs**

  In this guide, you can find step-by-step walkthroughs that go through the process of schema conversion and data migration for eight different source databases supported by AWS Database Migration Service.

   [Explore the guide](https://docs.aws.amazon.com/dms/latest/sbs/dms-sbs-welcome.html)
+  **How to migrate from Oracle to Amazon Aurora**

  In this hands-on lesson, you will migrate a legacy Oracle database to a cloud-native database with Amazon Aurora.

   [Start the lesson](https://aws.amazon.com/tutorials/break-free-from-legacy-databases/migrate-oracle-to-amazon-aurora/)

------
#### [ AWS DataSync ]
+  **Getting started with AWS DataSync**

  This guide focuses on getting started with DataSync using the AWS Management Console.

   [Explore the guide](https://docs.aws.amazon.com/datasync/latest/userguide/getting-started.html)
+  **Tutorial: Transferring data from on-premises storage to Amazon S3 in a different AWS account**

  In this tutorial, you will learn how to transfer data to from on-premises storage to an S3 bucket in a different account from the DataSync agent.

   [Start the tutorial](https://docs.aws.amazon.com/datasync/latest/userguide/s3-cross-account-transfer.html)
+  **Tutorial: Transferring data from Amazon S3 to Amazon S3 in a different AWS account**

  In this tutorial, you will learn how to use DataSync to transfer data from an S3 bucket in one account to another S3 bucket in a different account.

   [Start the tutorial](https://docs.aws.amazon.com/datasync/latest/userguide/tutorial_s3-s3-cross-account-transfer.html)

------
#### [ Direct Connect ]
+  **Using the Direct Connect Resiliency Toolkit to get started**

  This guide discusses how to use the Direct Connect Resiliency Toolkit to help you determine and then place your order for the number of dedicated connections to achieve your SLA objective.

   [Read the guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html)
+  **Continuous on-premises data migration with Direct Connect**

  This guide discusses using Direct Connect as part of an on-going data migration in a hybrid cloud deployment.

   [Read the guide](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-data-migration-services/use-case-2-continuous-on-premises-data-migration.html)
+  **Working with Direct Connect Gateways**

  This guide shows how to use Direct Connect gateways to connect your VPCs using either a transit gateway or a virtual private gateway.

   [Read the guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways-intro.html)

------

------
#### [ Amazon S3 Transfer Acceleration ]
+  **Getting started with Amazon S3 Transfer Acceleration**

  This guide will demonstrate how to get started with Amazon S3 Transfer Acceleration.

   [Explore the guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration-getting-started.html)
+  **Amazon S3 Transfer Acceleration speed comparison tool**

  This guide will demonstrate how to enable Transfer Acceleration on an S3 bucket and transfer data to and from the acceleration-enabled bucket.

   [Explore the guide](https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html)
+  **Uploading large objects to Amazon S3 using multipart upload and transfer acceleration**

  This tool allows you to compare the speed of multi-part file uploads for various Amazon S3 regions with and without the use of Amazon S3 Transfer Acceleration.

   [Go to the tool](https://aws.amazon.com/blogs/compute/uploading-large-objects-to-amazon-s3-using-multipart-upload-and-transfer-acceleration/)

------
#### [ DMS Schema Conversion ]
+  **Getting started with DMS Schema Conversion**

  This guide provides instructions for setting up DMS Schema Conversion.

   [Get started with the tutorial](https://docs.aws.amazon.com/dms/latest/userguide/getting-started.html)

------
#### [ AWS Storage Gateway ]
+  **Getting started with AWS Storage Gateway (Amazon S3 File Gateway)**

  This guide provides instructions for setting up S3 File Gateway and accessing it with Storage Gateway.

   [Get started with the tutorial](https://docs.aws.amazon.com/filegateway/latest/files3/setting-up.html)
+  **Getting started with AWS Storage Gateway (Amazon FSx File Gateway) **

  This guide provides instructions for setting up FSx File Gateway and accessing it with Storage Gateway.

   [Get started with the tutorial](https://docs.aws.amazon.com/filegateway/latest/filefsxw/setting-up.html)
+  **Data migration and cost saving at scale with Amazon S3 File Gateway**

  This blog walks through how Amazon S3 File Gateway helps migrate your data to the cloud while keeping metadata attributes intact, optimizing storage cost, and providing access to data in the cloud from on-premises application using standard SMB (Server Message Block) and NFS (Network File System) file protocols.

   [Read the blog post](https://aws.amazon.com/blogs/storage/data-migrations-at-scale-with-amazon-s3-file-gateway/)

------
#### [ AWS Transfer Family ]
+  **What is AWS Transfer Family? **

  This guide provides an overview of the Transfer Family service.

   [Read the guide](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)
+  **Tutorial: Getting started with AWS Transfer Family server endpoints**

  Use this tutorial to get started with Transfer Family. You'll learn how to create an SFTP-enabled server with a publicly accessible endpoint using Amazon S3 storage, add a user with service-managed authentication, and transfer a file with Cyberduck.

   [Get started with the tutorial](https://docs.aws.amazon.com/transfer/latest/userguide/getting-started.html)
+  **Tutorial: Setting up a managed workflow for decrypting a file**

  This tutorial illustrates how to set up a managed workflow that contains a decrypt step. The tutorial also shows how to upload an encrypted file to an Amazon S3 bucket and then view the decrypted file in that same bucket.

   [Get started with the tutorial](https://docs.aws.amazon.com/transfer/latest/userguide/workflow-decrypt-tutorial.html)

------

## Explore
<a name="explore"></a>
+ **Architecture diagrams**

  Explore reference architecture diagrams to help you develop your migration and transfer solutions on AWS.

  [Explore architecture diagrams](https://aws.amazon.com/architecture/migration/?achp_navtc11&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&ams%23interactive-card-vertical%23pattern-data-398312969.filter=%257B%2522filters%2522%253A%255B%257B%2522id%2522%253A%2522GLOBAL%2523local-tags-content-type.and%2522%252C%2522value%2522%253A%255B%2522reference-arch-diagram%2522%255D%257D%255D%257D)
+ **Whitepapers**

  Explore whitepapers to help you get started, learn best practices, and understand your migration and transfer options.

  [Explore whitepapers ](https://aws.amazon.com/architecture/migration/?achp_navtc11&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all&ams%23interactive-card-vertical%23pattern-data-398312969.filter=%257B%2522filters%2522%253A%255B%257B%2522id%2522%253A%2522GLOBAL%2523local-tags-content-type.and%2522%252C%2522value%2522%253A%255B%2522whitepaper%2522%255D%257D%255D%257D)
+ **Videos, patterns, AWS Solutions, and guidance**

  Explore additional architectural guidance for common use cases for migration and transfer services.

  [Explore additional assets](https://aws.amazon.com/architecture/migration/?achp_navtc11&cards-all.sort-by=item.additionalFields.sortDate&cards-all.sort-order=desc&awsf.content-type=*all&awsf.methodology=*all)
