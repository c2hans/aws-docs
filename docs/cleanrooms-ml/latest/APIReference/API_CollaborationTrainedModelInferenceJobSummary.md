---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CollaborationTrainedModelInferenceJobSummary.html
---

# CollaborationTrainedModelInferenceJobSummary
<a name="API_CollaborationTrainedModelInferenceJobSummary"></a>

Provides summary information about a trained model inference job in a collaboration.

## Contents
<a name="API_CollaborationTrainedModelInferenceJobSummary_Contents"></a>

 ** collaborationIdentifier **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the trained model inference job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-createTime"></a>
The time at which the trained model inference job was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-creatorAccountId"></a>
The account ID that created the trained model inference job.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** membershipIdentifier **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-membershipIdentifier"></a>
The membership ID of the membership that contains the trained model inference job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-name"></a>
The name of the trained model inference job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** outputConfiguration **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-outputConfiguration"></a>
Returns output configuration information for the trained model inference job.
Type: [InferenceOutputConfiguration](API_InferenceOutputConfiguration.md) object
Required: Yes

 ** status **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-status"></a>
The status of the trained model inference job.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | CANCEL_PENDING | CANCEL_IN_PROGRESS | CANCEL_FAILED | INACTIVE`
Required: Yes

 ** trainedModelArn **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model that is used for the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** trainedModelInferenceJobArn **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-trainedModelInferenceJobArn"></a>
The Amazon Resource Name (ARN) of the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model-inference-job/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-updateTime"></a>
The most recent time at which the trained model inference job was updated.
Type: Timestamp
Required: Yes

 ** configuredModelAlgorithmAssociationArn **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that is used for the trained model inference job.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: No

 ** description **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-description"></a>
The description of the trained model inference job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** logsStatus **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-logsStatus"></a>
The trained model inference job logs status.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`
Required: No

 ** logsStatusDetails **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-logsStatusDetails"></a>
Details about the logs status for the trained model inference job.
Type: String
Required: No

 ** metricsStatus **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-metricsStatus"></a>
the trained model inference job metrics status.
Type: String
Valid Values: `PUBLISH_SUCCEEDED | PUBLISH_FAILED`
Required: No

 ** metricsStatusDetails **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-metricsStatusDetails"></a>
Details about the metrics status for trained model inference job.
Type: String
Required: No

 ** mlModelInferencePayerAccountId **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-mlModelInferencePayerAccountId"></a>
The account ID of the member that is responsible for paying for model inference costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** trainedModelVersionIdentifier **   <a name="API-Type-CollaborationTrainedModelInferenceJobSummary-trainedModelVersionIdentifier"></a>
The version identifier of the trained model that was used for inference in this job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_CollaborationTrainedModelInferenceJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CollaborationTrainedModelInferenceJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CollaborationTrainedModelInferenceJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CollaborationTrainedModelInferenceJobSummary)
