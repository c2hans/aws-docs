---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/component-configuration-examples-vpc.html
---

# Amazon Virtual Private Cloud (Amazon VPC)
<a name="component-configuration-examples-vpc"></a>

The following example shows a component configuration in JSON format for Amazon VPC.

```
{
  "alarmMetrics": [
    {
      "alarmMetricName": "NetworkAddressUsage",
      "monitor": true
    },
    {
      "alarmMetricName": "NetworkAddressUsagePeered",
      "monitor": true
    },
    {
      "alarmMetricName": "VPCFirewallQueryVolume",
      "monitor": true
    }
  ]
}
```
