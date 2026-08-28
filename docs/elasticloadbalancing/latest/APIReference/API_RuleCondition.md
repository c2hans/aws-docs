---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_RuleCondition.html
---

# RuleCondition
<a name="API_RuleCondition"></a>

Information about a condition for a rule.

Each rule can optionally include up to one of each of the following conditions: `http-request-method`, `host-header`, `path-pattern`, and `source-ip`. Each rule can also optionally include one or more of each of the following conditions: `http-header` and `query-string`. Note that the value for a condition can't be empty.

For Network Load Balancer listener rules, the only supported condition is `source-ip`. Use `SourceIpConfig` with `IpAddressType` to match on the IP address type of the source traffic (`ipv4` or `ipv6`).

For more information, see [Quotas for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html).

## Contents
<a name="API_RuleCondition_Contents"></a>

 ** Field **
The name of the field. The possible values are:
+  `http-header` – [ALB] Matches on an HTTP header field.
+  `http-request-method` – [ALB] Matches on the HTTP request method.
+  `host-header` – [ALB] Matches on the host header.
+  `path-pattern` – [ALB] Matches on the URL path of the request.
+  `query-string` – [ALB] Matches on a query string parameter.
+  `source-ip` – [ALB, NLB] Matches on the source IP address. For ALB, use `SourceIpConfig` with `Values` to specify CIDR ranges. For NLB, use `SourceIpConfig` with `IpAddressType` to match the IP address type (`ipv4` or `ipv6`).
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** HostHeaderConfig **
Information for a host header condition. Specify only when `Field` is `host-header`.
Type: [HostHeaderConditionConfig](API_HostHeaderConditionConfig.md) object
Required: No

 ** HttpHeaderConfig **
Information for an HTTP header condition. Specify only when `Field` is `http-header`.
Type: [HttpHeaderConditionConfig](API_HttpHeaderConditionConfig.md) object
Required: No

 ** HttpRequestMethodConfig **
Information for an HTTP method condition. Specify only when `Field` is `http-request-method`.
Type: [HttpRequestMethodConditionConfig](API_HttpRequestMethodConditionConfig.md) object
Required: No

 ** PathPatternConfig **
Information for a path pattern condition. Specify only when `Field` is `path-pattern`.
Type: [PathPatternConditionConfig](API_PathPatternConditionConfig.md) object
Required: No

 ** QueryStringConfig **
Information for a query string condition. Specify only when `Field` is `query-string`.
Type: [QueryStringConditionConfig](API_QueryStringConditionConfig.md) object
Required: No

 ** RegexValues.member.N **
The regular expressions to match against the condition field. The maximum length of each string is 128 characters. Specify only when `Field` is `http-header`, `host-header`, or `path-pattern`.
Type: Array of strings
Required: No

 ** SourceIpConfig **
Information for a source IP condition. Specify only when `Field` is `source-ip`.
Type: [SourceIpConditionConfig](API_SourceIpConditionConfig.md) object
Required: No

 ** Values.member.N **
The condition value. Specify only when `Field` is `host-header` or `path-pattern`. Alternatively, to specify multiple host names or multiple path patterns, use `HostHeaderConfig` or `PathPatternConfig`.
If `Field` is `host-header` and you are not using `HostHeaderConfig`, you can specify a single host name (for example, my.example.com) in `Values`. A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.
+ A-Z, a-z, 0-9
+ - .
+ \* (matches 0 or more characters)
+ ? (matches exactly 1 character)
If `Field` is `path-pattern` and you are not using `PathPatternConfig`, you can specify a single path pattern (for example, /img/\*) in `Values`. A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.
+ A-Z, a-z, 0-9
+ \_ - . $ / \~ " ' @ : \+
+ & (using &amp;)
+ \* (matches 0 or more characters)
+ ? (matches exactly 1 character)
Type: Array of strings
Required: No

## See Also
<a name="API_RuleCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/RuleCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/RuleCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/RuleCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Elastic Load Balancing. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticloadbalancing` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
