---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SnowflakeConnectorProfileProperties.html
---

# SnowflakeConnectorProfileProperties
<a name="API_SnowflakeConnectorProfileProperties"></a>

 The connector-specific profile properties required when using Snowflake.

## Contents
<a name="API_SnowflakeConnectorProfileProperties_Contents"></a>

 ** bucketName **   <a name="appflow-Type-SnowflakeConnectorProfileProperties-bucketName"></a>
 The name of the Amazon S3 bucket associated with Snowflake.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `\S+`
Required: Yes

 ** stage **   <a name="appflow-Type-SnowflakeConnectorProfileProperties-stage"></a>
 The name of the Amazon S3 stage that was created while setting up an Amazon S3 stage in the Snowflake account. This is written in the following format: < Database>< Schema><Stage Name>.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** warehouse **   <a name="appflow-Type-SnowflakeConnectorProfileProperties-warehouse"></a>
 The name of the Snowflake warehouse.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\w/!@#+=.-]*`
Required: Yes

 ** accountName **   <a name="appflow-Type-SnowflakeConnectorProfileProperties-accountName"></a>
 The name of the account.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: No

 ** bucketPrefix **   <a name="appflow-Type-SnowflakeConnectorProfileProperties-bucketPrefix"></a>
 The bucket path that refers to the Amazon S3 bucket associated with Snowflake.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** privateLinkServiceName **   <a name="appflow-Type-SnowflakeConnectorProfileProperties-privateLinkServiceName"></a>
 The Snowflake Private Link service name to be used for private data transfers.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^$|com.amazonaws.vpce.[\w/!:@#.\-]+`
Required: No

 ** region **   <a name="appflow-Type-SnowflakeConnectorProfileProperties-region"></a>
 The AWS Region of the Snowflake account.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `\S+`
Required: No

## See Also
<a name="API_SnowflakeConnectorProfileProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SnowflakeConnectorProfileProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SnowflakeConnectorProfileProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SnowflakeConnectorProfileProperties)
