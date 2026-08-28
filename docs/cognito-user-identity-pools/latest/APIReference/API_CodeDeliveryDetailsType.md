---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CodeDeliveryDetailsType.html
---

# CodeDeliveryDetailsType
<a name="API_CodeDeliveryDetailsType"></a>

The delivery details for an email or SMS message that Amazon Cognito sent for authentication or verification.

This data type is a response parameter of operations that send a code for user profile confirmation, verification, or management, for example [ForgotPassword](API_ForgotPassword.md) and [SignUp](API_SignUp.md).

## Contents
<a name="API_CodeDeliveryDetailsType_Contents"></a>

 ** AttributeName **   <a name="CognitoUserPools-Type-CodeDeliveryDetailsType-AttributeName"></a>
The name of the attribute that Amazon Cognito verifies with the code.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+`
Required: No

 ** DeliveryMedium **   <a name="CognitoUserPools-Type-CodeDeliveryDetailsType-DeliveryMedium"></a>
The method that Amazon Cognito used to send the code.
Type: String
Valid Values: `SMS | EMAIL`
Required: No

 ** Destination **   <a name="CognitoUserPools-Type-CodeDeliveryDetailsType-Destination"></a>
The email address or phone number destination where Amazon Cognito sent the code.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 131072.
Required: No

## See Also
<a name="API_CodeDeliveryDetailsType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/CodeDeliveryDetailsType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/CodeDeliveryDetailsType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/CodeDeliveryDetailsType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
