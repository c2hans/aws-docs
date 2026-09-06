---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoMLCandidate.html
---

# AutoMLCandidate
<a name="API_AutoMLCandidate"></a>

Information about a candidate produced by an AutoML training job, including its status, steps, and other properties.

## Contents
<a name="API_AutoMLCandidate_Contents"></a>

 ** CandidateName **   <a name="sagemaker-Type-AutoMLCandidate-CandidateName"></a>
The name of the candidate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** CandidateStatus **   <a name="sagemaker-Type-AutoMLCandidate-CandidateStatus"></a>
The candidate's status.
Type: String
Valid Values: `Completed | InProgress | Failed | Stopped | Stopping`
Required: Yes

 ** CandidateSteps **   <a name="sagemaker-Type-AutoMLCandidate-CandidateSteps"></a>
Information about the candidate's steps.
Type: Array of [AutoMLCandidateStep](API_AutoMLCandidateStep.md) objects
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-AutoMLCandidate-CreationTime"></a>
The creation time.
Type: Timestamp
Required: Yes

 ** LastModifiedTime **   <a name="sagemaker-Type-AutoMLCandidate-LastModifiedTime"></a>
The last modified time.
Type: Timestamp
Required: Yes

 ** ObjectiveStatus **   <a name="sagemaker-Type-AutoMLCandidate-ObjectiveStatus"></a>
The objective's status.
Type: String
Valid Values: `Succeeded | Pending | Failed`
Required: Yes

 ** CandidateProperties **   <a name="sagemaker-Type-AutoMLCandidate-CandidateProperties"></a>
The properties of an AutoML candidate job.
Type: [CandidateProperties](API_CandidateProperties.md) object
Required: No

 ** EndTime **   <a name="sagemaker-Type-AutoMLCandidate-EndTime"></a>
The end time.
Type: Timestamp
Required: No

 ** FailureReason **   <a name="sagemaker-Type-AutoMLCandidate-FailureReason"></a>
The failure reason.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** FinalAutoMLJobObjectiveMetric **   <a name="sagemaker-Type-AutoMLCandidate-FinalAutoMLJobObjectiveMetric"></a>
The best candidate result from an AutoML training job.
Type: [FinalAutoMLJobObjectiveMetric](API_FinalAutoMLJobObjectiveMetric.md) object
Required: No

 ** InferenceContainerDefinitions **   <a name="sagemaker-Type-AutoMLCandidate-InferenceContainerDefinitions"></a>
The mapping of all supported processing unit (CPU, GPU, etc...) to inference container definitions for the candidate. This field is populated for the AutoML jobs V2 (for example, for jobs created by calling `CreateAutoMLJobV2`) related to image or text classification problem types only.
Type: String to array of [AutoMLContainerDefinition](API_AutoMLContainerDefinition.md) objects map
Map Entries: Minimum number of 0 items. Maximum number of 2 items.
Valid Keys: `CPU | GPU`
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** InferenceContainers **   <a name="sagemaker-Type-AutoMLCandidate-InferenceContainers"></a>
Information about the recommended inference container definitions.
Type: Array of [AutoMLContainerDefinition](API_AutoMLContainerDefinition.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_AutoMLCandidate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoMLCandidate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoMLCandidate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoMLCandidate)
