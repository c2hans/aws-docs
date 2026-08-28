---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_EvaluationWindow.html
---

# EvaluationWindow
<a name="API_EvaluationWindow"></a>

The evaluation window that an alarm uses to select the range of metric data that it evaluates each time it runs. This is a union type. Set exactly one of its members, `SlidingWindow` or `WallClockWindow`. If you don't set `EvaluationWindow`, the alarm uses a `SlidingWindow` by default.

For more information, see [Alarm evaluation windows](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation-window.html) in the *CloudWatch User Guide*.

## Contents
<a name="API_EvaluationWindow_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** SlidingWindow **   <a name="ACW-Type-EvaluationWindow-SlidingWindow"></a>
A sliding window, which advances each time the alarm is evaluated, forming a rolling time window. This is the default evaluation window.
Type: [SlidingWindow](API_SlidingWindow.md) object
Required: No

 ** WallClockWindow **   <a name="ACW-Type-EvaluationWindow-WallClockWindow"></a>
A wall clock window, which aligns the evaluated range to fixed clock boundaries that match the alarm's period, such as the top of the hour, midnight, or the start of the calendar week.
Type: [WallClockWindow](API_WallClockWindow.md) object
Required: No

## See Also
<a name="API_EvaluationWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/EvaluationWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/EvaluationWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/EvaluationWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
