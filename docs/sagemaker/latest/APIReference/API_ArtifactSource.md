---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ArtifactSource.html
---

# ArtifactSource
<a name="API_ArtifactSource"></a>

A structure describing the source of an artifact.

## Contents
<a name="API_ArtifactSource_Contents"></a>

 ** SourceUri **   <a name="sagemaker-Type-ArtifactSource-SourceUri"></a>
The URI of the source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** SourceTypes **   <a name="sagemaker-Type-ArtifactSource-SourceTypes"></a>
A list of source types.
Type: Array of [ArtifactSourceType](API_ArtifactSourceType.md) objects
Required: No

## See Also
<a name="API_ArtifactSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ArtifactSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ArtifactSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ArtifactSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
