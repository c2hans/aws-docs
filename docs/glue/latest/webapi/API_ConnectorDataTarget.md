---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConnectorDataTarget.html
---

# ConnectorDataTarget
<a name="API_ConnectorDataTarget"></a>

Specifies a target generated with standard connection options.

## Contents
<a name="API_ConnectorDataTarget_Contents"></a>

 ** ConnectionType **   <a name="Glue-Type-ConnectorDataTarget-ConnectionType"></a>
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

 ** Data **   <a name="Glue-Type-ConnectorDataTarget-Data"></a>
A map specifying connection options for the node. You can find standard connection options for the corresponding connection type in the [ Connection parameters](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html) section of the AWS Glue documentation.
Type: String to string map
Required: Yes

 ** Name **   <a name="Glue-Type-ConnectorDataTarget-Name"></a>
The name of this target node.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-ConnectorDataTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: No

## See Also
<a name="API_ConnectorDataTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConnectorDataTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConnectorDataTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConnectorDataTarget)
