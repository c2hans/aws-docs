---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-configurations.html
---

# Configuring logging for Managed Integrations
<a name="logging-configurations"></a>

Managed Integrations provides two types of logs delivered to Amazon CloudWatch Logs in your account:
+ *Event logs* – Cloud-side logs capturing events from Managed Integrations workflows. Written to the `/aws/iotmanagedintegrations/EventLog` log group.
+ *Runtime logs* – Device-side logs published by your devices or hubs. Written to the `/aws/iotmanagedintegrations/RuntimeLog` log group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
