---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_TimeRange.html
---

# TimeRange
<a name="API_TimeRange"></a>

A structure that defines the time range that you want to retrieve results from.

## Contents
<a name="API_TimeRange_Contents"></a>

 ** After **   <a name="cloudwatchrum-Type-TimeRange-After"></a>
The beginning of the time range to retrieve performance events from.
Type: Long
Required: Yes

 ** Before **   <a name="cloudwatchrum-Type-TimeRange-Before"></a>
The end of the time range to retrieve performance events from. If you omit this, the time range extends to the time that this operation is performed.
Type: Long
Required: No

## See Also
<a name="API_TimeRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/TimeRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/TimeRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/TimeRange)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
