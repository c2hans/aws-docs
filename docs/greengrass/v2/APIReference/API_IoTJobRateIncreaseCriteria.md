---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobRateIncreaseCriteria.html
---

# IoTJobRateIncreaseCriteria
<a name="API_IoTJobRateIncreaseCriteria"></a>

Contains information about criteria to meet before a job increases its rollout rate. Specify either `numberOfNotifiedThings` or `numberOfSucceededThings`.

## Contents
<a name="API_IoTJobRateIncreaseCriteria_Contents"></a>

 ** numberOfNotifiedThings **   <a name="greengrassv2-Type-IoTJobRateIncreaseCriteria-numberOfNotifiedThings"></a>
The number of devices to receive the job notification before the rollout rate increases.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** numberOfSucceededThings **   <a name="greengrassv2-Type-IoTJobRateIncreaseCriteria-numberOfSucceededThings"></a>
The number of devices to successfully run the configuration job before the rollout rate increases.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_IoTJobRateIncreaseCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/IoTJobRateIncreaseCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/IoTJobRateIncreaseCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/IoTJobRateIncreaseCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
