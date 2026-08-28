---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/rule-function-conditions.html
---

# Conditions in Connect Customer Rules Function language
<a name="rule-function-conditions"></a>

A rule function needs to start with either an AND or OR Operator. The Operands of AND or OR Operators is a list of conditions. Conditions vary depending on the TriggerEventSource.

Following are the conditions that you can use.

**Topics**
+ [OnMetricDataUpdate](OnMetricDataUpdate.md)
+ [OnContactEvaluationSubmit](OnContactEvaluationSubmit.md)
+ [OnPostCallAnalysisAvailable](OnPostCallAnalysisAvailable.md)
+ [OnRealTimeCallAnalysisAvailable](OnRealTimeCallAnalysisAvailable.md)
+ [OnPostChatAnalysisAvailable](OnPostChatAnalysisAvailable.md)
+ [OnEmailAnalysisAvailable](OnEmailAnalysisAvailable.md)
+ [OnZendeskTicketCreate](OnZendeskTicketCreate.md)
+ [OnZendeskTicketStatusUpdate](OnZendeskTicketStatusUpdate.md)
+ [OnSalesforceCaseCreate](OnSalesforceCaseCreate.md)
+ [OnCaseCreate](OnCaseCreate.md)
+ [OnCaseUpdate](OnCaseUpdate.md)
+ [OnSlaBreach](OnSlaBreach.md)
+ [PatternMatch Operands](patternmatch-operands.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
