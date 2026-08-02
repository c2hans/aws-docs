---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_ResolvedArtifact.html
---

# ResolvedArtifact
<a name="API_ResolvedArtifact"></a>

Represents a resolved build artifact. A resolved artifact is an artifact that is built and deployed to the destination, such as Amazon S3.

## Contents
<a name="API_ResolvedArtifact_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** identifier **   <a name="CodeBuild-Type-ResolvedArtifact-identifier"></a>
The identifier of the artifact.
Type: String
Required: No

 ** location **   <a name="CodeBuild-Type-ResolvedArtifact-location"></a>
The location of the artifact.
Type: String
Required: No

 ** type **   <a name="CodeBuild-Type-ResolvedArtifact-type"></a>
Specifies the type of artifact.
Type: String
Valid Values: `CODEPIPELINE | S3 | NO_ARTIFACTS`
Required: No

## See Also
<a name="API_ResolvedArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/ResolvedArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/ResolvedArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/ResolvedArtifact)
