---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_ExclusionWindow.html
---

# ExclusionWindow
<a name="API_ExclusionWindow"></a>

The core SLO time window exclusion object that includes Window, StartTime, RecurrenceRule, and Reason.

## Contents
<a name="API_ExclusionWindow_Contents"></a>

 ** Window **   <a name="applicationsignals-Type-ExclusionWindow-Window"></a>
The SLO time window exclusion .
Type: [Window](API_Window.md) object
Required: Yes

 ** Reason **   <a name="applicationsignals-Type-ExclusionWindow-Reason"></a>
A description explaining why this time period should be excluded from SLO calculations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** RecurrenceRule **   <a name="applicationsignals-Type-ExclusionWindow-RecurrenceRule"></a>
The recurrence rule for the SLO time window exclusion. Supports both cron and rate expressions.
Type: [RecurrenceRule](API_RecurrenceRule.md) object
Required: No

 ** StartTime **   <a name="applicationsignals-Type-ExclusionWindow-StartTime"></a>
The start of the SLO time window exclusion. Defaults to current time if not specified.
Type: Timestamp
Required: No

## See Also
<a name="API_ExclusionWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/ExclusionWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/ExclusionWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/ExclusionWindow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Signals. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query applicationsignals` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
