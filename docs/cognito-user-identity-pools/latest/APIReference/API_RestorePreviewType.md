---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_RestorePreviewType.html
---

# RestorePreviewType

The number of entities of one type that a point-in-time recovery creates, updates, and deletes.

This data type is a response parameter of [DescribePointInTimeRecovery](API_DescribePointInTimeRecovery.md).

## Contents
<a name="API_RestorePreviewType_Contents"></a>

 ** CreateCount **   <a name="CognitoUserPools-Type-RestorePreviewType-CreateCount"></a>
The number of entities of this type that the recovery creates. These entities existed at the recovery point and were deleted after it.
Type: Long
Required: No

 ** DeleteCount **   <a name="CognitoUserPools-Type-RestorePreviewType-DeleteCount"></a>
The number of entities of this type that the recovery deletes. These entities were created after the recovery point.
Type: Long
Required: No

 ** Entity **   <a name="CognitoUserPools-Type-RestorePreviewType-Entity"></a>
The type of user pool entity that the recovery changes. Can be one of the following values.
Users
User profiles, including their attributes.
Groups
User pool groups.
User MFAs
The MFA settings of users.
Passkeys
The passkeys that users registered.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** UpdateCount **   <a name="CognitoUserPools-Type-RestorePreviewType-UpdateCount"></a>
The number of entities of this type that the recovery reverts to their state at the recovery point. These entities were modified after the recovery point.
Type: Long
Required: No

## See Also
<a name="API_RestorePreviewType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/RestorePreviewType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/RestorePreviewType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/RestorePreviewType)
