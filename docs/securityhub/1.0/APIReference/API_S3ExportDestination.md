---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_S3ExportDestination.html
---

# S3ExportDestination
<a name="API_S3ExportDestination"></a>

The Amazon S3 destination for an export, including the bucket, the AWS KMS key used for encryption, and an optional object key prefix.

## Contents
<a name="API_S3ExportDestination_Contents"></a>

 ** BucketArn **   <a name="securityhub-Type-S3ExportDestination-BucketArn"></a>
The Amazon Resource Name (ARN) of the Amazon S3 bucket that Security Hub writes the export to. You must own the bucket, and its bucket policy must grant the Security Hub service principal (`exportv2.securityhub.amazonaws.com`) permission to write objects. For the required bucket policy, see the Examples section of `StartExportJobV2`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** KmsKeyArn **   <a name="securityhub-Type-S3ExportDestination-KmsKeyArn"></a>
The ARN of the AWS KMS key that Security Hub uses to encrypt the export objects with server-side encryption. The key policy must allow the Security Hub service principal (`exportv2.securityhub.amazonaws.com`) to use the key through Amazon S3. For the required key policy, see the Examples section of `StartExportJobV2`.
The key must meet all of the following requirements:
+ It must be a symmetric key with a key usage of `ENCRYPT_DECRYPT`.
+ It must be a single-Region key. Multi-Region keys, whose key IDs begin with `mrk-`, are rejected.
+ You must specify the full key ARN. Key IDs and aliases are rejected.
+ The key must be in the same AWS account as the export job.
+ The key must be in the same AWS Region as the export job.
+ The key must be in the `aws`, `aws-cn`, or `aws-us-gov` partition.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ObjectPrefix **   <a name="securityhub-Type-S3ExportDestination-ObjectPrefix"></a>
An optional key prefix that Security Hub prepends to the Amazon S3 object keys of the export output. Use a prefix to organize exports within the bucket. The value can be up to 512 characters.
Type: String
Length Constraints: Maximum length of 512.
Required: No

## See Also
<a name="API_S3ExportDestination_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/S3ExportDestination)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/S3ExportDestination)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/S3ExportDestination)
