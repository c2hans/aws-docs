---
source_url: https://docs.aws.amazon.com/greengrass/v1/apireference/definitions-runtimeconfiguration.html
---

End of support notice: On October 7th, 2026, AWS will discontinue support for AWS IoT Greengrass Version 1. After October 7th, 2026, you will no longer be able to access the AWS IoT Greengrass V1 resources. For more information, please visit [Migrate from AWS IoT Greengrass Version 1](https://docs.aws.amazon.com/greengrass/v2/developerguide/migrate-from-v1.html).

# RuntimeConfiguration
<a name="definitions-runtimeconfiguration"></a>

```
{
  "TelemetryConfiguration": {
    "Telemetry": "On|Off",
    "ConfigurationSyncStatus": "InSync|OutOfSync"
  }
}
```

RuntimeConfiguration
Runtime configuration for a thing.
type: object
items: [TelemetryConfiguration](definitions-telemetryconfiguration.md)

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
