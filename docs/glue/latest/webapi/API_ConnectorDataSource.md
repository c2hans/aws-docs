---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectorDataSource.html
---

# ConnectorDataSource
<a name="API_ConnectorDataSource"></a>

Specifies a source generated with standard connection options.

## Contents
<a name="API_ConnectorDataSource_Contents"></a>

 ** ConnectionType **   <a name="Glue-Type-ConnectorDataSource-ConnectionType"></a>
The `connectionType`, as provided to the underlying AWS Glue library. This node type supports the following connection types:
+  `opensearch`
+  `azuresql`
+  `azurecosmos`
+  `bigquery`
+  `saphana`
+  `teradata`
+  `vertica`
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Data **   <a name="Glue-Type-ConnectorDataSource-Data"></a>
A map specifying connection options for the node. You can find standard connection options for the corresponding connection type in the [ Connection parameters](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html) section of the AWS Glue documentation.
Type: String to string map
Required: Yes

 ** Name **   <a name="Glue-Type-ConnectorDataSource-Name"></a>
The name of this source node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** OutputSchemas **   <a name="Glue-Type-ConnectorDataSource-OutputSchemas"></a>
Specifies the data schema for this source.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_ConnectorDataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectorDataSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectorDataSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectorDataSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
