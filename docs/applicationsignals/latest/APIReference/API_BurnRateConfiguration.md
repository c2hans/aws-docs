---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BurnRateConfiguration.html
---

# BurnRateConfiguration
<a name="API_BurnRateConfiguration"></a>

This object defines the length of the look-back window used to calculate one burn rate metric for this SLO. The burn rate measures how fast the service is consuming the error budget, relative to the attainment goal of the SLO. A burn rate of exactly 1 indicates that the SLO goal will be met exactly.

For example, if you specify 60 as the number of minutes in the look-back window, the burn rate is calculated as the following:

 *burn rate = error rate over the look-back window / (100% - attainment goal percentage)*

For more information about burn rates, see [Calculate burn rates](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html#CloudWatch-ServiceLevelObjectives-burn).

## Contents
<a name="API_BurnRateConfiguration_Contents"></a>

 ** LookBackWindowMinutes **   <a name="applicationsignals-Type-BurnRateConfiguration-LookBackWindowMinutes"></a>
The number of minutes to use as the look-back window.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10080.
Required: Yes

## See Also
<a name="API_BurnRateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BurnRateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BurnRateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BurnRateConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
