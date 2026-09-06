---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingJobOutputSource.html
---

# IdMappingJobOutputSource
<a name="API_IdMappingJobOutputSource"></a>

An object containing `KMSArn`, `outputS3Path`, and `roleARN`.

## Contents
<a name="API_IdMappingJobOutputSource_Contents"></a>

 ** outputS3Path **   <a name="API-Type-IdMappingJobOutputSource-outputS3Path"></a>
The S3 path to which AWS Entity Resolution will write the output table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?`
Required: Yes

 ** roleArn **   <a name="API-Type-IdMappingJobOutputSource-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. AWS Entity Resolution assumes this role to access AWS resources on your behalf as part of workflow execution.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** KMSArn **   <a name="API-Type-IdMappingJobOutputSource-KMSArn"></a>
Customer AWS KMS ARN for encryption at rest. If not provided, system will use an AWS Entity Resolution managed KMS key.
Type: String
Pattern: `arn:aws:kms:.*:[0-9]+:.*`
Required: No

## See Also
<a name="API_IdMappingJobOutputSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdMappingJobOutputSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdMappingJobOutputSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdMappingJobOutputSource)
