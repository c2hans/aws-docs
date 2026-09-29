---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-providers.html
---

# Supported device trust providers
<a name="device-posture-providers"></a>

AWS Client VPN device posture supports the following device trust providers. You configure each one on your endpoint. The provider makes a device posture token available on the connecting device, which Client VPN evaluates against your authorization policy.

**Provider support by operating system**

| Device trust provider | Supported operating systems |
| --- | --- |
| CrowdStrike | macOS, Windows |
| Jamf | macOS |
| JumpCloud | macOS, Windows, Ubuntu |

Each provider documents how to set up device trust on the connecting device. For more information, see the following documentation on each provider's website:
+ CrowdStrike — [CrowdStrike Zero Trust Assessment](https://developer.crowdstrike.com/falcon-mcp/modules/zero-trust-assessment/)
+ Jamf — [Jamf Trusted Access](https://trusted.jamf.com/docs/enabling-access-for-trusted-devices)
+ JumpCloud — [JumpCloud Device Trust](https://www.jumpcloud.com/support/understand-device-trust-readiness)
