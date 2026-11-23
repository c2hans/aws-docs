---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RestorationType.html
---

# RestorationType

The details of a point-in-time recovery of a user pool.

This data type is a response parameter of [InitiatePointInTimeRecovery](API_InitiatePointInTimeRecovery.md), [DescribePointInTimeRecovery](API_DescribePointInTimeRecovery.md), [StartPointInTimeRecovery](API_StartPointInTimeRecovery.md), and [CancelPointInTimeRecovery](API_CancelPointInTimeRecovery.md).

## Contents
<a name="API_RestorationType_Contents"></a>

 ** RestoreId **   <a name="CognitoUserPools-Type-RestorationType-RestoreId"></a>
The ID of the recovery. Use this ID in requests to describe, start, or cancel the recovery.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}$`
Required: No

 ** RestorePreview **   <a name="CognitoUserPools-Type-RestorationType-RestorePreview"></a>
The recovery preview. For each type of entity, the preview shows the number of entities that the recovery creates, updates, and deletes. The preview doesn't include user data. Amazon Cognito returns the preview when it's available.
Type: Array of [RestorePreviewType](API_RestorePreviewType.md) objects
Required: No

 ** RestoreStatus **   <a name="CognitoUserPools-Type-RestorationType-RestoreStatus"></a>
The status of the recovery. Can be one of the following values.
PREVIEW\_GENERATING
Amazon Cognito is generating the recovery preview, which might not be available immediately. Write operations in the user pool are paused.
PREVIEW\_GENERATED
The recovery preview is ready for review. Write operations in the user pool are paused. Within 24 hours after you initiate the recovery, apply it with a `StartPointInTimeRecovery` request or discard it with a `CancelPointInTimeRecovery` request.
PREVIEW\_CANCELLED
You canceled the recovery. Amazon Cognito resumed write operations and didn't change your user pool data.
PREVIEW\_GENERATION\_FAILED
Amazon Cognito couldn't generate the recovery preview. Amazon Cognito resumed write operations and didn't change your user pool data. You can initiate a new recovery.
PREVIEW\_EXPIRED
You didn't start or cancel the recovery within 24 hours after you initiated it. Amazon Cognito resumed write operations and didn't change your user pool data.
RESTORING
Amazon Cognito is restoring user data in the user pool to its state at the recovery point. Write operations in the user pool are paused.
RESTORE\_COMPLETED
Amazon Cognito restored your user pool to its state at the recovery point and resumed write operations.
TEMPORARY\_INTERNAL\_ERROR\_SEE\_SUPPORT\_CASE
The recovery encountered an internal error. Write operations in the user pool remain paused. AWS Support contacts you through a support case to resolve the issue.
AWS\_ABORTED
Amazon Cognito stopped the recovery because of an internal failure. Write operations in the user pool remain paused, and you can't cancel or retry the recovery. AWS Support contacts you through a support case to resolve the issue.
Type: String
Valid Values: `PREVIEW_GENERATING | PREVIEW_GENERATED | PREVIEW_CANCELLED | PREVIEW_GENERATION_FAILED | PREVIEW_EXPIRED | RESTORING | RESTORE_COMPLETED | TEMPORARY_INTERNAL_ERROR_SEE_SUPPORT_CASE | AWS_ABORTED`
Required: No

 ** RestoreTimestamp **   <a name="CognitoUserPools-Type-RestorationType-RestoreTimestamp"></a>
The point in time that the recovery restores the user pool to.
Type: Timestamp
Required: No

 ** TriggerTimestamp **   <a name="CognitoUserPools-Type-RestorationType-TriggerTimestamp"></a>
The end of the period of changes that the recovery reverts. This time is shortly after the time that you initiated the recovery. The recovery reverts changes to user data that occurred between `RestoreTimestamp` and `TriggerTimestamp`.
Type: Timestamp
Required: No

## See Also
<a name="API_RestorationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RestorationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RestorationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RestorationType)
