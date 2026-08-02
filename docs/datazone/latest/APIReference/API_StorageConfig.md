---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_StorageConfig.html
---

# StorageConfig
<a name="API_StorageConfig"></a>

The storage configuration for a notebook run in Amazon SageMaker Unified Studio.

## Contents
<a name="API_StorageConfig_Contents"></a>

 ** kmsKeyArn **   <a name="datazone-Type-StorageConfig-kmsKeyArn"></a>
The ARN of the AWS KMS key used for encryption.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `arn:aws(|-cn|-us-gov):kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}`
Required: No

 ** projectS3Path **   <a name="datazone-Type-StorageConfig-projectS3Path"></a>
The Amazon Simple Storage Service path for the project storage.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://.+`
Required: No

## See Also
<a name="API_StorageConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/StorageConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/StorageConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/StorageConfig)
