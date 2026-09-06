---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CollaborationTrainedModelSummary.html
---

# CollaborationTrainedModelSummary
<a name="API_CollaborationTrainedModelSummary"></a>

Provides summary information about a trained model in a collaboration.

## Contents
<a name="API_CollaborationTrainedModelSummary_Contents"></a>

 ** collaborationIdentifier **   <a name="API-Type-CollaborationTrainedModelSummary-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the trained model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** configuredModelAlgorithmAssociationArn **   <a name="API-Type-CollaborationTrainedModelSummary-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that is used for this trained model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationTrainedModelSummary-createTime"></a>
The time at which the trained model was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationTrainedModelSummary-creatorAccountId"></a>
The account ID of the member that created the trained model.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** membershipIdentifier **   <a name="API-Type-CollaborationTrainedModelSummary-membershipIdentifier"></a>
The membership ID of the member that created the trained model.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-CollaborationTrainedModelSummary-name"></a>
The name of the trained model.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** status **   <a name="API-Type-CollaborationTrainedModelSummary-status"></a>
The status of the trained model.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_PENDING | DELETE_IN_PROGRESS | DELETE_FAILED | INACTIVE | CANCEL_PENDING | CANCEL_IN_PROGRESS | CANCEL_FAILED`
Required: Yes

 ** trainedModelArn **   <a name="API-Type-CollaborationTrainedModelSummary-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationTrainedModelSummary-updateTime"></a>
The most recent time at which the trained model was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-CollaborationTrainedModelSummary-description"></a>
The description of the trained model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** incrementalTrainingDataChannels **   <a name="API-Type-CollaborationTrainedModelSummary-incrementalTrainingDataChannels"></a>
Information about the incremental training data channels used to create this version of the trained model.
Type: Array of [IncrementalTrainingDataChannelOutput](API_IncrementalTrainingDataChannelOutput.md) objects
Array Members: Fixed number of 1 item.
Required: No

 ** mlModelTrainingPayerAccountId **   <a name="API-Type-CollaborationTrainedModelSummary-mlModelTrainingPayerAccountId"></a>
The account ID of the member that is responsible for paying for model training costs.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** versionIdentifier **   <a name="API-Type-CollaborationTrainedModelSummary-versionIdentifier"></a>
The version identifier of this trained model version.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_CollaborationTrainedModelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CollaborationTrainedModelSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CollaborationTrainedModelSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CollaborationTrainedModelSummary)
