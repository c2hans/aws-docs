---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_SnowflakeParameters.html
---

# SnowflakeParameters
<a name="API_SnowflakeParameters"></a>

The parameters for Snowflake.

## Contents
<a name="API_SnowflakeParameters_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Database **   <a name="QS-Type-SnowflakeParameters-Database"></a>
Database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** Host **   <a name="QS-Type-SnowflakeParameters-Host"></a>
Host.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** Warehouse **   <a name="QS-Type-SnowflakeParameters-Warehouse"></a>
Warehouse.
Type: String
Length Constraints: Maximum length of 128.
Required: Yes

 ** AuthenticationType **   <a name="QS-Type-SnowflakeParameters-AuthenticationType"></a>
The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.
Type: String
Valid Values: `PASSWORD | KEYPAIR | TOKEN | X509`
Required: No

 ** DatabaseAccessControlRole **   <a name="QS-Type-SnowflakeParameters-DatabaseAccessControlRole"></a>
The database access control role.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** OAuthParameters **   <a name="QS-Type-SnowflakeParameters-OAuthParameters"></a>
An object that contains information needed to create a data source connection between an Quick Sight account and Snowflake.
Type: [OAuthParameters](API_OAuthParameters.md) object
Required: No

## See Also
<a name="API_SnowflakeParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/SnowflakeParameters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/SnowflakeParameters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/SnowflakeParameters)
