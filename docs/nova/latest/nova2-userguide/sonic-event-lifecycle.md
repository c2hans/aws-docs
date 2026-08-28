---
source_url: https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-event-lifecycle.html
---

# Event lifecycle
<a name="sonic-event-lifecycle"></a>

The following diagram illustrates the complete bi-directional streaming event lifecycle:

![Bi-directional streaming flow between user, client, and Amazon Bedrock with audio and text.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/Event-Lifecycle-Diagram_1.png)

The bidirectional streaming event lifecycle follows a structured pattern from session initialization through conversation completion. Each conversation involves input events (from your application) and output events (from Amazon Nova 2 Sonic) that work together to create natural voice interactions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Nova. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query nova` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
