---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-trust-data-jamf.html
---

# Jamf (context.jamf.\*)
<a name="device-posture-trust-data-jamf"></a>

When Jamf is configured as a trust provider, the following fields are available in the Cedar context under the `context.jamf` namespace.

| Field | Type | Description |
| --- | --- | --- |
| risk | string | A Jamf-reported level of risk associated with the device. Valid values: HIGH, MEDIUM, LOW, SECURE, NOT\_APPLICABLE. |
| groups | array of strings | Group IDs from the UEM connector sync. |
| osv | string | The version of the OS currently running, in Apple version number format. |

The following example policy permits access when the reported risk is `LOW` or `SECURE`.

```
permit(principal, action, resource)
when { ["LOW", "SECURE"].contains(context.jamf.risk) };
```
