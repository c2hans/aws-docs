---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CandidateProperties.html
---

# CandidateProperties
<a name="API_CandidateProperties"></a>

The properties of an AutoML candidate job.

## Contents
<a name="API_CandidateProperties_Contents"></a>

 ** CandidateArtifactLocations **   <a name="sagemaker-Type-CandidateProperties-CandidateArtifactLocations"></a>
The Amazon S3 prefix to the artifacts generated for an AutoML candidate.
Type: [CandidateArtifactLocations](API_CandidateArtifactLocations.md) object
Required: No

 ** CandidateMetrics **   <a name="sagemaker-Type-CandidateProperties-CandidateMetrics"></a>
Information about the candidate metrics for an AutoML job.
Type: Array of [MetricDatum](API_MetricDatum.md) objects
Array Members: Minimum number of 0 items. Maximum number of 40 items.
Required: No

## See Also
<a name="API_CandidateProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CandidateProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CandidateProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CandidateProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
