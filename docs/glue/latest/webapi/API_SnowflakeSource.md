---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_SnowflakeSource.html
---

# SnowflakeSource
<a name="API_SnowflakeSource"></a>

Specifies a Snowflake data source.

## Contents
<a name="API_SnowflakeSource_Contents"></a>

 ** Data **   <a name="Glue-Type-SnowflakeSource-Data"></a>
Configuration for the Snowflake data source.
Type: [SnowflakeNodeData](API_SnowflakeNodeData.md) object
Required: Yes

 ** Name **   <a name="Glue-Type-SnowflakeSource-Name"></a>
The name of the Snowflake data source.
Type: String
Pattern: `([^\r\n])*`
Required: Yes

 ** OutputSchemas **   <a name="Glue-Type-SnowflakeSource-OutputSchemas"></a>
Specifies user-defined schemas for your output data.
Type: Array of [GlueSchema](API_GlueSchema.md) objects
Required: No

## See Also
<a name="API_SnowflakeSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/SnowflakeSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/SnowflakeSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/SnowflakeSource)
