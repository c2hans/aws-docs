---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UserPoolClientDescription.html
---

# UserPoolClientDescription
<a name="API_UserPoolClientDescription"></a>

A short description of a user pool app client.

This data type is a response parameter of [ListUserPoolClients](API_ListUserPoolClients.md).

## Contents
<a name="API_UserPoolClientDescription_Contents"></a>

 ** ClientId **   <a name="CognitoUserPools-Type-UserPoolClientDescription-ClientId"></a>
The app client ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: No

 ** ClientName **   <a name="CognitoUserPools-Type-UserPoolClientDescription-ClientName"></a>
The app client name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w\s+=,.@-]+`
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-UserPoolClientDescription-UserPoolId"></a>
The ID of the user pool that's associated with the app client.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_UserPoolClientDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UserPoolClientDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UserPoolClientDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UserPoolClientDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
