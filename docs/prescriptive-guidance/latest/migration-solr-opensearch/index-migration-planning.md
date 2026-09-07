---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/index-migration-planning.html
---

# Data migration planning
<a name="index-migration-planning"></a>

This section explores data migration paths and helps you select the most appropriate strategy for your use case. Before you begin your data migration to OpenSearch, choose the approach that best fits your requirements.

## Assess your current environment
<a name="index-assess-environment"></a>

When you decide to migrate from Solr to OpenSearch, you start a process that requires careful planning and strategic decision-making. The first crucial step is to assess your current environment and determine the most effective path forward.

The initial evaluation should focus on your transformation requirements. If you have straightforward transformations and robust ETL processes in Solr, adapting the current architecture with OpenSearch modifications might be optimal. On the other hand, if you need advanced capabilities or modernization, consider using [Amazon OpenSearch Ingestion (OSI)](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-getting-started-tutorials.html).

The following diagram illustrates the two major approaches to data migration, which run in parallel.

![Two parallel approaches when migrating from Solr to OpenSearch.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/images/guide-img/20cfd7ab-1afd-4038-9280-20666ff596e1/images/3c835e1a-ade8-4518-ae7c-a3d3a2f85e89.png)

1. **Live data migration** follows a  path from 1, to 3, 5, and 7 in the diagram. It captures real-time change data from various sources and ingests it into OpenSearch through ETL solutions.

1. **Historical data migration** follows a path from 2 to 4-5-7 or 6-7. It migrates past data to OpenSearch and provides two options after evaluating source system access:
   + 4.a **Reindex from source (recommended)**. When you migrate to Amazon OpenSearch Service, building from your source systems provides the most reliable path. This approach gives you direct access to your authoritative data sources, whether they're in Amazon Relational Database Service (Amazon RDS), Amazon DocumentDB, Amazon Simple Storage Service (Amazon S3), or other storage systems. You maintain complete control over data quality and can optimize your schema design during migration. The source system approach supports formats such as  JSON, CSV, and Apache Parquet, so you can work with your existing data structures while implementing the necessary transformations. The next step after you choose this migration option is to review existing ingestion (ETL) solutions (5).
   + 4.b **Solr as source**. Consider direct Solr migration when your source systems are inaccessible or when you need a faster migration path. This approach requires a stable Solr deployment with sufficient resources to handle the additional read load during migration. You can use either the Solr select handler with the `cursorMark` parameter for reliable pagination, or the export handler for optimized streaming. Although this method offers quicker implementation, it requires careful monitoring of your Solr cluster's performance and network bandwidth to ensure successful data transfer. This approach focuses solely on migrating historical data, so any tools or processes developed for this migration should be considered temporary and disposable. Continuous ingestion and ongoing data updates from the source system will need a separate, permanent solution after the historical data migration is complete. The next step after you choose this migration option is to review Solr handler solutions (6).

The recommended approach is to reindex from the original source system. Consider using Solr as a source as an alternative when direct source access is limited.

## ETL assessment
<a name="index-etl-assessment"></a>

After you select your migration approach, you can perform a detailed ETL assessment. This assessment helps determine specific implementation requirements based on your chosen path and existing infrastructure.
+ **Reviewing ingestion (ETL) solutions.** If your organization already has an established ETL pipeline, evaluate its effectiveness and compatibility with OpenSearch. Identify which category your existing ETL solution falls into:
  + Custom application development (for example, your own SolrJ-based solution)
  + Connector-based solution (for example, using Solr DIH, request handlers, or Apache Nutch)
  + Purpose-built integration (for example, Apache Tika connectors)
+ **Reviewing Solr handlers.** Solr provides handlers such as select and export by default. These help export millions of records.
