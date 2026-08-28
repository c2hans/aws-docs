---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SnowflakePropertiesInput.html
---

# SnowflakePropertiesInput
<a name="API_SnowflakePropertiesInput"></a>

Contains the Snowflake-specific settings required when creating or updating a connection, including the Snowflake role, identity mapping, and lineage sync configuration.

## Contents
<a name="API_SnowflakePropertiesInput_Contents"></a>

 ** identityMapping **   <a name="datazone-Type-SnowflakePropertiesInput-identityMapping"></a>
The identity mapping configuration for the Snowflake connection.
Type: [IdentityMapping](API_IdentityMapping.md) object
Required: Yes

 ** snowflakeRole **   <a name="datazone-Type-SnowflakePropertiesInput-snowflakeRole"></a>
The Snowflake role used to access Snowflake resources.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_$]+`
Required: Yes

 ** connectivityProperties **   <a name="datazone-Type-SnowflakePropertiesInput-connectivityProperties"></a>
The connectivity properties of the Snowflake connection.
Type: [ConnectivityProperties](API_ConnectivityProperties.md) object
Required: No

 ** lineageSync **   <a name="datazone-Type-SnowflakePropertiesInput-lineageSync"></a>
The lineage sync configuration for the Snowflake connection.
Type: [LineageSyncInput](API_LineageSyncInput.md) object
Required: No

## See Also
<a name="API_SnowflakePropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SnowflakePropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SnowflakePropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SnowflakePropertiesInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
