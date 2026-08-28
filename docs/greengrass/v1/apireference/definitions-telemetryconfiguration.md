---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-telemetryconfiguration.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# TelemetryConfiguration
<a name="definitions-telemetryconfiguration"></a>

```
{
  "Telemetry": "On|Off",
  "ConfigurationSyncStatus": "InSync|OutOfSync"
}
```

TelemetryConfiguration
The configuration settings to run telemetry.
type: object
required: ["Telemetry"]

Telemetry
The configuration setting to turn on or turn off telemetry.
type: string
enum: ["On", "Off"]

ConfigurationSyncStatus
The synchronization status of the device-reported configuration with the desired configuration.
type: string
enum: ["InSync", "OutOfSync"]

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Greengrass. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query greengrass` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
