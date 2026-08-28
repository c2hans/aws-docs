---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingBoost.html
---

# SamplingBoost
<a name="API_SamplingBoost"></a>

Temporary boost sampling rate. X-Ray calculates sampling boost for each service based on the recent sampling boost stats of all services that called [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html).

## Contents
<a name="API_SamplingBoost_Contents"></a>

 ** BoostRate **   <a name="xray-Type-SamplingBoost-BoostRate"></a>
The calculated sampling boost rate for this service
Type: Double
Required: Yes

 ** BoostRateTTL **   <a name="xray-Type-SamplingBoost-BoostRateTTL"></a>
When the sampling boost expires.
Type: Timestamp
Required: Yes

## See Also
<a name="API_SamplingBoost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingBoost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingBoost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingBoost)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
