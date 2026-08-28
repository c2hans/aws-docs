---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-mantle.html
---

# Monitor the `bedrock-mantle` endpoint
<a name="monitoring-mantle"></a>

The `bedrock-mantle.{{region}}.api.aws` endpoint serves the OpenAI Responses API, the OpenAI Chat Completions API, and the Anthropic Messages API. The topics in this section describe the observability options available for traffic to this endpoint, including Amazon CloudWatch metrics and AWS CloudTrail logging.

If your application calls the `bedrock-runtime.{{region}}.amazonaws.com` endpoint, see [Monitor the `bedrock-runtime` endpoint](monitoring.md) instead.

**Topics**
+ [Monitor `bedrock-mantle` inference using CloudWatch metrics](monitoring-mantle-metrics.md)
+ [Monitor `bedrock-mantle` API calls using CloudTrail](logging-cloudtrail-mantle.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
