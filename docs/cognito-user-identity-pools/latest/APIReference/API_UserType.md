---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserType.html
---

# UserType
<a name="API_UserType"></a>

A user profile in a Amazon Cognito user pool.

This data type is a response parameter to [AdminCreateUser](API_AdminCreateUser.md) and [ListUsers](API_ListUsers.md).

## Contents
<a name="API_UserType_Contents"></a>

 ** Attributes **   <a name="CognitoUserPools-Type-UserType-Attributes"></a>
Names and values of a user's attributes, for example `email`.
Type: Array of [AttributeType](API_AttributeType.md) objects
Required: No

 ** Enabled **   <a name="CognitoUserPools-Type-UserType-Enabled"></a>
Indicates whether the user's account is enabled or disabled.
Type: Boolean
Required: No

 ** MFAOptions **   <a name="CognitoUserPools-Type-UserType-MFAOptions"></a>
The user's MFA configuration.
Type: Array of [MFAOptionType](API_MFAOptionType.md) objects
Required: No

 ** UserCreateDate **   <a name="CognitoUserPools-Type-UserType-UserCreateDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** UserLastModifiedDate **   <a name="CognitoUserPools-Type-UserType-UserLastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** Username **   <a name="CognitoUserPools-Type-UserType-Username"></a>
The user's username.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}]+`
Required: No

 ** UserStatus **   <a name="CognitoUserPools-Type-UserType-UserStatus"></a>
The user status. This can be one of the following:
+  `UNCONFIRMED`: User has been created but not confirmed.
+  `CONFIRMED`: User has been confirmed.
+  `EXTERNAL_PROVIDER`: User signed in with a third-party IdP.
+  `RESET_REQUIRED`: User is confirmed, but the user must request a code and reset their password before they can sign in.
+  `FORCE_CHANGE_PASSWORD`: The user is confirmed and the user can sign in using a temporary password, but on first sign-in, the user must change their password to a new value before doing anything else.
The statuses `ARCHIVED`, `UNKNOWN`, and `COMPROMISED` are no longer used.
Type: String
Valid Values: `UNCONFIRMED | CONFIRMED | ARCHIVED | COMPROMISED | UNKNOWN | RESET_REQUIRED | FORCE_CHANGE_PASSWORD | EXTERNAL_PROVIDER`
Required: No

## See Also
<a name="API_UserType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
