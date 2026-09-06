---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AthenaConnectorSource.html
---

# AthenaConnectorSource
<a name="API_AthenaConnectorSource"></a>

Specifies a connector to an Amazon Athena data source.

## Contents
<a name="API_AthenaConnectorSource_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-AthenaConnectorSource-ConnectionName"></a>
The name of the connection that is associated with the connector.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionType **   <a name="Glue-Type-AthenaConnectorSource-ConnectionType"></a>
The type of connection, such as marketplace.athena or custom.athena, designating a connection to an Amazon Athena data store.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectorName **   <a name="Glue-Type-AthenaConnectorSource-ConnectorName"></a>
The name of a connector that assists with accessing the data store in AWS Glue Studio.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-AthenaConnectorSource-Name"></a>
The name of the data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** SchemaName **   <a name="Glue-Type-AthenaConnectorSource-SchemaName"></a>
The name of the Cloudwatch log group to read from. For example, `/aws-glue/jobs/output`.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionTable **   <a name="Glue-Type-AthenaConnectorSource-ConnectionTable"></a>
The name of the table in the data source.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-AthenaConnectorSource-OutputSchemas"></a>
Specifies the data schema for the custom Athena source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_AthenaConnectorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AthenaConnectorSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AthenaConnectorSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AthenaConnectorSource)
