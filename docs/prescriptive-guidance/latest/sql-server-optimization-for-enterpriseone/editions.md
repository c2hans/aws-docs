---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/sql-server-optimization-for-enterpriseone/editions.html
---

# SQL Server editions
<a name="editions"></a>

Most users are able to leverage SQL Server Standard edition to meet the business requirements of their production systems and SQL Server Developer edition for their non-production environments. SQL Server Enterprise edition tends to be infrequently used for EnterpriseOne because of its high costs and because Microsoft moves features from Enterprise edition to Standard edition with each release. Many of the features that EnterpriseOne typically uses have been moved to SQL Server Standard edition, including the following:
+ Maximum memory was increased to 128 GB in SQL Server 2012.
+ Basic Always On availability groups for single databases were made available in SQL Server 2016.
+ Database compression was made available in SQL Server 2016 SP1.
+ BPEs became available in SQL Server 2017.
+ Transparent data encryption became available in SQL Server 2019.

However, some features are available only in Enterprise edition. These include:
+ Online index operations
+ Using more than 128 GB of RAM per database instance
+ Using more than 24 cores
+ Resource Governor to manage workload and system resource consumption
+ Read-ahead operations

Most EnterpriseOne users can take advantage of other solutions to meet their business requirements without using these Enterprise edition features.
