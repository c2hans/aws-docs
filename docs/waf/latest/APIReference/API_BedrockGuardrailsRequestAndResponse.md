---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_BedrockGuardrailsRequestAndResponse.html
---

# BedrockGuardrailsRequestAndResponse

Configures the AI security managed rule group to use Amazon Bedrock Guardrails to inspect web requests and the responses to them.

This is used in the `BedrockGuardrails` setting of `AWSManagedRulesAISecurityRuleSet`.

## Contents
<a name="API_BedrockGuardrailsRequestAndResponse_Contents"></a>

 ** RoleArn **   <a name="WAF-Type-BedrockGuardrailsRequestAndResponse-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that AWS WAF uses to call Amazon Bedrock Guardrails for the rule group. The role must be in the same AWS account as the web ACL.
To specify the role, you must have permission to call `iam:PassRole` on it, to pass it to the AWS WAF service principal `wafv2.amazonaws.com`.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:iam::\d{12}:role/(?:[\x21-\x7F]+/)?[\w+=,.@-]+$`
Required: Yes

## See Also
<a name="API_BedrockGuardrailsRequestAndResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/BedrockGuardrailsRequestAndResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/BedrockGuardrailsRequestAndResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/BedrockGuardrailsRequestAndResponse)
