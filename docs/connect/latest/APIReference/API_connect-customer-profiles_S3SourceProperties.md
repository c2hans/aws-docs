---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_S3SourceProperties.html
---

# S3SourceProperties
<a name="API_connect-customer-profiles_S3SourceProperties"></a>

The properties that are applied when Amazon S3 is being used as the flow source.

## Contents
<a name="API_connect-customer-profiles_S3SourceProperties_Contents"></a>

 ** BucketName **   <a name="connect-Type-connect-customer-profiles_S3SourceProperties-BucketName"></a>
The Amazon S3 bucket name where the source files are stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `\S+`
Required: Yes

 ** BucketPrefix **   <a name="connect-Type-connect-customer-profiles_S3SourceProperties-BucketPrefix"></a>
The object key for the Amazon S3 bucket in which the source files are stored.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

## See Also
<a name="API_connect-customer-profiles_S3SourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/S3SourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/S3SourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/S3SourceProperties)
