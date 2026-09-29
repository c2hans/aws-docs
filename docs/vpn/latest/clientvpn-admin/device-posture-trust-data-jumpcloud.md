---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-trust-data-jumpcloud.html
---

# JumpCloud (context.jumpcloud.\*)
<a name="device-posture-trust-data-jumpcloud"></a>

When JumpCloud is configured as a trust provider, the following fields are available in the Cedar context under the `context.jumpcloud` namespace.

| Field | Type | Description |
| --- | --- | --- |
| device.is\_managed | boolean | Indicates whether the device is under management. |
| org\_id | string | The JumpCloud organization ID. |
| system | string | The JumpCloud system ID. |
| durt\_id | string | Device User Refresh Token ID. A unique ID that represents the device and user combination. |

The following example policy permits access when the device is under management.

```
permit(principal, action, resource)
when { context.jumpcloud.device.is_managed == true };
```
