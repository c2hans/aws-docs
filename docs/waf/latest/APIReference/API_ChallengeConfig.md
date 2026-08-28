---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ChallengeConfig.html
---

# ChallengeConfig
<a name="API_ChallengeConfig"></a>

Specifies how AWS WAF should handle `Challenge` evaluations. This is available at the web ACL level and in each rule.

## Contents
<a name="API_ChallengeConfig_Contents"></a>

 ** ImmunityTimeProperty **   <a name="WAF-Type-ChallengeConfig-ImmunityTimeProperty"></a>
Determines how long a challenge timestamp in the token remains valid after the client successfully responds to a challenge.
Type: [ImmunityTimeProperty](API_ImmunityTimeProperty.md) object
Required: No

## See Also
<a name="API_ChallengeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ChallengeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ChallengeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ChallengeConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
