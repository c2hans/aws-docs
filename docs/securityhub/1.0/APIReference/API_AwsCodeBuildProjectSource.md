---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCodeBuildProjectSource.html
---

# AwsCodeBuildProjectSource
<a name="API_AwsCodeBuildProjectSource"></a>

Information about the build input source code for this build project.

## Contents
<a name="API_AwsCodeBuildProjectSource_Contents"></a>

 ** GitCloneDepth **   <a name="securityhub-Type-AwsCodeBuildProjectSource-GitCloneDepth"></a>
Information about the Git clone depth for the build project.
Type: Integer
Required: No

 ** InsecureSsl **   <a name="securityhub-Type-AwsCodeBuildProjectSource-InsecureSsl"></a>
Whether to ignore SSL warnings while connecting to the project source code.
Type: Boolean
Required: No

 ** Location **   <a name="securityhub-Type-AwsCodeBuildProjectSource-Location"></a>
Information about the location of the source code to be built.
Valid values include:
+ For source code settings that are specified in the source action of a pipeline in AWS CodePipeline, location should not be specified. If it is specified, AWS CodePipeline ignores it. This is because AWS CodePipeline uses the settings in a pipeline's source action instead of this value.
+ For source code in an AWS CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the build spec file (for example, `https://git-codecommit.region-ID.amazonaws.com/v1/repos/repo-name` ).
+ For source code in an S3 input bucket, one of the following.
  + The path to the ZIP file that contains the source code (for example, `bucket-name/path/to/object-name.zip`).
  +  The path to the folder that contains the source code (for example, `bucket-name/path/to/source-code/folder/`).
+ For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the build spec file.
+ For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the build spec file.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsCodeBuildProjectSource-Type"></a>
The type of repository that contains the source code to be built. Valid values are:
+  `BITBUCKET` - The source code is in a Bitbucket repository.
+  `CODECOMMIT` - The source code is in an AWS CodeCommit repository.
+  `CODEPIPELINE` - The source code settings are specified in the source action of a pipeline in AWS CodePipeline.
+  `GITHUB` - The source code is in a GitHub repository.
+  `GITHUB_ENTERPRISE` - The source code is in a GitHub Enterprise repository.
+  `NO_SOURCE` - The project does not have input source code.
+  `S3` - The source code is in an S3 input bucket.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCodeBuildProjectSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCodeBuildProjectSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCodeBuildProjectSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCodeBuildProjectSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
