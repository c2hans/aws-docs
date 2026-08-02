---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-fsx.html
---

# Amazon FSx
<a name="component-configuration-examples-fsx"></a>

The following example shows a component configuration in JSON format for Amazon FSx.

```
{
  "alarmMetrics": [
    {
      "alarmMetricName": "DataReadBytes",
      "monitor": true
    },
    {
      "alarmMetricName": "DataWriteBytes",
      "monitor": true
    },
    {
      "alarmMetricName": "DataReadOperations",
      "monitor": true
    },
    {
      "alarmMetricName": "DataWriteOperations",
      "monitor": true
    },
    {
      "alarmMetricName": "MetadataOperations",
      "monitor": true
    },
    {
      "alarmMetricName": "FreeStorageCapacity",
      "monitor": true
    }
  ]
}
```
