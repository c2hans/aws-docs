---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CrawlerTargets.html
---

# CrawlerTargets
<a name="API_CrawlerTargets"></a>

Specifies data stores to crawl.

## Contents
<a name="API_CrawlerTargets_Contents"></a>

 ** CatalogTargets **   <a name="Glue-Type-CrawlerTargets-CatalogTargets"></a>
Specifies AWS Glue Data Catalog targets.
Type: Array of [CatalogTarget](API_CatalogTarget.md) objects
Required: No

 ** DeltaTargets **   <a name="Glue-Type-CrawlerTargets-DeltaTargets"></a>
Specifies Delta data store targets.
Type: Array of [DeltaTarget](API_DeltaTarget.md) objects
Required: No

 ** DynamoDBTargets **   <a name="Glue-Type-CrawlerTargets-DynamoDBTargets"></a>
Specifies Amazon DynamoDB targets.
Type: Array of [DynamoDBTarget](API_DynamoDBTarget.md) objects
Required: No

 ** HudiTargets **   <a name="Glue-Type-CrawlerTargets-HudiTargets"></a>
Specifies Apache Hudi data store targets.
Type: Array of [HudiTarget](API_HudiTarget.md) objects
Required: No

 ** IcebergTargets **   <a name="Glue-Type-CrawlerTargets-IcebergTargets"></a>
Specifies Apache Iceberg data store targets.
Type: Array of [IcebergTarget](API_IcebergTarget.md) objects
Required: No

 ** JdbcTargets **   <a name="Glue-Type-CrawlerTargets-JdbcTargets"></a>
Specifies JDBC targets.
Type: Array of [JdbcTarget](API_JdbcTarget.md) objects
Required: No

 ** MongoDBTargets **   <a name="Glue-Type-CrawlerTargets-MongoDBTargets"></a>
Specifies Amazon DocumentDB or MongoDB targets.
Type: Array of [MongoDBTarget](API_MongoDBTarget.md) objects
Required: No

 ** S3Targets **   <a name="Glue-Type-CrawlerTargets-S3Targets"></a>
Specifies Amazon Simple Storage Service (Amazon S3) targets.
Type: Array of [S3Target](API_S3Target.md) objects
Required: No

## See Also
<a name="API_CrawlerTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CrawlerTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CrawlerTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CrawlerTargets)
