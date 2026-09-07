---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/index-migration-process.html
---

# Data migration process
<a name="index-migration-process"></a>

The following diagram provides a decision matrix for your migration assessment.

![Decision matrix for ETL assessment before Solr to OpenSearch migration.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/images/guide-img/20cfd7ab-1afd-4038-9280-20666ff596e1/images/3782a66d-1acf-4aa3-8045-5e6c18160bad.png)

The following sections describe the process illustrated in the diagram in more detail.

## Determine whether an ETL solution exists
<a name="index-etl-solution"></a>

This decision point determines whether you have an existing ETL solution in Solr, leading to two paths:
+ If you have an existing ETL solution (2.a in the diagram), follow the instructions in the next section to adapt your implementation type to work with OpenSearch.
+ If you don't have an existing ETL solution (2.b in the diagram), you have an opportunity to build a modern, cloud-native data pipeline by using OSI.

## Evaluate your current ETL
<a name="index-etl-evaluation"></a>

The ETL pathway consists of:
+ Light transformation: Adapt existing ETL by incorporating an OpenSearch sink (the target for your data).
+ Heavy transformation: Preserve current ETL infrastructure while transitioning from SolrJ to the OpenSearch bulk API.

When you migrate data from your current data sources, you typically have ETL solutions that align with one of three categories:
+ Custom code solutions (3.a in the previous diagram)
+ Connector-based solutions (3.b in the diagram)
+ Purpose-built solutions (3.c in the diagram)

### Custom code solutions (high complexity)
<a name="custom-code-solutions--high-complexity-.de8524dc-069f-5318-8313-d34fb49852da"></a>

If you've built custom data ingestion solutions for Solr, migrating to Amazon OpenSearch Service requires a systematic approach that preserves your existing functionality while leveraging AWS Cloud capabilities. This section guides you through the migration process for your custom applications.

1. **Understand your current environment**. Begin by examining your existing custom implementation. Your application likely contains specific data processing logic, unique ingestion patterns, and custom post-processing requirements that you'll need to maintain after migration. Start with a comprehensive review of your current system, focusing on how your application interacts with Solr and identifying critical functionality that must be preserved.

1. **Plan your migration**. Before you modify any code, conduct a thorough assessment across three key areas:
   + Analyze your codebase to understand its scope and complexity. Document the programming languages in use, map out your data transformation logic, and review your current ingestion patterns. This analysis helps identify potential challenges and opportunities for optimization.
   + Evaluate your architecture. Whether your application runs on premises or on Amazon Elastic Compute Cloud (Amazon EC2), consider how you can modernize your deployment model. This might involve adopting containerization, implementing serverless components, or using other AWS managed services.
   + Examine your data processing workflows. Understanding how your application transforms and loads data helps ensure a smooth transition to Amazon OpenSearch Service while maintaining data integrity.

1. **Implement changes**. Focus on two primary areas:
   + Update your code to work with Amazon OpenSearch Service. This involves:
     + Modifying endpoint configurations to connect to your OpenSearch domain.
     + Updating client libraries to use the OpenSearch SDK.
     + Implementing AWS authentication mechanisms.
     + Testing data synchronization to ensure consistency.
   + Consider modernization opportunities, such as:
     + Evaluating OSI for simplified data loading.
     + Exploring AWS managed services that could replace custom components.
     + Planning a gradual transition from self-managed solutions to reduce risk.

The following sample code shows how to migrate document indexing code from an Apache SolrJ client to an OpenSearch client.

JSON format:

```
{
    "id": "123",
    "title": "Sample Document",
    "content": "This is the document content"
}
```

Indexing in a SolrJ client:

```
//Using SolrInputDocument
SolrInputDocument doc = new SolrInputDocument();
doc.addField("id", "123");
doc.addField("title", "Sample Document");
doc.addField("content", "This is the document content");
solrClient.add(doc);

// Commit the changes
solrClient.commit();
```

Indexing in an OpenSearch client:

```
// Using Map
Map<String, Object> document = new HashMap<>();
document.put("title", "Sample Document");
document.put("content", "This is the document content");
IndexRequest request = new IndexRequest("index_name").id("123").source(document);

// Run the index request
IndexResponse response = client.index(request, RequestOptions.DEFAULT);
```

### Connector-based solutions (medium complexity)
<a name="connector-based-solutions--medium-complexity-.1499fa2f-5e54-5b56-bdf3-9bb5b1cf5f3a"></a>

If your Solr implementation relies on prebuilt connectors for data ingestion, migrating to Amazon OpenSearch Service requires careful evaluation of your existing integrations. This section guides you through migrating your connector-based solutions while maintaining their functionality.

1. **Understand your current connectors**. Connectors serve as crucial bridges between your data sources and search infrastructure. In Solr environments, you might be using Database Import Handler (DIH) for database integration, XML or JSON handlers for file processing, Apache Tika for document parsing, Apache Nutch for web content crawling, or Fluent Bit or Logstash for real-time data processing. These connectors provide standardized ways to ingest and transform data while reducing development overhead.

1. **Plan your migration**. Start by assessing your current connector ecosystem. Examine how each connector interfaces with your data sources and what transformations they perform. For example, if you're using DIH to import database records, document the mapping configurations and any custom transformations you've implemented.

   Based on your assessment, you have three main implementation options:
   + Adapt compatible connectors. If your current connectors support Amazon OpenSearch Service, you can modify their configurations to point to your new OpenSearch domain. This approach minimizes changes to your existing architecture while leveraging familiar tools.
   + Implement OSI. For scenarios where direct compatibility isn't possible, OSI provides a managed alternative. This service handles data ingestion with built-in support for various data sources and formats.
   + Use AWS managed services. Consider AWS Cloud solutions that can replace your current connectors. For example, you can consider using AWS Lambda for your ingestion logic instead of using AWS Database Migration Service (AWS DMS). If you want to stream data to Amazon OpenSearch Service without staging data, consider using Amazon Data Firehose for streaming data.

1. **Implement changes**. Many Solr connectors work with XML formats, whereas OpenSearch prefers JSON. Plan your transformation approach.

### Purpose-built integrations
<a name="purpose-built-integrations.c5f24a20-698a-52a3-979e-8eef816bcea9"></a>

When your Solr implementation uses purpose-built tools for data ingestion, migrating to Amazon OpenSearch Service often presents the most straightforward path.

Purpose-built tools simplify your migration journey by providing streamlined migration paths, simple configuration updates, minimal code modifications, and ready-to-use integration patterns.

OSI provides a managed service for migrating your data to Amazon OpenSearch Service. This section guides you through the implementation process, from initial assessment to production deployment, as illustrated in the following diagram.

![OSI assessment and implementation for Solr migration.](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-solr-opensearch/images/guide-img/20cfd7ab-1afd-4038-9280-20666ff596e1/images/73e4e071-1872-4d92-b9e7-25d4f5bb7351.png)

1. **Initial assessment**. Begin your implementation journey by evaluating your migration requirements. Consider your current data volumes, throughput needs, and transformation requirements. During this phase, analyze:
   + Your application's performance requirements
   + Data source compatibility with OSI
   + Service quotas and limitations
   + Resource requirements

1. **Processor evaluation**. Based on your assessment, determine your processing needs:
   + **2.a. Native processors**. When your requirements align with OSI's built-in capabilities, you can use a native processor. An example configuration includes:

     ```
     processor:
     - type: date
     field: timestamp
     formats: ["yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"]
     ```

     Implementation steps include:
     + Configuring data source connections
     + Setting up transformation pipelines
     + Implementing monitoring
     + Testing performance
   + **2.b. Custom transformations**. For complex transformations that require additional processing, you can use AWS Lambda. For example:

     ```
     def process_record(event, context):
     # Custom transformation logic
     return transformed_data
     ```

     Key considerations:
     + Lambda function implementation
     + Custom transformation logic
     + Error handling setup
     + Performance monitoring

1. **Direct implementation path**. For implementations that use native processors, you can configure pipelines directly. For example:

   ```
   pipeline:
   source:
   type: s3
   bucket: your-bucket sink:
   type: opensearch
   domain: your-domain
   ```

1. **Enhanced implementation path**. For implementations that include Lambda processors, you can configure pipelines as follows:

   ```
   pipeline:
   source:
   type: s3 processor:
   - type: lambda
   function_arn: your-lambda-arn
   sink:
   type: opensearch
   ```

   Your migration approach depends on your tool's compatibility with Amazon OpenSearch Service.
   + Compatible tools. When your tools support Amazon OpenSearch Service, focus on configuration updates. Implementation steps include:
     + Updating endpoint configurations.
     + Modifying authentication settings.
     + Testing performance and reliability.
     + Monitoring data consistency.
   + Incompatible tools. For tools that lack OpenSearch compatibility:
     + Assess transformation requirements.
     + Evaluate data flow patterns.
     + Document integration points.

   Based on your compatibility assessment, choose one path:
   + For compatible solutions:
     + Reuse existing tools and update OpenSearch as the load endpoint.
     + Update configurations.
     + Test performance.
     + Monitor operations.
   + For a new implementation with OSI, set up a pipeline; for example:

     ```
     # Example: OSI pipeline setup
     version: 1
     pipeline:
     source:
     type: s3
     sink:
     type: opensearch
     ```

     OSI provides zero-ETL to the following supported data sources:
     + Amazon S3 for bulk data
     + Amazon DynamoDB for NoSQL data
     + Amazon DocumentDB for document data
     + Amazon Aurora for SQL data
     + Apache Kafka for streaming data

     The typical migration process starts from Solr, exports the data to JSON, places it in an S3 bucket, ingests it into OSI, and moves it to OpenSearch. By following this structured approach, you can implement OSI effectively while maintaining AWS best practices for performance, reliability, and operational excellence.

So far, this section focused on how configurations can be rewired. The next section explains how data can be migrated.
