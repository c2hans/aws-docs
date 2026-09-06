---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/introduction.html
---

# Migrate workloads to the AWS Cloud by using CloudEndure Migration
<a name="introduction"></a>

*Chandra Sekhar Yaratha and Harnath Valeti, Amazon Web Services*

*Chandra Sekhar Yaratha and Harnath Valeti, Consultants, AWS Professional Services *

*November 2020 (*[*last update*](doc-history.md)*: January 2021)*

This guide describes the process for migrating applications from a physical, virtual, or cloud-based infrastructure to the Amazon Web Services (AWS) Cloud by using CloudEndure Migration. It includes best practices and troubleshooting tips, which are also covered in the following video.

CloudEndure Migration is an agent-based tool that rehosts your applications on AWS. It supports self-service, highly automated, lift-and-shift migrations with minimal business disruption. You install the CloudEndure Agent on your source machines. The Agent replicates your applications and data in a staging area on AWS. After the initial replication, the CloudEndure Agent tracks and migrates changes from your source environment to the target staging area by using asynchronous, block-level data replication, without causing downtime or affecting performance.

You can use CloudEndure's self-service, web-based console to configure your target environment, to check for compability issues, and to validate that your applications are fully operational on AWS before you cut over. After you rehost your workloads on AWS, you can restructure, rewrite, and re-architect your applications and take advantage of AWS services.

CloudEndure Migration supports both Microsoft Windows and Linux-based workloads (see [supported versions](https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Supported_Operating_Systems/Supported_Operating_Systems.htm)). For more information, see the [CloudEndure Migration website](https://aws.amazon.com/cloudendure-migration/).

This guide is for project managers, system administrators, and migration architects who are planning to migrate their workloads to AWS. It describes the migration process, including preparing your source and target environments, configuring network settings, migrating your workloads, testing, and cutting over. If you're planning a large-scale migration that involves  rehosting thousands of servers, you can further automate tasks by using CloudEndure Migration Factory (CEMF).

**Note**
[ AWS Application Migration Service (MGN)](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) is the primary migration service recommended for lift-and-shift migrations to the AWS Cloud. Customers who currently use CloudEndure Migration or AWS Server Migration Service (AWS SMS) are encouraged to switch to MGN for future migrations.
