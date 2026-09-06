---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-microsoft-workloads-aws/migrating-windows-server-workloads.html
---

# Migrating Windows Server
<a name="migrating-windows-server-workloads"></a>

This section focuses on the different options available for migrating Windows Server to AWS.

## Assess
<a name="migrating-windows-server-workloads-assess"></a>

First, identify the applications and workloads that need to be migrated to AWS. You can use [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/) to create a map of your on-premises infrastructure and dependencies between applications. This helps you identify the servers, applications, and services that you need to migrate to AWS.

You can use [AWS Migration Hub](https://aws.amazon.com/migration-hub/) to create an inventory of your applications and evaluate their compatibility with AWS. Migration Hub provides a centralized view of your application portfolio and helps you plan, track, and manage your migration projects. You can also use third-party assessment tools that support AWS, such as Cloudamize or Evolve.

## Mobilize
<a name="migrating-windows-server-workloads-mobilize"></a>

It can be a significant challenge to find the right path for rehosting (lift and shift) large scale infrastructure. While there are numerous [best practices](https://aws.amazon.com/blogs/enterprise-strategy/21-best-practices-for-your-cloud-migration/) that are helpful, the choice of tool depends on multiple factors, such as workload type, affordable downtime, and operating system requirements. We recommend that you use [AWS Transform MGN](https://aws.amazon.com/application-migration-service/) to rehost.

### AWS Transform MGN
<a name="9999999999999999mgnlong-.afd2fff0-68ef-5496-ad4c-58bf43b9318a"></a>

You can use MGN to quickly lift and shift physical, virtual, or cloud servers without compatibility issues, performance impact, or long cutover windows. MGN continuously replicates your source servers to your AWS account. Then, when you're ready to migrate, MGN automatically converts and launches your servers on AWS with minimal downtime. For more information, see [What Is AWS Transform MGN?](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) in the MGN documentation.

### AWS Transform for VMware
<a name="9999999999999999trn--for-vmware.f93ef541-f1d2-520e-8f02-3f45095b1d03"></a>

[AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/what-is-service.html) simplifies and automates the migration of servers and enterprise applications to AWS by using AI-driven orchestration. It provides a single workspace to create, run, and track your migration jobs. [AWS Transform for VMware](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-vmware.html) combines automated discovery, intelligent wave planning, and rehosting capabilities to efficiently migrate workloads from VMware environments to Amazon EC2 with minimal disruption.

AWS Transform supports multiple migration job types, including:
+ **End-to-end migration** – Covers discovery, wave planning, VPC configuration, and server migration
+ **Network migration only** – Generates and deploys VPC network configurations
+ **Network-and-server migration** – Combines VPC setup with server rehosting
+ **Discovery and server migration** – Performs discovery, generates a wave plan, and migrates servers

AWS Transform uses AI-driven conversion of VMware network configurations to an Amazon VPC architecture, generates migration plans with application grouping and suggested migration waves, and automates the rehosting of Windows and Linux servers to run natively on Amazon EC2.

### VM Import/Export
<a name="9999999999999999vmielong-.87112c1e-6300-556d-ac9f-ae9e6924e118"></a>

[VM Import/Export](https://aws.amazon.com/ec2/vm-import/) enables you to import VM images from your existing virtualization environment to Amazon EC2, and then export them back. This enables you to migrate applications and workloads to Amazon EC2, copy your VM image catalog to Amazon EC2, or create a repository of VM images for backup and disaster recovery. For more information, see [What is VM Import/Export?](https://docs.aws.amazon.com/vm-import/latest/userguide/what-is-vmimport.html) in the Amazon EC2 documentation.

After assessing the workloads for migration, create a migration plan that outlines the migration strategy, timeline, and costs involved in the migration process. You can use [AWS Pricing/TCO Tools](https://docs.aws.amazon.com/whitepapers/latest/how-aws-pricing-works/aws-pricingtco-tools.html) to estimate the cost savings of running your applications on AWS.

## Migrate
<a name="migrating-windows-server-workloads-migrate"></a>

Migrating a Windows workload to AWS involves several phases, including the migration planning, readiness assessment, and migration implementation phases. The migrate phase is the last phase, which involves migrating the Windows workload to AWS. The following are some steps to consider during the migrate phase:
+ **Prepare the AWS environment** – Before you begin the migration process, you must prepare the AWS environment by creating an Amazon Machine Image (AMI) and setting up a VPC where you're migrating the workload.
+ **Select the migration tool** – There are various migration methods to choose from, including Migration Hub, MGN, and VM Import/Export. Choose the method that best suits your needs.
+ **Configure the migration** – Configure the migration by selecting the source server and specifying the target instance type, storage, and network settings.
+ **Perform the migration** – After the configuration is complete, perform the migration. The process involves replicating the data, testing the migrated workload, and performing final cutovers to switch over to the migrated workload. The migration tool you selected above will guide you through these steps.
+ **Validate the migration** – After the migration is complete, validate that the migrated workload is functioning as expected. Perform tests and ensure that the security and compliance requirements are met.
+ **Optimize the migrated workload **– Optimize the migrated workload by resizing the instance, configuring auto-scaling, and implementing cost-saving strategies such as Reserved Instances or Spot Instances.
+ **Monitor and manage the migrated workload** – Continuously monitor and manage the migrated workload to ensure optimal performance and security. You can use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) for monitoring.
