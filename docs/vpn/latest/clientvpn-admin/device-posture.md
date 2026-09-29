---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture.html
---

# Device posture for AWS Client VPN
<a name="device-posture"></a>

With AWS Client VPN device posture, you can control access to your network based on the security health of the connecting device, not just the identity of the user. When device posture is enabled, Client VPN evaluates the health of each device before it grants access, and continues to evaluate it for the life of the session.

To use device posture, you configure a device trust provider (CrowdStrike, Jamf, or JumpCloud) on your Client VPN endpoint. The provider makes a device posture token available on each device — a signed claim that describes the device's health, such as its compliance status or disk encryption state. You define the requirements that a device must meet in an authorization policy. Client VPN evaluates the token against this policy each time a device connects, and again every 5 minutes for the life of the session. Client VPN denies connections and disconnects sessions that do not meet your requirements. For example, you can require that only devices with disk encryption enabled can connect, or that only devices with an active firewall can remain connected.

**Important**
Device posture relies on device trust providers that you configure and manage. AWS does not control or operate these third-party providers. You are responsible for configuring your device trust provider, defining your authorization policy, and ensuring your devices meet your compliance requirements. Client VPN evaluates the device posture tokens that these providers make available, but does not independently verify the health of your devices.

Each device trust provider must also be set up on the connecting device. For links to each provider's setup documentation, see [Supported device trust providers](device-posture-providers.md). Device-side setup steps for your end users are documented in the AWS Client VPN User Guide.
