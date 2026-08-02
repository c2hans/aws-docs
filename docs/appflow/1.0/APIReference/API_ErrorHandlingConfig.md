---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ErrorHandlingConfig.html
---

# ErrorHandlingConfig
<a name="API_ErrorHandlingConfig"></a>

 The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. `ErrorHandlingConfig` is a part of the destination connector details.

## Contents
<a name="API_ErrorHandlingConfig_Contents"></a>

 ** bucketName **   <a name="appflow-Type-ErrorHandlingConfig-bucketName"></a>
 Specifies the name of the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `\S+`
Required: No

 ** bucketPrefix **   <a name="appflow-Type-ErrorHandlingConfig-bucketPrefix"></a>
 Specifies the Amazon S3 bucket prefix.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** failOnFirstDestinationError **   <a name="appflow-Type-ErrorHandlingConfig-failOnFirstDestinationError"></a>
 Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.
Type: Boolean
Required: No

## See Also
<a name="API_ErrorHandlingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ErrorHandlingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ErrorHandlingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ErrorHandlingConfig)
