---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-prerequisites.html
---

# Prerequisites
<a name="device-posture-prerequisites"></a>

Before you configure device posture, make sure you have the following.
+ An account with a supported device trust provider (CrowdStrike, Jamf, or JumpCloud), configured on each device that connects. For details, see [Supported device trust providers](device-posture-providers.md).
+ The AWS provided client, version 6.2.0 or later. Device posture is not supported with third-party OpenVPN clients.
+ A Client VPN endpoint, either an existing one or a new one that you create when you configure device posture.
