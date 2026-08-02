---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_CollaborationTrainedModelExportJobSummary.html
---

# CollaborationTrainedModelExportJobSummary
<a name="API_CollaborationTrainedModelExportJobSummary"></a>

Provides summary information about a trained model export job in a collaboration.

## Contents
<a name="API_CollaborationTrainedModelExportJobSummary_Contents"></a>

 ** collaborationIdentifier **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the trained model export job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** createTime **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-createTime"></a>
The time at which the trained model export job was created.
Type: Timestamp
Required: Yes

 ** creatorAccountId **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-creatorAccountId"></a>
The account ID of the member that created the trained model.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`
Required: Yes

 ** membershipIdentifier **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-membershipIdentifier"></a>
The membership ID of the member that created the trained model export job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** name **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-name"></a>
The name of the trained model export job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

 ** outputConfiguration **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-outputConfiguration"></a>
Information about the output of the trained model export job.
Type: [TrainedModelExportOutputConfiguration](API_TrainedModelExportOutputConfiguration.md) object
Required: Yes

 ** status **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-status"></a>
The status of the trained model.
Type: String
Valid Values: `CREATE_PENDING | CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE`
Required: Yes

 ** trainedModelArn **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-trainedModelArn"></a>
The Amazon Resource Name (ARN) of the trained model that is being exported.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/trained-model/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** updateTime **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-updateTime"></a>
The most recent time at which the trained model export job was updated.
Type: Timestamp
Required: Yes

 ** description **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-description"></a>
The description of the trained model.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** statusDetails **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-statusDetails"></a>
Details about the status of a resource.
Type: [StatusDetails](API_StatusDetails.md) object
Required: No

 ** trainedModelVersionIdentifier **   <a name="API-Type-CollaborationTrainedModelExportJobSummary-trainedModelVersionIdentifier"></a>
The version identifier of the trained model that was exported in this job.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

## See Also
<a name="API_CollaborationTrainedModelExportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/CollaborationTrainedModelExportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/CollaborationTrainedModelExportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/CollaborationTrainedModelExportJobSummary)
