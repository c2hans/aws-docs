---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_UICustomizationType.html
---

# UICustomizationType
<a name="API_UICustomizationType"></a>

A container for the UI customization information for the hosted UI in a user pool.

This data type is a response parameter of [DescribeUserPoolClient](API_DescribeUserPoolClient.md).

## Contents
<a name="API_UICustomizationType_Contents"></a>

 ** ClientId **   <a name="CognitoUserPools-Type-UICustomizationType-ClientId"></a>
The app client ID for your UI customization. When this value isn't present, the customization applies to all user pool app clients that don't have client-level settings..
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\w+]+`
Required: No

 ** CreationDate **   <a name="CognitoUserPools-Type-UICustomizationType-CreationDate"></a>
The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** CSS **   <a name="CognitoUserPools-Type-UICustomizationType-CSS"></a>
The CSS values in the UI customization.
To get a template with your UI customization options, make a [GetUICustomization](API_GetUICustomization.md) request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

 ** CSSVersion **   <a name="CognitoUserPools-Type-UICustomizationType-CSSVersion"></a>
The CSS version number.
Type: String
Required: No

 ** ImageUrl **   <a name="CognitoUserPools-Type-UICustomizationType-ImageUrl"></a>
A URL path to the hosted logo image of your UI customization.
Type: String
Required: No

 ** LastModifiedDate **   <a name="CognitoUserPools-Type-UICustomizationType-LastModifiedDate"></a>
The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java `Date` object.
Type: Timestamp
Required: No

 ** UserPoolId **   <a name="CognitoUserPools-Type-UICustomizationType-UserPoolId"></a>
The ID of the user pool with hosted UI customizations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: No

## See Also
<a name="API_UICustomizationType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/UICustomizationType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/UICustomizationType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/UICustomizationType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
