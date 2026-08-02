---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JDBCConnectorSource.html
---

# JDBCConnectorSource
<a name="API_JDBCConnectorSource"></a>

Specifies a connector to a JDBC data source.

## Contents
<a name="API_JDBCConnectorSource_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-JDBCConnectorSource-ConnectionName"></a>
The name of the connection that is associated with the connector.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionType **   <a name="Glue-Type-JDBCConnectorSource-ConnectionType"></a>
The type of connection, such as marketplace.jdbc or custom.jdbc, designating a connection to a JDBC data store.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectorName **   <a name="Glue-Type-JDBCConnectorSource-ConnectorName"></a>
The name of a connector that assists with accessing the data store in AWS Glue Studio.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-JDBCConnectorSource-Name"></a>
The name of the data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-JDBCConnectorSource-AdditionalOptions"></a>
Additional connection options for the connector.
Type: [JDBCConnectorOptions](API_JDBCConnectorOptions.md) object
Required: No

 ** ConnectionTable **   <a name="Glue-Type-JDBCConnectorSource-ConnectionTable"></a>
The name of the table in the data source.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-JDBCConnectorSource-OutputSchemas"></a>
Specifies the data schema for the custom JDBC source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** Query **   <a name="Glue-Type-JDBCConnectorSource-Query"></a>
The table or SQL query to get the data from. You can specify either `ConnectionTable` or `query`, but not both.
Type: String
Pattern: `([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\s])*`
Required: No

## See Also
<a name="API_JDBCConnectorSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JDBCConnectorSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JDBCConnectorSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JDBCConnectorSource)
