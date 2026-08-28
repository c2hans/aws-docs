---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_ImmunityTimeProperty.html
---

# ImmunityTimeProperty
<a name="API_ImmunityTimeProperty"></a>

Used for CAPTCHA and challenge token settings. Determines how long a `CAPTCHA` or challenge timestamp remains valid after AWS WAF updates it for a successful `CAPTCHA` or challenge response.

## Contents
<a name="API_ImmunityTimeProperty_Contents"></a>

 ** ImmunityTime **   <a name="WAF-Type-ImmunityTimeProperty-ImmunityTime"></a>
The amount of time, in seconds, that a `CAPTCHA` or challenge timestamp is considered valid by AWS WAF. The default setting is 300.
For the Challenge action, the minimum setting is 300.
Type: Long
Valid Range: Minimum value of 60. Maximum value of 259200.
Required: Yes

## See Also
<a name="API_ImmunityTimeProperty_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/ImmunityTimeProperty)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/ImmunityTimeProperty)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/ImmunityTimeProperty)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
