---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CognitoConfig.html
---

# CognitoConfig
<a name="API_CognitoConfig"></a>

Use this parameter to configure your Amazon Cognito workforce. A single Cognito workforce is created using and corresponds to a single [ Amazon Cognito user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html).

## Contents
<a name="API_CognitoConfig_Contents"></a>

 ** ClientId **   <a name="sagemaker-Type-CognitoConfig-ClientId"></a>
The client ID for your Amazon Cognito user pool.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[ -~]+`
Required: Yes

 ** UserPool **   <a name="sagemaker-Type-CognitoConfig-UserPool"></a>
A [ user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) is a user directory in Amazon Cognito. With a user pool, your users can sign in to your web or mobile app through Amazon Cognito. Your users can also sign in through social identity providers like Google, Facebook, Amazon, or Apple, and through SAML identity providers.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 55.
Pattern: `[\w-]+_[0-9a-zA-Z]+`
Required: Yes

## See Also
<a name="API_CognitoConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CognitoConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CognitoConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CognitoConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
