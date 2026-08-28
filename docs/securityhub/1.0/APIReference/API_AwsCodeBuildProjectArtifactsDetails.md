---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCodeBuildProjectArtifactsDetails.html
---

# AwsCodeBuildProjectArtifactsDetails
<a name="API_AwsCodeBuildProjectArtifactsDetails"></a>

Information about the build artifacts for the CodeBuild project.

## Contents
<a name="API_AwsCodeBuildProjectArtifactsDetails_Contents"></a>

 ** ArtifactIdentifier **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-ArtifactIdentifier"></a>
An identifier for the artifact definition.
Type: String
Pattern: `.*\S.*`
Required: No

 ** EncryptionDisabled **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-EncryptionDisabled"></a>
Indicates whether to disable encryption on the artifact. Only valid when `Type` is `S3`.
Type: Boolean
Required: No

 ** Location **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-Location"></a>
Only used when `Type` is `S3`. The name of the S3 bucket where the artifact is located.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-Name"></a>
Only used when Type is S3. The name of the artifact. Used with `NamepaceType` and `Path` to determine the pattern for storing the artifact.
Type: String
Pattern: `.*\S.*`
Required: No

 ** NamespaceType **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-NamespaceType"></a>
Only used when `Type` is `S3`. The value to use for the namespace. Used with `Name` and `Path` to determine the pattern for storing the artifact.
Type: String
Pattern: `.*\S.*`
Required: No

 ** OverrideArtifactName **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-OverrideArtifactName"></a>
Whether the name specified in the buildspec file overrides the artifact name.
Type: Boolean
Required: No

 ** Packaging **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-Packaging"></a>
Only used when `Type` is `S3`. The type of output artifact to create.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Path **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-Path"></a>
Only used when `Type` is `S3`. The path to the artifact. Used with `Name` and `NamespaceType` to determine the pattern for storing the artifact.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-AwsCodeBuildProjectArtifactsDetails-Type"></a>
The type of build artifact.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsCodeBuildProjectArtifactsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsCodeBuildProjectArtifactsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsCodeBuildProjectArtifactsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsCodeBuildProjectArtifactsDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
