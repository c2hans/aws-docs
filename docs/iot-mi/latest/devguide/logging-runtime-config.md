---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/logging-runtime-config.html
---

# Configuring runtime logs
<a name="logging-runtime-config"></a>

Runtime log configurations control device-side logging behavior for individual managed things. Use [PutRuntimeLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_PutRuntimeLogConfiguration.html) to set the runtime log configuration for a specific managed thing:

```
aws iot-managed-integrations put-runtime-log-configuration \
    --managed-thing-id "{{your-managed-thing-id}}" \
    --runtime-log-configurations '{"LogLevel":"ERROR","UploadLog":true,"UploadPeriodMinutes":5}'
```

Use [GetRuntimeLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_GetRuntimeLogConfiguration.html) to retrieve the current configuration, or [ResetRuntimeLogConfiguration](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ResetRuntimeLogConfiguration.html) to reset it to defaults.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
