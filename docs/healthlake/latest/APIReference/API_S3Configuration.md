---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_S3Configuration.html
---

# S3Configuration
<a name="API_S3Configuration"></a>

The configuration of the Amazon S3 bucket for either an import or export job. This includes assigning access permissions.

## Contents
<a name="API_S3Configuration_Contents"></a>

 ** KmsKeyId **   <a name="HealthLake-Type-S3Configuration-KmsKeyId"></a>
The Key Management Service (AWS KMS) key ID used to access the Amazon S3 bucket.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 400.
Pattern: `(arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:kms:)?([a-z]{2}-[a-z]+(-[a-z]+)?-\d:)?(\d{12}:)?(((key/)?[a-zA-Z0-9-_]+)|(alias/[a-zA-Z0-9:/_-]+))`
Required: Yes

 ** S3Uri **   <a name="HealthLake-Type-S3Configuration-S3Uri"></a>
The `S3Uri` is the user-specified Amazon S3 location of the FHIR data to be imported into AWS HealthLake.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

## See Also
<a name="API_S3Configuration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/S3Configuration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/S3Configuration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/S3Configuration)
