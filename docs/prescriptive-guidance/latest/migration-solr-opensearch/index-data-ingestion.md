---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/index-data-ingestion.html
---

# Understanding data ingestion
<a name="index-data-ingestion"></a>

In Solr, you can implement extract, transform, load (ETL) workflows by using various approaches that are optimized for different use cases and data sources. These approaches provide proper data extraction, transformation to match your schema, and loading into the search index while maintaining data integrity and search optimization.

The key components of an ETL workflow are:
+ Extract: Get data from source systems (databases, file systems, web feeds, and APIs).
+ Transform: Process, clean, format, and validate data.
+ Load: Index processed data into the target system.

Solr provides request handlers that process incoming requests to add, update, or delete documents in the index. The two primary handlers used for this purpose are the update handler and the Data Import Handler (DIH). You can use these request handlers to implement ETL processes for ingestion of data into Solr.

## Update handler
<a name="update-handler.8b40942a-46b2-52f3-9069-b9030d2f103e"></a>

The update handler is the main endpoint for receiving index updates in Solr. It accepts documents in several formats, including:
+ XML: The traditional format for adding and updating documents in the index
+ JSON: A modern and widely used format for indexing single documents, a list of documents, or update commands
+ CSV: Allows for straightforward ingestion of comma-separated data
+ Javabin: An optimized binary format that is used primarily by the SolrJ Java client

The update handler is ideal for direct, programmatic data ingestion where an external application or process pushes data to Solr.

## Data Import Handler (DIH)
<a name="data-import-handler--dih-.472a0217-101d-5c4d-9fc5-c1148591b95f"></a>

The Data Import Handler (DIH) is a Solr request handler that pulls data directly into Solr from structured sources such as relational databases, XML files, and RSS feeds by using a configuration-driven approach that's defined in a `data-config.xml` file. DIH supports multiple data sources through Java Database Connectivity (JDBC), file systems, and web feeds; offers both full and incremental (delta) imports for keeping indexes updated; and includes built-in transformers for data modification before indexing.

However, DIH has been deprecated and was removed from Solr 9.0. Solr now recommends alternatives such as using custom ingestion clients with the update handler, community-maintained DIH plugins, or streaming expressions.

## Other indexing-related handlers
<a name="other-indexing-related-handlers.18c1512f-f99a-5958-95e7-a940f0492f63"></a>

In addition to the main update handlers, the following tools can help with data ingestion for specific use cases:
+ Extracting request handler (Solr Cell): This handler uses Apache Tika to automatically extract text and metadata from rich-text documents such as PDFs and Microsoft Office files.
+ Update request processors: These are plugins that can be chained together to pre-process documents before they are indexed. They can perform various tasks, such as language detection, dropping fields, or updating fields.

## Common ETL processes in Solr
<a name="common-etl-processes-in-solr.1c4c8c54-2e73-5441-90a0-61710c64f58a"></a>

Organizations typically use the following ETL processes in Solr:
+ Database ETL: DIH provides a streamlined ETL process for RDBMS sources by automatically mapping database columns to fields and handling incremental updates. The SolrJ API enables programmatic control for custom ETL workflows when importing from file systems or other structured data sources. You can design a composite ETL pipeline where database records contain metadata and file path references, and use DIH with custom entity processors to fetch metadata and enrich it with file content.
+ Web content ETL: Apache Nutch integration delivers a systematic ETL pipeline for web content. Apache Nutch handles crawling and extraction, transforms HTML content into structured data, and loads it directly into the index through native integration (DIH).
