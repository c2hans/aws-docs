---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Investigations-SuggestionTypes.html
---

# Insights that CloudWatch investigations can surface in investigations
<a name="Investigations-SuggestionTypes"></a>

CloudWatch investigations can surface the following types of items and add them to the **Suggestions** tab of an investigation. For hypotheses involving multiple resources, visual diagrams may also be provided to illustrate causal relationships.
+ Hypotheses about root causes
+ CloudWatch alarms, including both metric alarms and composite alarms
+ CloudWatch metrics
+ AWS Health events
+ Change events logged in CloudTrail
+ X-Ray trace data
+ CloudWatch Logs Insights queries for log groups in the Standard log class
+ CloudWatch Contributor Insights data
+ CloudWatch Application Signals data
+ CloudWatch Database Insights data

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
