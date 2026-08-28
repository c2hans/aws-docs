---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobAbortCriteria.html
---

# AwsJobAbortCriteria
<a name="API_AwsJobAbortCriteria"></a>

The criteria that determine when and how a job abort takes place.

## Contents
<a name="API_AwsJobAbortCriteria_Contents"></a>

 ** action **   <a name="iot-Type-AwsJobAbortCriteria-action"></a>
The type of job action to take to initiate the job abort.
Type: String
Valid Values: `CANCEL`
Required: Yes

 ** failureType **   <a name="iot-Type-AwsJobAbortCriteria-failureType"></a>
The type of job execution failures that can initiate a job abort.
Type: String
Valid Values: `FAILED | REJECTED | TIMED_OUT | ALL`
Required: Yes

 ** minNumberOfExecutedThings **   <a name="iot-Type-AwsJobAbortCriteria-minNumberOfExecutedThings"></a>
The minimum number of things which must receive job execution notifications before the job can be aborted.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** thresholdPercentage **   <a name="iot-Type-AwsJobAbortCriteria-thresholdPercentage"></a>
The minimum percentage of job execution failures that must occur to initiate the job abort.
 AWS IoT Core supports up to two digits after the decimal (for example, 10.9 and 10.99, but not 10.999).
Type: Double
Valid Range: Maximum value of 100.
Required: Yes

## See Also
<a name="API_AwsJobAbortCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AwsJobAbortCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AwsJobAbortCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AwsJobAbortCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
