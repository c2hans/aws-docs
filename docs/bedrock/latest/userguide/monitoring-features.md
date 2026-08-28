---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-features.html
---

# Monitor Amazon Bedrock features
<a name="monitoring-features"></a>

The topics in this section describe observability for Amazon Bedrock features whose monitoring is independent of which inference endpoint you call. These capabilities apply to resources you create or to job state changes, rather than to traffic on the `bedrock-runtime` or `bedrock-mantle` endpoint.

**Topics**
+ [Monitor knowledge bases using CloudWatch Logs](knowledge-bases-logging.md)
+ [Monitor Amazon Bedrock Guardrails using CloudWatch metrics](monitoring-guardrails-cw-metrics.md)
+ [Monitor Amazon Bedrock Agents using CloudWatch Metrics](monitoring-agents-cw-metrics.md)
+ [Monitor Amazon Bedrock job state changes using Amazon EventBridge](monitoring-eventbridge.md)
+ [Monitor Web Search](monitoring-web-search.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
