---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingRuleUpdate.html
---

# SamplingRuleUpdate
<a name="API_SamplingRuleUpdate"></a>

A document specifying changes to a sampling rule's configuration.

## Contents
<a name="API_SamplingRuleUpdate_Contents"></a>

 ** Attributes **   <a name="xray-Type-SamplingRuleUpdate-Attributes"></a>
Matches attributes derived from the request.
Type: String to string map
Map Entries: Maximum number of 5 items.
Key Length Constraints: Minimum length of 1. Maximum length of 32.
Value Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** FixedRate **   <a name="xray-Type-SamplingRuleUpdate-FixedRate"></a>
The percentage of matching requests to instrument, after the reservoir is exhausted.
Type: Double
Required: No

 ** Host **   <a name="xray-Type-SamplingRuleUpdate-Host"></a>
Matches the hostname from a request URL.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** HTTPMethod **   <a name="xray-Type-SamplingRuleUpdate-HTTPMethod"></a>
Matches the HTTP method of a request.
Type: String
Length Constraints: Maximum length of 10.
Required: No

 ** Priority **   <a name="xray-Type-SamplingRuleUpdate-Priority"></a>
The priority of the sampling rule.
Type: Integer
Required: No

 ** ReservoirSize **   <a name="xray-Type-SamplingRuleUpdate-ReservoirSize"></a>
A fixed number of matching requests to instrument per second, prior to applying the fixed rate. The reservoir is not used directly by services, but applies to all services using the rule collectively.
Type: Integer
Required: No

 ** ResourceARN **   <a name="xray-Type-SamplingRuleUpdate-ResourceARN"></a>
Matches the ARN of the AWS resource on which the service runs.
Type: String
Length Constraints: Maximum length of 500.
Required: No

 ** RuleARN **   <a name="xray-Type-SamplingRuleUpdate-RuleARN"></a>
The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.
Type: String
Required: No

 ** RuleName **   <a name="xray-Type-SamplingRuleUpdate-RuleName"></a>
The name of the sampling rule. Specify a rule by either name or ARN, but not both.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** SamplingRateBoost **   <a name="xray-Type-SamplingRuleUpdate-SamplingRateBoost"></a>
Specifies the multiplier applied to the base sampling rate. This boost allows you to temporarily increase sampling without changing the rule's configuration.
Type: [SamplingRateBoost](API_SamplingRateBoost.md) object
Required: No

 ** ServiceName **   <a name="xray-Type-SamplingRuleUpdate-ServiceName"></a>
Matches the `name` that the service uses to identify itself in segments.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** ServiceType **   <a name="xray-Type-SamplingRuleUpdate-ServiceType"></a>
Matches the `origin` that the service uses to identify its type in segments.
Type: String
Length Constraints: Maximum length of 64.
Required: No

 ** URLPath **   <a name="xray-Type-SamplingRuleUpdate-URLPath"></a>
Matches the path from a request URL.
Type: String
Length Constraints: Maximum length of 128.
Required: No

## See Also
<a name="API_SamplingRuleUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingRuleUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingRuleUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingRuleUpdate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
