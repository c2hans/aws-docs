---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ArtifactSummary.html
---

# ArtifactSummary
<a name="API_ArtifactSummary"></a>

Lists a summary of the properties of an artifact. An artifact represents a URI addressable object or data. Some examples are a dataset and a model.

## Contents
<a name="API_ArtifactSummary_Contents"></a>

 ** ArtifactArn **   <a name="sagemaker-Type-ArtifactSummary-ArtifactArn"></a>
The Amazon Resource Name (ARN) of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:artifact/.*`
Required: No

 ** ArtifactName **   <a name="sagemaker-Type-ArtifactSummary-ArtifactName"></a>
The name of the artifact.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: No

 ** ArtifactType **   <a name="sagemaker-Type-ArtifactSummary-ArtifactType"></a>
The type of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** CreationTime **   <a name="sagemaker-Type-ArtifactSummary-CreationTime"></a>
When the artifact was created.
Type: Timestamp
Required: No

 ** LastModifiedTime **   <a name="sagemaker-Type-ArtifactSummary-LastModifiedTime"></a>
When the artifact was last modified.
Type: Timestamp
Required: No

 ** Source **   <a name="sagemaker-Type-ArtifactSummary-Source"></a>
The source of the artifact.
Type: [ArtifactSource](API_ArtifactSource.md) object
Required: No

## See Also
<a name="API_ArtifactSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ArtifactSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ArtifactSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ArtifactSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
