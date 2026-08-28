---
source_url: https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_ArtifactDetail.html
---

# ArtifactDetail
<a name="API_ArtifactDetail"></a>

Artifact details for the action execution, such as the artifact location.

## Contents
<a name="API_ArtifactDetail_Contents"></a>

 ** name **   <a name="CodePipeline-Type-ArtifactDetail-name"></a>
The artifact object name for the action execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9_\-]+`
Required: No

 ** s3location **   <a name="CodePipeline-Type-ArtifactDetail-s3location"></a>
The Amazon S3 artifact location for the action execution.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_ArtifactDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codepipeline-2015-07-09/ArtifactDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codepipeline-2015-07-09/ArtifactDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codepipeline-2015-07-09/ArtifactDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CodePipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codepipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
