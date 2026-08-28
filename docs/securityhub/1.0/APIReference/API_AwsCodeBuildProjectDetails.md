---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCodeBuildProjectDetails.html
---

# AwsCodeBuildProjectDetails
<a name="API_AwsCodeBuildProjectDetails"></a>

Information about an AWS CodeBuild project.

## Contents
<a name="API_AwsCodeBuildProjectDetails_Contents"></a>

 ** Artifacts **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-Artifacts"></a>
Information about the build artifacts for the CodeBuild project.
Type: Array of [AwsCodeBuildProjectArtifactsDetails](API_AwsCodeBuildProjectArtifactsDetails.md) objects
Required: No

 ** EncryptionKey **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-EncryptionKey"></a>
The AWS KMS key used to encrypt the build output artifacts.
You can specify either the ARN of the KMS key or, if available, the KMS key alias (using the format alias/alias-name).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Environment **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-Environment"></a>
Information about the build environment for this build project.
Type: [AwsCodeBuildProjectEnvironment](API_AwsCodeBuildProjectEnvironment.md) object
Required: No

 ** LogsConfig **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-LogsConfig"></a>
Information about logs for the build project.
Type: [AwsCodeBuildProjectLogsConfigDetails](API_AwsCodeBuildProjectLogsConfigDetails.md) object
Required: No

 ** Name **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-Name"></a>
The name of the build project.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SecondaryArtifacts **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-SecondaryArtifacts"></a>
Information about the secondary artifacts for the CodeBuild project.
Type: Array of [AwsCodeBuildProjectArtifactsDetails](API_AwsCodeBuildProjectArtifactsDetails.md) objects
Required: No

 ** ServiceRole **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-ServiceRole"></a>
The ARN of the IAM role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Source **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-Source"></a>
Information about the build input source code for this build project.
Type: [AwsCodeBuildProjectSource](API_AwsCodeBuildProjectSource.md) object
Required: No

 ** VpcConfig **   <a name="securityhub-Type-AwsCodeBuildProjectDetails-VpcConfig"></a>
Information about the VPC configuration that AWS CodeBuild accesses.
Type: [AwsCodeBuildProjectVpcConfig](API_AwsCodeBuildProjectVpcConfig.md) object
Required: No

## See Also
<a name="API_AwsCodeBuildProjectDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCodeBuildProjectDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCodeBuildProjectDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCodeBuildProjectDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
