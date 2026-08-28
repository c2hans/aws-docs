---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-create-config.html
---

# Creating event log configurations
<a name="logging-create-config"></a>

Use the [CreateEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_CreateEventLogConfiguration.html) API action to enable event logging for a resource type. We recommend creating a separate configuration for each resource type, using `*` as the resource identifier to capture logs for all resources of that type. Start at the `ERROR` log level to receive all failure logs without generating excessive volume or cost.

```
aws iot-managed-integrations create-event-log-configuration \
    --resource-type "managed-thing" \
    --resource-id "*" \
    --event-log-level "ERROR"
```

Repeat for each resource type:

```
aws iot-managed-integrations create-event-log-configuration \
    --resource-type "credential-locker" \
    --resource-id "*" \
    --event-log-level "ERROR"

aws iot-managed-integrations create-event-log-configuration \
    --resource-type "provisioning-profile" \
    --resource-id "*" \
    --event-log-level "ERROR"

aws iot-managed-integrations create-event-log-configuration \
    --resource-type "ota-task" \
    --resource-id "*" \
    --event-log-level "ERROR"

aws iot-managed-integrations create-event-log-configuration \
    --resource-type "account-association" \
    --resource-id "*" \
    --event-log-level "ERROR"
```

After you call `CreateEventLogConfiguration`, logs are pushed to the `/aws/iotmanagedintegrations/EventLog` log group in CloudWatch Logs. Use [ListEventLogConfigurations](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ListEventLogConfigurations.html) to view all configurations, or [GetEventLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetEventLogConfiguration.html) to retrieve a specific configuration by ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
