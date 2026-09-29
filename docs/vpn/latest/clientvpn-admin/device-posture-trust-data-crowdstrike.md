---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-trust-data-crowdstrike.html
---

# CrowdStrike (context.crowdstrike.\*)
<a name="device-posture-trust-data-crowdstrike"></a>

When CrowdStrike is configured as a trust provider, the following fields are available in the Cedar context under the `context.crowdstrike` namespace.

| Field | Type | Description |
| --- | --- | --- |
| assessment.overall | integer | A single metric between 1-100 that is a weighted average of the OS and sensor config scores. |
| assessment.os | integer | A single metric between 1-100 that accounts for OS-specific settings monitored on the host. |
| assessment.sensor\_config | integer | A single metric between 1-100 that accounts for the sensor policies monitored on the host. |
| assessment.version | string | The version of the scoring algorithm. |
| cid | string | Customer ID (CID) unique to the customer's environment. |
| platform | string | Operating system of the endpoint (Windows 10, Windows 11, or macOS). |
| serial\_number | string | The serial number of the device. |

The following example policy permits access when the overall assessment score is greater than 50.

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };
```
