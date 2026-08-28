---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_DateTimeRange.html
---

# DateTimeRange
<a name="API_DateTimeRange"></a>

A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime`, `endTime`, or `lastUpdatedTime`) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from`. If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to`.

## Contents
<a name="API_DateTimeRange_Contents"></a>

 ** from **   <a name="AWSHealth-Type-DateTimeRange-from"></a>
The starting date and time of a time range.
Type: Timestamp
Required: No

 ** to **   <a name="AWSHealth-Type-DateTimeRange-to"></a>
The ending date and time of a time range.
Type: Timestamp
Required: No

## See Also
<a name="API_DateTimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/DateTimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/DateTimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/DateTimeRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
