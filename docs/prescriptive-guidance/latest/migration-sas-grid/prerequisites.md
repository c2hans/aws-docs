---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sas-grid/prerequisites.html
---

# Assumptions and prerequisites
<a name="prerequisites"></a>

To migrate SAS Grid to AWS, you must meet the assumptions and requirements discussed in this section. The migration of SAS software may require expert skills in SAS administration, system administration, and AWS administration. If you need help with determining the scope of migration for your SAS Grid environment, we recommend that you contact SAS professional services for the following assessments:
+ Current SAS Grid workload assessment
+ Security assessment
+ SAS Grid migration assessment
+ SAS Grid migration advisory service

## Migration requirements
<a name="migration-req"></a>

The physical topology of source and target systems must be equivalent, including host machines and their roles, with the expectation that RAM, CPU, and disk volume/throughput will compare similarly. Also, source and target operating systems must be in the same family. For SAS installation prerequisites, see [SAS system requirements ](https://support.sas.com/en/documentation/system-requirements.html)on the SAS website.
+ Source and target systems must be SAS 9.2 or later.
+ Data, files, and other content that isn't migrated automatically must be migrated manually.
+ This workload migration doesn't include original data providers. Rehosting original data on AWS, especially in a different data provider technology, requires additional effort.
+ For SAS Bring Your Own License (BYOL) migration, you must establish and maintain the AWS environment.

## Knowledge requirements
<a name="knowledge-req"></a>

A solid understanding of the SAS system and the components of SAS infrastructure is required to optimize your SAS Grid environment on AWS. Considerations such as storage service, server instance types, networking performance, high availability, and disaster recovery affect the architecture design of your SAS environment on AWS.

## Additional SAS considerations
<a name="additional"></a>
+ SAS infrastructure sizing and architecture must be created based on:
  + Instance types
  + Ephemeral, persistent, and shared storage types
  + A shared file system for SAS Grid Manager
  + Placement of SAS Permanent Data File Space (SASDATA) and temporary file spaces: SAS Working Data File Space (SASWORK) and SAS Utility Data File space (UTILLOC)
+ SAS software licensing metrics are the same for SAS software cloud and on-premises deployments.
+ Cloud administration, security, and monitoring are the responsibility of users, unless the environment has been contracted by SAS as part of a remotely managed environment.
+ SAS software can be scaled, but you must be careful to comply with licensing agreements.
+ In most cases, scaling a SAS infrastructure results in an outage of service during the process.
+ High availability, disaster recovery, and backup and restoration are as important in SAS software cloud deployments as they are in SAS software on-premises deployments.
+ Local laws and privacy regulations might affect the data you store in the cloud. For example, certain geographies might restrict the storage and processing of data in a cloud location out of country or state.
+ The cost of a cloud infrastructure is a core consideration.
