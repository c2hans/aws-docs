---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_HostHeaderConditionConfig.html
---

# HostHeaderConditionConfig
<a name="API_HostHeaderConditionConfig"></a>

Information about a host header condition.

## Contents
<a name="API_HostHeaderConditionConfig_Contents"></a>

 ** RegexValues.member.N **
The regular expressions to compare against the host header. The maximum length of each string is 128 characters.
Type: Array of strings
Required: No

 ** Values.member.N **
The host names. The maximum length of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: \* (matches 0 or more characters) and ? (matches exactly 1 character). You must include at least one "." character. You can include only alphabetical characters after the final "." character.
If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.
Type: Array of strings
Required: No

## See Also
<a name="API_HostHeaderConditionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/HostHeaderConditionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/HostHeaderConditionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/HostHeaderConditionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
