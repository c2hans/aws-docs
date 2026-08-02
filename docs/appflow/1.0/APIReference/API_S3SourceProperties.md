---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_S3SourceProperties.html
---

# S3SourceProperties
<a name="API_S3SourceProperties"></a>

 The properties that are applied when Amazon S3 is being used as the flow source.

## Contents
<a name="API_S3SourceProperties_Contents"></a>

 ** bucketName **   <a name="appflow-Type-S3SourceProperties-bucketName"></a>
 The Amazon S3 bucket name where the source files are stored.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `\S+`
Required: Yes

 ** bucketPrefix **   <a name="appflow-Type-S3SourceProperties-bucketPrefix"></a>
 The object key for the Amazon S3 bucket in which the source files are stored.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `.*`
Required: No

 ** s3InputFormatConfig **   <a name="appflow-Type-S3SourceProperties-s3InputFormatConfig"></a>
 When you use Amazon S3 as the source, the configuration format that you provide the flow input data.
Type: [S3InputFormatConfig](API_S3InputFormatConfig.md) object
Required: No

## See Also
<a name="API_S3SourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/S3SourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/S3SourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/S3SourceProperties)
