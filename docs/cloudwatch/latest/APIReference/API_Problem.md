---
source_url: https://docs.aws.amazon.com/cloudwatch/latest/APIReference/API_Problem.html
---

# Problem
<a name="API_Problem"></a>

Describes a problem that is detected by correlating observations.

## Contents
<a name="API_Problem_Contents"></a>

 ** AccountId **   <a name="appinsights-Type-Problem-AccountId"></a>
The AWS account ID for the owner of the resource group affected by the problem.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^\d{12}$`
Required: No

 ** AffectedResource **   <a name="appinsights-Type-Problem-AffectedResource"></a>
The resource affected by the problem.
Type: String
Required: No

 ** EndTime **   <a name="appinsights-Type-Problem-EndTime"></a>
The time when the problem ended, in epoch seconds.
Type: Timestamp
Required: No

 ** Feedback **   <a name="appinsights-Type-Problem-Feedback"></a>
Feedback provided by the user about the problem.
Type: String to string map
Map Entries: Maximum number of 10 items.
Valid Keys: `INSIGHTS_FEEDBACK`
Valid Values: `NOT_SPECIFIED | USEFUL | NOT_USEFUL`
Required: No

 ** Id **   <a name="appinsights-Type-Problem-Id"></a>
The ID of the problem.
Type: String
Length Constraints: Fixed length of 38.
Pattern: `p-[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}`
Required: No

 ** Insights **   <a name="appinsights-Type-Problem-Insights"></a>
A detailed analysis of the problem using machine learning.
Type: String
Required: No

 ** LastRecurrenceTime **   <a name="appinsights-Type-Problem-LastRecurrenceTime"></a>
 The last time that the problem reoccurred after its last resolution.
Type: Timestamp
Required: No

 ** RecurringCount **   <a name="appinsights-Type-Problem-RecurringCount"></a>
 The number of times that the same problem reoccurred after the first time it was resolved.
Type: Long
Required: No

 ** ResolutionMethod **   <a name="appinsights-Type-Problem-ResolutionMethod"></a>
Specifies how the problem was resolved. If the value is `AUTOMATIC`, the system resolved the problem. If the value is `MANUAL`, the user resolved the problem. If the value is `UNRESOLVED`, then the problem is not resolved.
Type: String
Valid Values: `MANUAL | AUTOMATIC | UNRESOLVED`
Required: No

 ** ResourceGroupName **   <a name="appinsights-Type-Problem-ResourceGroupName"></a>
The name of the resource group affected by the problem.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[a-zA-Z0-9\.\-_]*`
Required: No

 ** SeverityLevel **   <a name="appinsights-Type-Problem-SeverityLevel"></a>
A measure of the level of impact of the problem.
Type: String
Valid Values: `Informative | Low | Medium | High`
Required: No

 ** ShortName **   <a name="appinsights-Type-Problem-ShortName"></a>
 The short name of the problem associated with the SNS notification.
Type: String
Required: No

 ** StartTime **   <a name="appinsights-Type-Problem-StartTime"></a>
The time when the problem started, in epoch seconds.
Type: Timestamp
Required: No

 ** Status **   <a name="appinsights-Type-Problem-Status"></a>
The status of the problem.
Type: String
Valid Values: `IGNORE | RESOLVED | PENDING | RECURRING | RECOVERING`
Required: No

 ** Title **   <a name="appinsights-Type-Problem-Title"></a>
The name of the problem.
Type: String
Required: No

 ** Visibility **   <a name="appinsights-Type-Problem-Visibility"></a>
Specifies whether or not you can view the problem. Updates to ignored problems do not generate notifications.
Type: String
Valid Values: `IGNORED | VISIBLE`
Required: No

## See Also
<a name="API_Problem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-insights-2018-11-25/Problem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-insights-2018-11-25/Problem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-insights-2018-11-25/Problem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Application Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
