---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RateIncreaseCriteria.html
---

# RateIncreaseCriteria
<a name="API_RateIncreaseCriteria"></a>

Allows you to define a criteria to initiate the increase in rate of rollout for a job.

## Contents
<a name="API_RateIncreaseCriteria_Contents"></a>

 ** numberOfNotifiedThings **   <a name="iot-Type-RateIncreaseCriteria-numberOfNotifiedThings"></a>
The threshold for number of notified things that will initiate the increase in rate of rollout.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** numberOfSucceededThings **   <a name="iot-Type-RateIncreaseCriteria-numberOfSucceededThings"></a>
The threshold for number of succeeded things that will initiate the increase in rate of rollout.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_RateIncreaseCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RateIncreaseCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RateIncreaseCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RateIncreaseCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
