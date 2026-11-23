---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RestorationDescriptionType.html
---

# RestorationDescriptionType

A summary of a point-in-time recovery of a user pool.

This data type is a response parameter of [ListPointInTimeRecoveries](API_ListPointInTimeRecoveries.md).

## Contents
<a name="API_RestorationDescriptionType_Contents"></a>

 ** RestoreId **   <a name="CognitoUserPools-Type-RestorationDescriptionType-RestoreId"></a>
The ID of the recovery.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}$`
Required: No

 ** RestoreStatus **   <a name="CognitoUserPools-Type-RestorationDescriptionType-RestoreStatus"></a>
The status of the recovery. For a description of each status, see the `RestoreStatus` parameter of `RestorationType`.
Type: String
Valid Values: `PREVIEW_GENERATING | PREVIEW_GENERATED | PREVIEW_CANCELLED | PREVIEW_GENERATION_FAILED | PREVIEW_EXPIRED | RESTORING | RESTORE_COMPLETED | TEMPORARY_INTERNAL_ERROR_SEE_SUPPORT_CASE | AWS_ABORTED`
Required: No

 ** RestoreTimestamp **   <a name="CognitoUserPools-Type-RestorationDescriptionType-RestoreTimestamp"></a>
The point in time that the recovery restores the user pool to.
Type: Timestamp
Required: No

## See Also
<a name="API_RestorationDescriptionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RestorationDescriptionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RestorationDescriptionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RestorationDescriptionType)
