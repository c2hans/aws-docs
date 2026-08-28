---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobAbortCriteria.html
---

# IoTJobAbortCriteria
<a name="API_IoTJobAbortCriteria"></a>

Contains criteria that define when and how to cancel a job.

The deployment stops if the following conditions are true:

1. The number of things that receive the deployment exceeds the `minNumberOfExecutedThings`.

1. The percentage of failures with type `failureType` exceeds the `thresholdPercentage`.

## Contents
<a name="API_IoTJobAbortCriteria_Contents"></a>

 ** action **   <a name="greengrassv2-Type-IoTJobAbortCriteria-action"></a>
The action to perform when the criteria are met.
Type: String
Valid Values: `CANCEL`
Required: Yes

 ** failureType **   <a name="greengrassv2-Type-IoTJobAbortCriteria-failureType"></a>
The type of job deployment failure that can cancel a job.
Type: String
Valid Values: `FAILED | REJECTED | TIMED_OUT | ALL`
Required: Yes

 ** minNumberOfExecutedThings **   <a name="greengrassv2-Type-IoTJobAbortCriteria-minNumberOfExecutedThings"></a>
The minimum number of things that receive the configuration before the job can cancel.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** thresholdPercentage **   <a name="greengrassv2-Type-IoTJobAbortCriteria-thresholdPercentage"></a>
The minimum percentage of `failureType` failures that occur before the job can cancel.
This parameter supports up to two digits after the decimal (for example, you can specify `10.9` or `10.99`, but not `10.999`).
Type: Double
Valid Range: Maximum value of 100.
Required: Yes

## See Also
<a name="API_IoTJobAbortCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/IoTJobAbortCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/IoTJobAbortCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/IoTJobAbortCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
