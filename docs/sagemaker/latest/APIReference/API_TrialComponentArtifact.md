---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrialComponentArtifact.html
---

# TrialComponentArtifact
<a name="API_TrialComponentArtifact"></a>

Represents an input or output artifact of a trial component. You specify `TrialComponentArtifact` as part of the `InputArtifacts` and `OutputArtifacts` parameters in the [CreateTrialComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrialComponent.html) request.

Examples of input artifacts are datasets, algorithms, hyperparameters, source code, and instance types. Examples of output artifacts are metrics, snapshots, logs, and images.

## Contents
<a name="API_TrialComponentArtifact_Contents"></a>

 ** Value **   <a name="sagemaker-Type-TrialComponentArtifact-Value"></a>
The location of the artifact.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*`
Required: Yes

 ** MediaType **   <a name="sagemaker-Type-TrialComponentArtifact-MediaType"></a>
The media type of the artifact, which indicates the type of data in the artifact file. The media type consists of a *type* and a *subtype* concatenated with a slash (/) character, for example, text/csv, image/jpeg, and s3/uri. The type specifies the category of the media. The subtype specifies the kind of data.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[-\w]+\/[-\w+]+`
Required: No

## See Also
<a name="API_TrialComponentArtifact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrialComponentArtifact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrialComponentArtifact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrialComponentArtifact)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
