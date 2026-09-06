---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SparkConnectorSource.html
---

# SparkConnectorSource
<a name="API_SparkConnectorSource"></a>

Specifies a connector to an Apache Spark data source.

## Contents
<a name="API_SparkConnectorSource_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-SparkConnectorSource-ConnectionName"></a>
The name of the connection that is associated with the connector.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionType **   <a name="Glue-Type-SparkConnectorSource-ConnectionType"></a>
The type of connection, such as marketplace.spark or custom.spark, designating a connection to an Apache Spark data store.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectorName **   <a name="Glue-Type-SparkConnectorSource-ConnectorName"></a>
The name of a connector that assists with accessing the data store in AWS Glue Studio.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-SparkConnectorSource-Name"></a>
The name of the data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-SparkConnectorSource-AdditionalOptions"></a>
Additional connection options for the connector.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-SparkConnectorSource-OutputSchemas"></a>
Specifies data schema for the custom spark source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_SparkConnectorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SparkConnectorSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SparkConnectorSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SparkConnectorSource)
