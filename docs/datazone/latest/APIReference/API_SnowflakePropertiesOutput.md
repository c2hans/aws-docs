---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SnowflakePropertiesOutput.html
---

# SnowflakePropertiesOutput
<a name="API_SnowflakePropertiesOutput"></a>

Contains the Snowflake-specific settings returned for an existing connection, including the current role, identity mapping, lineage sync state, and connection status.

## Contents
<a name="API_SnowflakePropertiesOutput_Contents"></a>

 ** identityMapping **   <a name="datazone-Type-SnowflakePropertiesOutput-identityMapping"></a>
The identity mapping configuration for the Snowflake connection.
Type: [IdentityMapping](API_IdentityMapping.md) object
Required: Yes

 ** lineageSync **   <a name="datazone-Type-SnowflakePropertiesOutput-lineageSync"></a>
The lineage sync configuration for the Snowflake connection.
Type: [LineageSyncOutput](API_LineageSyncOutput.md) object
Required: Yes

 ** snowflakeRole **   <a name="datazone-Type-SnowflakePropertiesOutput-snowflakeRole"></a>
The Snowflake role used to access Snowflake resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_$]+`
Required: Yes

 ** status **   <a name="datazone-Type-SnowflakePropertiesOutput-status"></a>
The status of the Snowflake connection.
Type: String
Valid Values: `CREATING | CREATE_FAILED | DELETING | DELETE_FAILED | READY | UPDATING | UPDATE_FAILED | DELETED`
Required: Yes

 ** errorMessage **   <a name="datazone-Type-SnowflakePropertiesOutput-errorMessage"></a>
An error message returned if the Snowflake connection failed to establish or validate.
Type: String
Required: No

## See Also
<a name="API_SnowflakePropertiesOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SnowflakePropertiesOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SnowflakePropertiesOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SnowflakePropertiesOutput)
