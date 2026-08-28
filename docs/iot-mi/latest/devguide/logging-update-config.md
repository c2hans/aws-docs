---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-update-config.html
---

# Updating event log configurations
<a name="logging-update-config"></a>

You can change the log level at any time using [UpdateEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_UpdateEventLogConfiguration.html):

```
aws iot-managed-integrations update-event-log-configuration \
    --id "{{your-configuration-id}}" \
    --event-log-level "DEBUG"
```

To remove an event log configuration, use [DeleteEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_DeleteEventLogConfiguration.html).

**Important**
Enabling `DEBUG` logging generates significantly more log entries and increases CloudWatch Logs costs. We recommend starting with `ERROR` and only increasing the level when actively troubleshooting an issue.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
