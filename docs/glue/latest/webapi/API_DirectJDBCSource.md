---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DirectJDBCSource.html
---

# DirectJDBCSource
<a name="API_DirectJDBCSource"></a>

Specifies the direct JDBC source connection.

## Contents
<a name="API_DirectJDBCSource_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-DirectJDBCSource-ConnectionName"></a>
The connection name of the JDBC source.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionType **   <a name="Glue-Type-DirectJDBCSource-ConnectionType"></a>
The connection type of the JDBC source.
Type: String
Valid Values: `sqlserver | mysql | oracle | postgresql | redshift`
Required: Yes

 ** Database **   <a name="Glue-Type-DirectJDBCSource-Database"></a>
The database of the JDBC source connection.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Name **   <a name="Glue-Type-DirectJDBCSource-Name"></a>
The name of the JDBC source connection.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Table **   <a name="Glue-Type-DirectJDBCSource-Table"></a>
The table of the JDBC source connection.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** OutputSchemas **   <a name="Glue-Type-DirectJDBCSource-OutputSchemas"></a>
Specifies the data schema for the direct JDBC source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

 ** RedshiftTmpDir **   <a name="Glue-Type-DirectJDBCSource-RedshiftTmpDir"></a>
The temp directory of the JDBC Redshift source.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

## See Also
<a name="API_DirectJDBCSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DirectJDBCSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DirectJDBCSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DirectJDBCSource)
