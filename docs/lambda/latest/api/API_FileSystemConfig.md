---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_FileSystemConfig.html
---

# FileSystemConfig
<a name="API_FileSystemConfig"></a>

Details about the connection between a Lambda function and an [Amazon EFS file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html) or an [Amazon S3 Files file system](https://docs.aws.amazon.com/lambda/latest/dg/configuration-filesystem.html).

## Contents
<a name="API_FileSystemConfig_Contents"></a>

 ** Arn **   <a name="lambda-Type-FileSystemConfig-Arn"></a>
The Amazon Resource Name (ARN) of the Amazon EFS or Amazon S3 Files access point that provides access to the file system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-zA-Z-]*:elasticfilesystem:[a-z]{2}((-gov)|(-iso(b?)))?-[a-z]+-\d{1}:\d{12}:access-point/fsap-[a-f0-9]{17}$|^arn:aws[-a-z]*:s3files:[0-9a-z-:]+:file-system/fs-[0-9a-f]{17,40}/access-point/fsap-[0-9a-f]{17,40}`
Required: Yes

 ** LocalMountPath **   <a name="lambda-Type-FileSystemConfig-LocalMountPath"></a>
The path where the function can access the file system, starting with `/mnt/`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 160.
Pattern: `/mnt/[a-zA-Z0-9-_.]+`
Required: Yes

## See Also
<a name="API_FileSystemConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/FileSystemConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/FileSystemConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/FileSystemConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
