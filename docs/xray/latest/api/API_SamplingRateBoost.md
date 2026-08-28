---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_SamplingRateBoost.html
---

# SamplingRateBoost
<a name="API_SamplingRateBoost"></a>

Enable temporary sampling rate increases when you detect anomalies to improve visibility.

## Contents
<a name="API_SamplingRateBoost_Contents"></a>

 ** CooldownWindowMinutes **   <a name="xray-Type-SamplingRateBoost-CooldownWindowMinutes"></a>
Sets the time window (in minutes) in which only one sampling rate boost can be triggered. After a boost occurs, no further boosts are allowed until the next window.
Type: Integer
Valid Range: Minimum value of 0.
Required: Yes

 ** MaxRate **   <a name="xray-Type-SamplingRateBoost-MaxRate"></a>
Defines max temporary sampling rate to apply when a boost is triggered. Calculated boost rate by X-Ray will be less than or equal to this max rate.
Type: Double
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

## See Also
<a name="API_SamplingRateBoost_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/SamplingRateBoost)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/SamplingRateBoost)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/SamplingRateBoost)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS X-Ray. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query xray` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
