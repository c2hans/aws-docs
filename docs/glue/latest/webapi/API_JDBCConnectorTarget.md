---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_JDBCConnectorTarget.html
---

# JDBCConnectorTarget
<a name="API_JDBCConnectorTarget"></a>

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.

## Contents
<a name="API_JDBCConnectorTarget_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-JDBCConnectorTarget-ConnectionName"></a>
The name of the connection that is associated with the connector.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionTable **   <a name="Glue-Type-JDBCConnectorTarget-ConnectionTable"></a>
The name of the table in the data target.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionType **   <a name="Glue-Type-JDBCConnectorTarget-ConnectionType"></a>
The type of connection, such as marketplace.jdbc or custom.jdbc, designating a connection to a JDBC data target.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectorName **   <a name="Glue-Type-JDBCConnectorTarget-ConnectorName"></a>
The name of a connector that will be used.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-JDBCConnectorTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-JDBCConnectorTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-JDBCConnectorTarget-AdditionalOptions"></a>
Additional connection options for the connector.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-JDBCConnectorTarget-OutputSchemas"></a>
Specifies the data schema for the JDBC target.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_JDBCConnectorTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/JDBCConnectorTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/JDBCConnectorTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/JDBCConnectorTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
