---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SnowflakeDestinationProperties.html
---

# SnowflakeDestinationProperties
<a name="API_SnowflakeDestinationProperties"></a>

 The properties that are applied when Snowflake is being used as a destination.

## Contents
<a name="API_SnowflakeDestinationProperties_Contents"></a>

 ** intermediateBucketName **   <a name="appflow-Type-SnowflakeDestinationProperties-intermediateBucketName"></a>
 The intermediate bucket that Amazon AppFlow uses when moving data into Snowflake.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `\S+`
Required: Yes

 ** object **   <a name="appflow-Type-SnowflakeDestinationProperties-object"></a>
 The object specified in the Snowflake flow destination.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** bucketPrefix **   <a name="appflow-Type-SnowflakeDestinationProperties-bucketPrefix"></a>
 The object key for the destination bucket in which Amazon AppFlow places the files.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** errorHandlingConfig **   <a name="appflow-Type-SnowflakeDestinationProperties-errorHandlingConfig"></a>
 The settings that determine how Amazon AppFlow handles an error when placing data in the Snowflake destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.
Type: [ErrorHandlingConfig](API_ErrorHandlingConfig.md) object
Required: No

## See Also
<a name="API_SnowflakeDestinationProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SnowflakeDestinationProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SnowflakeDestinationProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SnowflakeDestinationProperties)
