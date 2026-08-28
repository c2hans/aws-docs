---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/userguide/integrating_how-services-use-secrets_events.html
---

# How Amazon EventBridge uses AWS Secrets Manager
<a name="integrating_how-services-use-secrets_events"></a>

Amazon EventBridge is a serverless event bus service that you can use to connect your applications with data from a variety of sources.

When you create an Amazon EventBridge API destination, EventBridge stores the connection for it in a Secrets Manager [managed secret](service-linked-secrets.md) with the prefix `events`. The cost of storing the secret is included with the charge for using an API destination. To update the secret, you must use EventBridge rather than Secrets Manager. For more information, see [API destinations](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-api-destinations.html) in the *Amazon EventBridge User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Secrets Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query secretsmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
