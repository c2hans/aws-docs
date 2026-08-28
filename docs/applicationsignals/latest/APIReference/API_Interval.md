---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_Interval.html
---

# Interval
<a name="API_Interval"></a>

The time period used to evaluate the SLO. It can be either a calendar interval or rolling interval.

## Contents
<a name="API_Interval_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** CalendarInterval **   <a name="applicationsignals-Type-Interval-CalendarInterval"></a>
If the interval is a calendar interval, this structure contains the interval specifications.
Type: [CalendarInterval](API_CalendarInterval.md) object
Required: No

 ** RollingInterval **   <a name="applicationsignals-Type-Interval-RollingInterval"></a>
If the interval is a rolling interval, this structure contains the interval specifications.
Type: [RollingInterval](API_RollingInterval.md) object
Required: No

## See Also
<a name="API_Interval_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/Interval)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/Interval)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/Interval)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
