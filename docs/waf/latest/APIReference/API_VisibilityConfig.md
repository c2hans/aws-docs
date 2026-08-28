---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_VisibilityConfig.html
---

# VisibilityConfig
<a name="API_VisibilityConfig"></a>

Defines and enables Amazon CloudWatch metrics and web request sample collection.

## Contents
<a name="API_VisibilityConfig_Contents"></a>

 ** CloudWatchMetricsEnabled **   <a name="WAF-Type-VisibilityConfig-CloudWatchMetricsEnabled"></a>
Indicates whether the associated resource sends metrics to Amazon CloudWatch. For the list of available metrics, see [AWS WAF Metrics](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#waf-metrics) in the * AWS WAF Developer Guide*.
For web ACLs, the metrics are for web requests that have the web ACL default action applied. AWS WAF applies the default action to web requests that pass the inspection of all rules in the web ACL without being either allowed or blocked. For more information, see [The web ACL default action](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-default-action.html) in the * AWS WAF Developer Guide*.
Type: Boolean
Required: Yes

 ** MetricName **   <a name="WAF-Type-VisibilityConfig-MetricName"></a>
A name of the Amazon CloudWatch metric dimension. The name can contain only the characters: A-Z, a-z, 0-9, - (hyphen), and \_ (underscore). The name can be from one to 128 characters long. It can't contain whitespace or metric names that are reserved for AWS WAF, for example `All` and `Default_Action`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[\w#:\.\-/]+$`
Required: Yes

 ** SampledRequestsEnabled **   <a name="WAF-Type-VisibilityConfig-SampledRequestsEnabled"></a>
Indicates whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.
If you configure data protection for the web ACL, the protection applies to the web ACL's sampled web request data.
Request sampling doesn't provide a field redaction option, and any field redaction that you specify in your logging configuration doesn't affect sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.
Type: Boolean
Required: Yes

## See Also
<a name="API_VisibilityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/VisibilityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/VisibilityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/VisibilityConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
