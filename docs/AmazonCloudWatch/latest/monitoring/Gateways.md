---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Gateways.html
---

# Gateways
<a name="Gateways"></a>

Monitor how your agents discover and interact with external tools and services through AgentCore Gateway. For more information on Amazon Bedrock AgentCore Gateway, see [Amazon Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html). Gateway observability includes comprehensive monitoring across multiple areas:
+ Track API transformation success rates and response times for external service calls
+ Monitor tool discovery patterns and usage frequency across different agents
+ Analyze authentication and authorization flows for third-party service access
+ Observe data transformation accuracy when converting between different API formats
+ Track error rates and retry patterns for external service integrations

![Gateways view.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/Gateways.png)

Expand the **View details** section to view the gateway metrics in graphs.

![Gateways metrics view.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/Gateway_metrics.png)

Under **Gateways**, choose a gateway **Name** to view the dashboard. You can also sort the list of gateways by click the column headers in the table.

![Gateways details view.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/Gateways_tile.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
