---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/build-from-source.html
---

# 2. Building from the source
<a name="build-from-source"></a>

As described earlier, building from the source is the approach where you do not migrate data from the current Elasticsearch or OpenSearch environment. Instead, you build indexes in the target domain directly from your log, or product-catalog data source or content source.

Two options are available for building from the source. The option you choose depends on the data type of your source data:
+ Using AWS Database Migration Service – If the source of your data is a relational database management system (RDBMS) and the source is supported by AWS Database Migration Service (AWS DMS), you can use AWS DMS to copy data from your data source to your target Amazon OpenSearch Service domain. AWS DMS supports full load and change data capture (CDC) options. In the full load option, the AWS DMS task copies all data from source database table to a target OpenSearch index. You can use default mapping or provide custom mapping configurations. In the CDC option, AWS DMS first makes a full copy of the source table records into a target OpenSearch index. Then it captures changed data (updates and inserts) and copies it to the OpenSearch index. For more information, see the blog posts [Introducing Amazon Elasticsearch Service as a target in AWS Database Migration Service](https://aws.amazon.com/blogs/database/introducing-amazon-elasticsearch-service-as-a-target-in-aws-database-migration-service/) and [Scale Amazon Elasticsearch Service for AWS Database Migration Service migrations](https://aws.amazon.com/blogs/database/scale-amazon-elasticsearch-service-for-aws-database-migration-service-migrations/).
+ Building from the document source – If your data source is not an RDBMS or it is not supported by AWS DMS, you might have to create a custom solution using open-source tools or a combination of open-source tools and AWS services. You must convert your source data to JSON documents before it can be loaded in OpenSearch. If you already have pipelines set up from your source to your current Elasticsearch or OpenSearch environment, you can point those data pipelines to OpenSearch with appropriate changes in client libraries and (if required) data model changes in indexes in the Amazon OpenSearch Service domain. When building indexes from source, keep in mind the following considerations:
  + The location of the documents – The documents could already be available in the AWS Cloud, in object storage such as Amazon S3, or they might be stored in an on-premises storage location such as a file system.
  + The format of the documents – The documents could already be in JSON format, ready to be ingested into the Amazon OpenSearch Service domain, or they might need to be cleansed, processed, and formatted into JSON before they can be ingested into Amazon OpenSearch Service domain.

Building from the source involves the following high-level steps:

1. Define index mapping and settings in the Amazon OpenSearch Service domain.

1. Extract data from the document source and copy it into an object storage location such as Amazon S3. You can use an open source tool (for example, Logstash), an AWS service client (for example, Amazon Kinesis Agent), a third-party commercial tool, or a custom program.

1. Configure an open-source tool (for example, Logstash or Fluent Bit) or a native AWS service (for example, AWS Lambda or AWS DMS) to convert data into JSON documents and load it periodically or continuously from the object store to the Amazon OpenSearch Service domain.

For more information, see [Loading streaming data into Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/integrations.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
