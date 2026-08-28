---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_SoftwareTokenMfaConfigType.html
---

# SoftwareTokenMfaConfigType
<a name="API_SoftwareTokenMfaConfigType"></a>

Settings for time-based one-time password (TOTP) multi-factor authentication (MFA) in a user pool. Enables and disables availability of this feature.

This data type is a request parameter of [SetUserPoolMfaConfig](API_SetUserPoolMfaConfig.md) and a response parameter of [GetUserPoolMfaConfig](API_GetUserPoolMfaConfig.md).

## Contents
<a name="API_SoftwareTokenMfaConfigType_Contents"></a>

 ** Enabled **   <a name="CognitoUserPools-Type-SoftwareTokenMfaConfigType-Enabled"></a>
The activation state of TOTP MFA.
Type: Boolean
Required: No

## See Also
<a name="API_SoftwareTokenMfaConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/SoftwareTokenMfaConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/SoftwareTokenMfaConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/SoftwareTokenMfaConfigType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
