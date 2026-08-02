---
source_url: https://docs.aws.amazon.com/whitepapers/latest/data-warehousing-on-aws/tools-and-additional-help-for-database-migration.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Tools and additional help for database migration
<a name="tools-and-additional-help-for-database-migration"></a>

 Several tools and technologies for data migration are available. You can use some of these tools interchangeably, or you can use other third-party or open-source tools available in the market.
+  [AWS Database Migration Service](https://aws.amazon.com/dms/) supports both the one-step and the two-step migration processes. To follow the two-step migration process, you enable supplemental logging to capture changes to the source system. You can enable supplemental logging at the table or database level.
+  [AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/) (SCT) is a free tool that can convert the source database schema and a majority of the database code objects, including views, stored procedures, and functions, to a format compatible with the target databases. SCT can scan your application source code for embedded SQL statements and convert them as part of a database schema conversion project. After schema conversion is complete, SCT can help migrate a range of data warehouses to Amazon Redshift using built-in data migration agents.
+  Additional data integration partner tools include:
  +  [Informatica](https://www.informatica.com/)
  +  [Matillion](https://www.matillion.com/)
  +  [SnapLogic](https://www.snaplogic.com/)
  +  [Talend](https://www.talend.com/)
  +  [BryteFlow Ingest](https://bryteflow.com/bryteflow-ingest-xl-ingest/?did=pa_card&trk=pa_card)
  +  [SQL Server Integration Services](https://docs.microsoft.com/en-us/sql/integration-services/sql-server-integration-services?view=sql-server-ver15) (SSIS)

 For more information on data integration and consulting partners, see [Amazon Redshift Partners](https://aws.amazon.com/redshift/partners/).

 We provide technical advice, migration support, and financial assistance to help eligible customers quickly and cost-effectively migrate from legacy data warehouses to Amazon Redshift, the most popular and fastest cloud data warehouse. Qualifying customers receive advice on application architecture, migration strategies, program management, proof-of-concept, and employee training that are customized for their technology landscape and migration goals. We offer migration assistance through [Amazon Database Migration Accelerator](https://aws.amazon.com/solutions/databasemigrations/database-migration-accelerator/), [AWS Professional Services](https://aws.amazon.com/professional-services/), or our network of Partners. These teams and organizations specialize in a range of data warehouse and analytics technologies, and bring a wealth of experience acquired by migrating thousands of data warehouses and applications to AWS. We also offer service credits to minimize the financial impact of the migration. For more information, see [Migrate to Amazon Redshift](https://aws.amazon.com/redshift/data-warehouse-migration/).
