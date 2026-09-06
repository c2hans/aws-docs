---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SnowflakePropertiesPatch.html
---

# SnowflakePropertiesPatch
<a name="API_SnowflakePropertiesPatch"></a>

Contains the Snowflake-specific settings to update on an existing connection. Include only the fields you want to change.

## Contents
<a name="API_SnowflakePropertiesPatch_Contents"></a>

 ** connectivityPropertiesPatch **   <a name="datazone-Type-SnowflakePropertiesPatch-connectivityPropertiesPatch"></a>
The connectivity properties patch of the Snowflake connection.
Type: [ConnectivityPropertiesPatch](API_ConnectivityPropertiesPatch.md) object
Required: No

 ** lineageSync **   <a name="datazone-Type-SnowflakePropertiesPatch-lineageSync"></a>
The lineage sync configuration for the Snowflake connection.
Type: [LineageSyncInput](API_LineageSyncInput.md) object
Required: No

 ** snowflakeRole **   <a name="datazone-Type-SnowflakePropertiesPatch-snowflakeRole"></a>
The Snowflake role used to access Snowflake resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_$]+`
Required: No

## See Also
<a name="API_SnowflakePropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SnowflakePropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SnowflakePropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SnowflakePropertiesPatch)
