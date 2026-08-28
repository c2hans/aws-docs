---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_QueryStringConditionConfig.html
---

# QueryStringConditionConfig
<a name="API_QueryStringConditionConfig"></a>

Information about a query string condition.

The query string component of a URI starts after the first '?' character and is terminated by either a '\#' character or the end of the URI. A typical query string contains key/value pairs separated by '&' characters. The allowed characters are specified by RFC 3986. Any character can be percentage encoded.

## Contents
<a name="API_QueryStringConditionConfig_Contents"></a>

 ** Values.member.N **
The key/value pairs or values to find in the query string. The maximum length of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: \* (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal '\*' or '?' character in a query string, you must escape these characters in `Values` using a '\\' character.
If you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.
Type: Array of [QueryStringKeyValuePair](API_QueryStringKeyValuePair.md) objects
Required: No

## See Also
<a name="API_QueryStringConditionConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/QueryStringConditionConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/QueryStringConditionConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/QueryStringConditionConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
