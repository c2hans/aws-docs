---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_ClientSecretDescriptorType.html
---

# ClientSecretDescriptorType
<a name="API_ClientSecretDescriptorType"></a>

Contains information about a client secret, including its unique identifier, value, and creation timestamp.

## Contents
<a name="API_ClientSecretDescriptorType_Contents"></a>

 ** ClientSecretCreateDate **   <a name="CognitoUserPools-Type-ClientSecretDescriptorType-ClientSecretCreateDate"></a>
The date and time when the client secret was created.
Type: Timestamp
Required: No

 ** ClientSecretId **   <a name="CognitoUserPools-Type-ClientSecretDescriptorType-ClientSecretId"></a>
The unique identifier for the client secret. This identifier follows the format <client-id>--<epoch-create-time>.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ClientSecretValue **   <a name="CognitoUserPools-Type-ClientSecretDescriptorType-ClientSecretValue"></a>
The actual secret value. This is only returned when creating a new secret and only if Amazon Cognito generated the secret. For custom secrets that you provide, this field is not included in the response.
Type: String
Length Constraints: Minimum length of 24. Maximum length of 64.
Pattern: `[\w+]+`
Required: No

## See Also
<a name="API_ClientSecretDescriptorType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/ClientSecretDescriptorType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/ClientSecretDescriptorType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/ClientSecretDescriptorType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cognito User Pools. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cognito-user-identity-pools` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
