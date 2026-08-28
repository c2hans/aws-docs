---
source_url: https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdateCognitoUserPoolConfiguration.html
---

# UpdateCognitoUserPoolConfiguration
<a name="API_UpdateCognitoUserPoolConfiguration"></a>

Contains configuration details of a Amazon Cognito user pool for use with an identity source.

## Contents
<a name="API_UpdateCognitoUserPoolConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** userPoolArn **   <a name="verifiedpermissions-Type-UpdateCognitoUserPoolConfiguration-userPoolArn"></a>
The [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Amazon Cognito user pool associated with this identity source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-zA-Z0-9-]+:cognito-idp:(([a-zA-Z0-9-]+:\d{12}:userpool/[\w-]+_[0-9a-zA-Z]+))`
Required: Yes

 ** clientIds **   <a name="verifiedpermissions-Type-UpdateCognitoUserPoolConfiguration-clientIds"></a>
The client ID of an app client that is configured for the specified Amazon Cognito user pool.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1000 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

 ** groupConfiguration **   <a name="verifiedpermissions-Type-UpdateCognitoUserPoolConfiguration-groupConfiguration"></a>
The configuration of the user groups from an Amazon Cognito user pool identity source.
Type: [UpdateCognitoGroupConfiguration](API_UpdateCognitoGroupConfiguration.md) object
Required: No

## See Also
<a name="API_UpdateCognitoUserPoolConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/verifiedpermissions-2021-12-01/UpdateCognitoUserPoolConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/verifiedpermissions-2021-12-01/UpdateCognitoUserPoolConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/verifiedpermissions-2021-12-01/UpdateCognitoUserPoolConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Verified Permissions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query verifiedpermissions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
