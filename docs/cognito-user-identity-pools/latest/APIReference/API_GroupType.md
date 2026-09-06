---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_GroupType.html
---

# GroupType
<a name="API_GroupType"></a>

A user pool group. Contains details about the group and the way that it contributes to IAM role decisions with identity pools. Identity pools can make decisions about the IAM role to assign based on groups: users get credentials for the role associated with their highest-priority group.

This data type is a response parameter of [AdminListGroupsForUser](API_AdminListGroupsForUser.md), [CreateGroup](API_CreateGroup.md), [GetGroup](API_GetGroup.md), [ListGroups](API_ListGroups.md), and [UpdateGroup](API_UpdateGroup.md).

## Contents
<a name="API_GroupType_Contents"></a>

 ** CreationDate **   <a name="CognitoUserPools-Type-GroupType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** Description **   <a name="CognitoUserPools-Type-GroupType-Description"></a>
A friendly description of the group.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

 ** GroupName **   <a name="CognitoUserPools-Type-GroupType-GroupName"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-GroupType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** Precedence **   <a name="CognitoUserPools-Type-GroupType-Precedence"></a>
A non-negative integer value that specifies the precedence of this group relative to the other groups that a user can belong to in the user pool. Zero is the highest precedence value. Groups with lower `Precedence` values take precedence over groups with higher ornull `Precedence` values. If a user belongs to two or more groups, it is the group with the lowest precedence value whose role ARN is given in the user's tokens for the `cognito:roles` and `cognito:preferred_role` claims.
Two groups can have the same `Precedence` value. If this happens, neither group takes precedence over the other. If two groups with the same `Precedence` have the same role ARN, that role is used in the `cognito:preferred_role` claim in tokens for users in each group. If the two groups have different role ARNs, the `cognito:preferred_role` claim isn't set in users' tokens.
The default `Precedence` value is `null`.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** RoleArn **   <a name="CognitoUserPools-Type-GroupType-RoleArn"></a>
The ARN of the IAM role associated with the group. If a group has the highest priority of a user's groups, users who authenticate with an identity pool get credentials for the `RoleArn` that's associated with the group.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:[\w+=/,.@-]+:[\w+=/,.@-]+:([\w+=/,.@-]*)?:[0-9]+:[\w+=/,.@-]+(:[\w+=/,.@-]+)?(:[\w+=/,.@-]+)?`
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-GroupType-UserPoolId"></a>
The ID of the user pool that contains the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_GroupType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/GroupType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/GroupType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/GroupType)
