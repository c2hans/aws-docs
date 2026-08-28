---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolDescriptionType.html
---

# UserPoolDescriptionType
<a name="API_UserPoolDescriptionType"></a>

A short description of a user pool.

This data type is a response parameter of [ListUserPools](API_ListUserPools.md).

## Contents
<a name="API_UserPoolDescriptionType_Contents"></a>

 ** CreationDate **   <a name="CognitoUserPools-Type-UserPoolDescriptionType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** Id **   <a name="CognitoUserPools-Type-UserPoolDescriptionType-Id"></a>
The user pool ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

 ** LambdaConfig **   <a name="CognitoUserPools-Type-UserPoolDescriptionType-LambdaConfig"></a>
A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of user pool operations. Triggers can modify the outcome of the operations that invoked them.
Type: [LambdaConfigType](API_LambdaConfigType.md) object
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-UserPoolDescriptionType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** Name **   <a name="CognitoUserPools-Type-UserPoolDescriptionType-Name"></a>
The user pool name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: No

 ** ReplicaRegions **   <a name="CognitoUserPools-Type-UserPoolDescriptionType-ReplicaRegions"></a>
A list of AWS Regions where replicas of this user pool exist.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** Status **   <a name="CognitoUserPools-Type-UserPoolDescriptionType-Status"></a>
 *This member has been deprecated.*
The user pool status.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

## See Also
<a name="API_UserPoolDescriptionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolDescriptionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolDescriptionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolDescriptionType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
