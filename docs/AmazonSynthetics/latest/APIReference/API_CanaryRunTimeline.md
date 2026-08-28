---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunTimeline.html
---

# CanaryRunTimeline
<a name="API_CanaryRunTimeline"></a>

This structure contains the start and end times of a single canary run.

## Contents
<a name="API_CanaryRunTimeline_Contents"></a>

 ** Completed **   <a name="synthetics-Type-CanaryRunTimeline-Completed"></a>
The end time of the run.
Type: Timestamp
Required: No

 ** MetricTimestampForRunAndRetries **   <a name="synthetics-Type-CanaryRunTimeline-MetricTimestampForRunAndRetries"></a>
The time at which the metrics will be generated for this run or retries.
Type: Timestamp
Required: No

 ** Started **   <a name="synthetics-Type-CanaryRunTimeline-Started"></a>
The start time of the run.
Type: Timestamp
Required: No

## See Also
<a name="API_CanaryRunTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryRunTimeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryRunTimeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryRunTimeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
