---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SparkConnectorTarget.html
---

# SparkConnectorTarget
<a name="API_SparkConnectorTarget"></a>

Specifies a target that uses an Apache Spark connector.

## Contents
<a name="API_SparkConnectorTarget_Contents"></a>

 ** ConnectionName **   <a name="Glue-Type-SparkConnectorTarget-ConnectionName"></a>
The name of a connection for an Apache Spark connector.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectionType **   <a name="Glue-Type-SparkConnectorTarget-ConnectionType"></a>
The type of connection, such as marketplace.spark or custom.spark, designating a connection to an Apache Spark data store.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** ConnectorName **   <a name="Glue-Type-SparkConnectorTarget-ConnectorName"></a>
The name of an Apache Spark connector.
Type: String
Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: Yes

 ** Inputs **   <a name="Glue-Type-SparkConnectorTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: Yes

 ** Name **   <a name="Glue-Type-SparkConnectorTarget-Name"></a>
The name of the data target.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** AdditionalOptions **   <a name="Glue-Type-SparkConnectorTarget-AdditionalOptions"></a>
Additional connection options for the connector.
Type: String to string map
Key Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Value Pattern: `([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`
Required: No

 ** OutputSchemas **   <a name="Glue-Type-SparkConnectorTarget-OutputSchemas"></a>
Specifies the data schema for the custom spark target.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_SparkConnectorTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SparkConnectorTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SparkConnectorTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SparkConnectorTarget)
