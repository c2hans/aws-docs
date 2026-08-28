---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-web-search.html
---

# Monitor Web Search
<a name="monitoring-web-search"></a>

Web Search on Amazon Bedrock is integrated with AWS CloudTrail. CloudTrail captures API activity for Web Search so you can audit who invoked the tool, when, and from where.

Web Search activity is recorded as CloudTrail data events. Data events are not logged by default. To capture them, create a trail (or event data store) and enable data event logging for Web Search. For the steps, see [Logging data events with AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html). Additional charges apply for data events.

Once data event logging is enabled, CloudTrail captures the following for each recorded call:
+ The identity that invoked the action
+ The time the call occurred
+ The specific `bedrock-websearch` action that was called
+ The source identity, including the forward access sessions (FAS) session originator
+ The account and Region context of the request

Access-denied outcomes are only logged when you opt into data event delivery for `bedrock-websearch`. Otherwise they are not reported. An `AccessDenied` event includes the specific condition key that caused the request to be denied, which helps you diagnose policy issues.

By design, CloudTrail does not expose the query text, the URLs, or the raw search results from Web Search. Query text is treated the same way as an inference prompt.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
