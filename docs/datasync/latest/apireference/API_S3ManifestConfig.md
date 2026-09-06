---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_S3ManifestConfig.html
---

# S3ManifestConfig
<a name="API_S3ManifestConfig"></a>

Specifies the S3 bucket where you're hosting the manifest that you want AWS DataSync to use. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html).

## Contents
<a name="API_S3ManifestConfig_Contents"></a>

 ** BucketAccessRoleArn **   <a name="DataSync-Type-S3ManifestConfig-BucketAccessRoleArn"></a>
Specifies the AWS Identity and Access Management (IAM) role that allows DataSync to access your manifest. For more information, see [Providing DataSync access to your manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html#transferring-with-manifest-access).
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`
Required: Yes

 ** ManifestObjectPath **   <a name="DataSync-Type-S3ManifestConfig-ManifestObjectPath"></a>
Specifies the Amazon S3 object key of your manifest. This can include a prefix (for example, `prefix/my-manifest.csv`).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`
Required: Yes

 ** S3BucketArn **   <a name="DataSync-Type-S3ManifestConfig-S3BucketArn"></a>
Specifies the Amazon Resource Name (ARN) of the S3 bucket where you're hosting your manifest.
Type: String
Length Constraints: Maximum length of 268.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:[a-z\-0-9]*:[0-9]{12}:accesspoint[/:][a-zA-Z0-9\-.]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]+:[0-9]{12}:outpost[/:][a-zA-Z0-9\-]{1,63}[/:]accesspoint[/:][a-zA-Z0-9\-]{1,63}$|^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):s3:::[a-zA-Z0-9.\-_]{1,255}$`
Required: Yes

 ** ManifestObjectVersionId **   <a name="DataSync-Type-S3ManifestConfig-ManifestObjectVersionId"></a>
Specifies the object version ID of the manifest that you want DataSync to use. If you don't set this, DataSync uses the latest version of the object.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^.+$`
Required: No

## See Also
<a name="API_S3ManifestConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/S3ManifestConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/S3ManifestConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/S3ManifestConfig)
