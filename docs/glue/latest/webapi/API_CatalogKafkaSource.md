---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CatalogKafkaSource.html
---

# CatalogKafkaSource
<a name="API_CatalogKafkaSource"></a>

Specifies an Apache Kafka data store in the Data Catalog.

## Contents
<a name="API_CatalogKafkaSource_Contents"></a>

 ** Database **   <a name="Glue-Type-CatalogKafkaSource-Database"></a>
The name of the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-CatalogKafkaSource-Name"></a>
The name of the data store.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-CatalogKafkaSource-Table"></a>
The name of the table in the database to read from.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** DataPreviewOptions **   <a name="Glue-Type-CatalogKafkaSource-DataPreviewOptions"></a>
Specifies options related to data preview for viewing a sample of your data.
Type: [StreamingDataPreviewOptions](API_StreamingDataPreviewOptions.md) object
Required: No

 ** DetectSchema **   <a name="Glue-Type-CatalogKafkaSource-DetectSchema"></a>
Whether to automatically determine the schema from the incoming data.
Type: Boolean
Required: No

 ** StreamingOptions **   <a name="Glue-Type-CatalogKafkaSource-StreamingOptions"></a>
Specifies the streaming options.
Type: [KafkaStreamingSourceOptions](API_KafkaStreamingSourceOptions.md) object
Required: No

 ** WindowSize **   <a name="Glue-Type-CatalogKafkaSource-WindowSize"></a>
The amount of time to spend processing each micro batch.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_CatalogKafkaSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CatalogKafkaSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CatalogKafkaSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CatalogKafkaSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
