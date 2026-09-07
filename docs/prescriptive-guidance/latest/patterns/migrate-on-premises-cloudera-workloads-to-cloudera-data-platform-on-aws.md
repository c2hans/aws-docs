---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws.html
---

# Migrate on-premises Cloudera workloads to Cloudera Data Platform on AWS
<a name="migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws"></a>

*Battulga Purevragchaa and Nidhi Gupta, Amazon Web Services*

*Nijjwol Lamsal, Cloudera, Inc.*

## Summary
<a name="migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws-summary"></a>

This pattern describes the high-level steps for migrating your on-premises Cloudera Distributed Hadoop (CDH), Hortonworks Data Platform (HDP), and Cloudera Data Platform (CDP) workloads to CDP Public Cloud on AWS. We recommend that you partner with Cloudera Professional Services and a systems integrator (SI) to implement these steps.

There are many reasons Cloudera customers want to move their on-premises CDH, HDP, and CDP workloads to the cloud. Some typical reasons include:
+ Streamline adoption of new data platform paradigms such as data lakehouse or data mesh
+ Increase business agility, democratize access and inference on existing data assets
+ Lower the total cost of ownership (TCO)
+ Enhance workload elasticity
+ Enable greater scalability; drastically reduce time to provision data services compared with legacy, on-premises install base
+ Retire legacy hardware; significantly reduce hardware refresh cycles
+ Take advantage of pay-as-you-go pricing, which is extended to Cloudera workloads on AWS with the Cloudera licensing model (CCU)
+ Take advantage of faster deployment and improved integration with continuous integration and continuous delivery (CI/CD) platforms
+ Use a single unified platform (CDP) for multiple workloads

Cloudera supports all major workloads, including Machine Learning, Data Engineering, Data Warehouse, Operational Database, Stream Processing (CSP), and data security and governance. Cloudera has offered these workloads for many years on premises, and you can migrate these workloads to the AWS Cloud by using CDP Public Cloud with Workload Manager and Replication Manager.

Cloudera Shared Data Experience (SDX) provides a shared metadata catalog across these workloads to facilitate consistent data management and operations. SDX also includes comprehensive, granular security to protect against threats, and unified governance for audit and search capabilities for compliance with standards such as Payment Card Industry Data Security Standard (PCI DSS) and GDPR.

**CDP migration at a glance**

|  |  |
| --- |--- |
|    Workload | Source workload | CDH, HDP, and CDP Private Cloud |
| --- |--- |--- |
| Source environment | + Windows, Linux<br />+ On-premises, colocation, or any non-AWS environment |
| Destination workload | CDP Public Cloud on AWS |
| Destination environment | + Deployment model: customer account<br />+ Operating model: customer/Cloudera control plane |
| ** **<br />** **<br />**Migration** | Migration strategy (7Rs) | Rehost, replatform, or refactor |
| Is this an upgrade in the workload version? | Yes |
| Migration duration | + Deployment: About 1 week to create customer account, virtual private cloud (VPC), and CDP Public Cloud customer-managed environment.<br />+ Migration duration: 1-4 months, depending on the complexity and size of the workload. |
| **Cost** | Cost of running the workload on AWS | + At a high level, the cost of a CDH workload migration to AWS assumes that you will establish a new environment on AWS. It includes accounting for personnel time and effort as well as provisioning computing resources and licensing software for the new environment.<br />+ The Cloudera cloud consumption-based pricing model gives you the flexibility to take advantage of bursting and automatic scaling capabilities. For more information, see [CDP Public Cloud service rates](https://www.cloudera.com/products/pricing/cdp-public-cloud-service-rates.html) on the Cloudera website.<br />+ Cloudera Enterprise [Data Hub](https://www.cloudera.com/products/enterprise-data-hub.html) is based on Amazon Elastic Compute Cloud (Amazon EC2) and closely models traditional clusters. Data Hub can be [customized](https://docs.cloudera.com/data-hub/cloud/create-cluster-aws/topics/mc-creating-a-cluster.html), but this will affect costs.<br />+ [CDP Public Cloud Data Warehouse](https://docs.cloudera.com/data-warehouse/cloud/index.html), [Cloudera Machine Learning](https://docs.cloudera.com/machine-learning/cloud/product/topics/ml-product-overview.html), and [Cloudera Data Engineering (CDE)](https://docs.cloudera.com/data-engineering/cloud/index.html) are container-based and can be configured to scale automatically. |
| ** **<br />** **<br />**Infrastructure agreements and framework** | System requirements | See the [Prerequisites](#migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws-prereqs) section. |
| SLA | See [Cloudera Service Level Agreement for CDP Public Cloud.](https://www.cloudera.com/legal/terms-and-conditions/cdp-public-cloud-sla.html) |
| DR | See [Disaster Recovery](https://docs.cloudera.com/cdp-reference-architectures/latest/cdp-ra-operations/topics/cdp-ra-abstract.html) in the Cloudera documentation. |
| Licensing and operating model (for target AWS account) | Bring Your Own License (BYOL) model |
| ** **<br />**Compliance** | Security requirements | See [Cloudera Security Overview](https://docs.cloudera.com/cdp-private-cloud-base/7.1.6/security-overview/topics/cm-security-overview.html) in the Cloudera documentation. |
| Other [compliance certifications](https://aws.amazon.com/compliance/programs) | See the information on the Cloudera website about [General Data Protection Regulation (GDPR](https://www.cloudera.com/solutions/lower-business-risks/general-data-protection-regulation.html)) compliance and the [CDP Trust Center](https://www.cloudera.com/products/trust-center.html). |

## Prerequisites and limitations
<a name="migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws-prereqs"></a>

**Prerequisites**
+ [AWS account requirements](https://docs.cloudera.com/cdp-public-cloud/cloud/requirements-aws/topics/mc-requirements-aws.html), including accounts, resources, services, and permissions, such as AWS Identity and Access Management (IAM) roles and policies setup
+ [Prerequisites for deploying CDP](https://docs.cloudera.com/cdp-public-cloud/cloud/getting-started/topics/cdp-set_up_cdp_prerequisites.html) from the Cloudera website

The migration requires the following roles and expertise:

|
|
| Role | Skills and responsibilities |
| --- |--- |
| Migration lead | Ensures executive support, team collaboration, planning, implementation, and assessment |
| Cloudera SME | Expert skills in CDH, HDP, and CDP administration, system administration, and architecture |
| AWS architect | Skills in AWS services, networking, security, and architectures |

## Architecture
<a name="migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws-architecture"></a>

Building to the appropriate architecture is a critical step to ensure that migration and performance meet your expectations. For your migration effort to meet this playbook’s assumptions, your target data environment in the AWS Cloud, either on virtual private cloud (VPC) hosted instances or CDP, must be an equivalent match to your source environment in terms of operating system and software versions as well as major machine specifications.

The following diagram (reproduced with permission from the [Cloudera Shared Data Experience data sheet](https://www.cloudera.com/content/dam/www/marketing/resources/datasheets/cloudera-sdx-datasheet.pdf?daqp=true)) shows the infrastructure components for the CDP environment and how the tiers or infrastructure components interact.

![CDP environment components](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bb47435e-2638-425c-ac37-7d55053452ac/images/91d62277-7fde-4ec6-8e2b-86a446e2f6ee.png)

The architecture includes the following CDP components:
+ Data Hub is a service for launching and managing workload clusters powered by Cloudera Runtime. You can use the cluster definitions in Data Hub to provision and access workload clusters for custom use cases and define custom cluster configurations. For more information, see the [Cloudera website](https://docs.cloudera.com/data-hub/cloud/index.html).
+ Data Flow and Streaming addresses the key challenges enterprises face with data in motion. It manages the following:
  + Processing real-time data streaming at high volume and high scale
  + Tracking data provenance and lineage of streaming data
  + Managing and monitoring edge applications and streaming sources

  For more information, see [Cloudera DataFlow](https://www.cloudera.com/products/dataflow.html) and [CSP](https://www.cloudera.com/products/stream-processing.html) on the Cloudera website.
+ Data Engineering includes data integration, data quality, and data governance, which help organizations build and maintain data pipelines and workflows. For more information, see the [Cloudera website](https://docs.cloudera.com/data-engineering/cloud/index.html). Learn about [support for spot instances to facilitate cost savings on AWS](https://docs.cloudera.com/data-engineering/cloud/cost-management/topics/cde-spot-instances.html) for Cloudera Data Engineering workloads.
+ Data Warehouse** **enables you to create independent data warehouses and data marts that automatically scale to meet workload demands. This service provides isolated compute instances and automated optimization for each data warehouse and data mart, and helps you save costs while meeting SLAs. For more information, see the [Cloudera website](https://docs.cloudera.com/data-warehouse/cloud/index.html). Learn about [managing costs](https://docs.cloudera.com/data-warehouse/cloud/planning/topics/dw-manage-cloud-costs.html) and [auto-scaling](https://docs.cloudera.com/data-warehouse/cloud/auto-scaling/topics/dw-public-cloud-autoscaling-overview.html) for Cloudera Data Warehouse on AWS.
+ Operational Database in CDP provides a reliable and flexible foundation for scalable, high-performance applications. It delivers a real-time, always available, scalable database that serves traditional structured data alongside new, unstructured data within a unified operational and warehousing platform. For more information, see the [Cloudera website](https://www.cloudera.com/products/operational-db.html).
+ Machine Learning is a cloud-native machine learning platform that merges self-service data science and data engineering capabilities into a single, portable service within an enterprise data cloud. It enables scalable deployment of machine learning and artificial intelligence (AI) on data anywhere. For more information, see the [Cloudera website](https://docs.cloudera.com/machine-learning/cloud/index.html).

**CDP on AWS**

The following diagram (adapted with permission from the Cloudera website) shows the high-level architecture of CDP on AWS. CDP implements its [own security model](https://docs.cloudera.com/runtime/7.1.0/cdp-security-overview/topics/security-management-console-security.html) to manage both accounts and data flow. These are integrated with [IAM](https://aws.amazon.com/iam/) through the use of [cross-account roles](https://docs.cloudera.com/cdp-public-cloud/cloud/requirements-aws/topics/mc-aws-req-credential.html).

![CDP on AWS high-level architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bb47435e-2638-425c-ac37-7d55053452ac/images/54420517-38b4-4e82-bd19-9ded50ed009c.png)

The CDP control plane resides in a Cloudera master account in its own VPC. Each customer account has its own sub-account and unique VPC. Cross-account IAM roles and SSL technologies route management traffic to and from the control plane to customer services that reside on internet-routable public subnets within each customer VPC. On the customer’s VPC, the Cloudera Shared Data Experience (SDX) provides enterprise-strength security with unified governance and compliance so you can get insights from your data faster. SDX is a design philosophy incorporated into all Cloudera products. For more information about [SDX](https://docs.cloudera.com/cdp-public-cloud/cloud/overview/topics/cdp-services.html) and the [CDP Public Cloud network architecture for AWS](https://docs.cloudera.com/cdp-public-cloud/cloud/aws-refarch/topics/cdp-pc-aws-refarch-overview.html), see the Cloudera documentation.

## Tools
<a name="migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Relational Database Service (Amazon RDS)](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) helps you set up, operate, and scale a relational database in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Automation and tooling**
+ For additional tooling, you can use [Cloudera Backup Data Recovery (BDR)](https://docs.cloudera.com/documentation/enterprise/6/6.3/topics/cm_bdr_tutorials.html), [AWS Snowball](https://aws.amazon.com/snowball/), and [AWS Snowmobile](https://aws.amazon.com/snowmobile/) to help migrate data from on-premises CDH, HDP, and CDP to AWS-hosted CDP.
+ For new deployments, we recommend that you use the [AWS Partner Solution for CDP](https://aws.amazon.com/solutions/partners/terraform-modules/cdp-public-cloud/).

## Epics
<a name="migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws-epics"></a>

### Prepare for migration
<a name="prepare-for-migration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Engage the Cloudera team. | Cloudera pursues a standardized engagement model with its customers and can work with your systems integrator (SI) to promote the same approach. Contact the Cloudera customer team so they can provide guidance and the necessary technical resources to get the project started. Contacting the Cloudera team ensures that all necessary teams can prepare for the migration as its date approaches. <br />You can contact Cloudera Professional Services to move your Cloudera deployment from pilot to production quickly, at lower cost, and with peak performance. For a complete list of offerings, see the [Cloudera website](https://www.cloudera.com/about/services-and-support/professional-services.html). | Migration lead |
| Create a CDP Public Cloud environment on AWS for your VPC. | Work with Cloudera Professional Services or your SI to plan and deploy CDP Public Cloud into a VPC on AWS. | Cloud architect, Cloudera SME |
| Prioritize and assess workloads for migration. | Evaluate all your on-premises workloads to determine the workloads that are the easiest to migrate. Applications that aren’t mission-critical are the best to move first, because they will have minimal impact on your customers. Save the mission-critical workloads for last, after you successfully migrate other workloads.Transient (CDP Data Engineering) workloads are easier to migrate than persistent (CDP Data Warehouse) workloads. It’s also important to consider data volume and locations when migrating. Challenges can include replicating data continuously from an on-premises environment to the cloud, and changing the data ingestion pipelines to import data directly to the cloud. | Migration lead |
| Discuss CDH, HDP, CDP, and legacy application migration activities. | Consider and start planning for the following activities with Cloudera Workload Manager:+ Data and workloads to copy to your AWS environment<br />+ Cloud-ready data<br />+ Noisy neighbors, which use up resources and create issues for other tenants<br />+ Elastic workloads<br />+ Small clusters with high operational overhead | Migration lead |
| Complete the Cloudera Replication Manager requirements and recommendations. | Work with Cloudera Professional Services  and your SI to prepare to migrate workloads to your CDP Public Cloud environment on AWS. Understanding the following requirements and recommendations can help you avoid common issues during and after you install the Replication Manager service.+ Review Replication Manager supporting documents to confirm that you meet the environment and system requirements. For more information, see [Support matrix for CDP Public Cloud Replication Manager](https://docs.cloudera.com/replication-manager/cloud/operations/topics/rm-product-compatibility-matrix.html) on the Cloudera website.<br />+ You don’t need root access to the nodes on which the Replication Manager App and Data Lifecycle Manager (DLM) engine will be installed.<br />+ Install Apache Hive during the initial installation of Replication Manager, unless you are certain that you won’t use Hive replication in the future. If you decide to install Hive after creating HDFS replication policies in Replication Manager, you have to delete and then recreate all HDFS replication policies after you add Hive.<br />+ Clusters used in Replication Manager must have symmetrical configurations. Each cluster in a replication relationship must be configured exactly the same for security (Kerberos), user management (LDAP/AD), and Knox Proxy. Cluster services such as Hadoop Distributed File System (HDFS), Apache Hive, Apache Knox, Apache Ranger, and Apache Atlas can have different configurations for high availability (HA). For example, source and target clusters might have separate HA and non-HA configurations. | Migration lead |

### Migrate CDP to AWS
<a name="migrate-cdp-to-aws"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Migrate the first workload for dev/test environments by using Cloudera Workload Manager. | Your SI can help you migrate your first workload to the AWS Cloud. This should be an application that isn’t customer-facing or mission-critical. Ideal candidates for dev/test migration are applications that have data that the cloud can easily ingest, such as CDP Data Engineering workloads. This is a transient workload that usually has fewer users accessing it, compared with a persistent workload such as a CDP Data Warehouse workload that could have many users who need uninterrupted access. Data Engineering workloads aren’t persistent, which minimizes the business impact if something goes wrong. However, these jobs could be critical for production reporting, so prioritize low-impact Data Engineering workloads first. | Migration lead |
| Repeat migration steps as necessary. | Cloudera Workload Manager helps identify workloads that are best suited for the cloud. It provides metrics such as cloud performance ratings, sizing/capacity plans for the target environment, and replication plans. The best candidates for migration are seasonal workloads, ad hoc reporting, and intermittent jobs that don’t consume many resources.<br />Cloudera Replication Manager moves data from on premises to the cloud, and from the cloud to on premises.<br />Proactively optimize workloads, applications, performance, and infrastructure capacity for data warehousing, data engineering, and machine learning by using Workload Manager. For a complete guide on how to modernize a data warehouse, see the [Cloudera website](https://www.cloudera.com/content/dam/www/marketing/resources/webinars/modern-data-warehouse-fundamentals.png.landing.html). | Cloudera SME |

## Related resources
<a name="migrate-on-premises-cloudera-workloads-to-cloudera-data-platform-on-aws-resources"></a>

Cloudera documentation:
+ [Registering classic clusters with CDP, Cloudera Manager, and Replication Manager:](https://docs.cloudera.com/replication-manager/cloud/operations/topics/rm-requirements-for-bdr-cdh-clusters.html)
  + [Management Console](https://docs.cloudera.com/management-console/cloud/overview/topics/mc-management-console.html)
  + [Replication Manager hive replication](https://docs.cloudera.com/replication-manager/cloud/core-concepts/topics/rm-replication-of-data-using-hive.html)
+ [Sentry replication](https://docs.cloudera.com/replication-manager/cloud/core-concepts/topics/rm-sentry-policy-replication.html)
+ [Sentry permissions](https://docs.cloudera.com/replication-manager/cloud/core-concepts/topics/rm-sentry-ranger-permissions.html)
+ [Data Hub cluster planning checklist](https://docs.cloudera.com/data-hub/cloud/cluster-planning/topics/dh-cluster-checklist.html)
+ [Workload Manager architecture](https://docs.cloudera.com/workload-manager/cloud/configuration/topics/wm-public-architecture-wm.html)
+ [Replication Manager requirements](https://docs.cloudera.com/replication-manager/cloud/index.html)
+ [Cloudera Data Platform Observability](https://www.cloudera.com/products/observability.html)
+ [AWS requirements](https://docs.cloudera.com/cdp-public-cloud/cloud/requirements-aws/topics/mc-requirements-aws.html)

AWS documentation:
+ [Cloud Data Migration](https://aws.amazon.com/cloud-data-migration/)
