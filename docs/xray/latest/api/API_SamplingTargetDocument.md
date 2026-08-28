---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingTargetDocument.html
---

# SamplingTargetDocument
<a name="API_SamplingTargetDocument"></a>

Temporary changes to a sampling rule configuration. To meet the global sampling target for a rule, X-Ray calculates a new reservoir for each service based on the recent sampling results of all services that called [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html).

## Contents
<a name="API_SamplingTargetDocument_Contents"></a>

 ** FixedRate **   <a name="xray-Type-SamplingTargetDocument-FixedRate"></a>
The percentage of matching requests to instrument, after the reservoir is exhausted.
Type: Double
Required: No

 ** Interval **   <a name="xray-Type-SamplingTargetDocument-Interval"></a>
The number of seconds for the service to wait before getting sampling targets again.
Type: Integer
Required: No

 ** ReservoirQuota **   <a name="xray-Type-SamplingTargetDocument-ReservoirQuota"></a>
The number of requests per second that X-Ray allocated for this service.
Type: Integer
Required: No

 ** ReservoirQuotaTTL **   <a name="xray-Type-SamplingTargetDocument-ReservoirQuotaTTL"></a>
When the reservoir quota expires.
Type: Timestamp
Required: No

 ** RuleName **   <a name="xray-Type-SamplingTargetDocument-RuleName"></a>
The name of the sampling rule.
Type: String
Required: No

 ** SamplingBoost **   <a name="xray-Type-SamplingTargetDocument-SamplingBoost"></a>
The sampling boost that X-Ray allocated for this service.
Type: [SamplingBoost](API_SamplingBoost.md) object
Required: No

## See Also
<a name="API_SamplingTargetDocument_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingTargetDocument)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingTargetDocument)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingTargetDocument)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
