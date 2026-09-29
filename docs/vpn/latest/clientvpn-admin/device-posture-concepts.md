---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-concepts.html
---

# Concepts
<a name="device-posture-concepts"></a>

The following concepts are central to how device posture works.

**Device trust provider**
The configuration on an endpoint that represents your third-party device trust vendor (CrowdStrike, Jamf, or JumpCloud). In the API, device trust providers are configured under `DevicePostureOptions`, which has an `Enabled` field that you must set to `true` to turn on device posture, and a `TrustProviders` list. Each entry has a `TrustProviderType` of `crowdstrike`, `jamf`, or `jumpcloud`. You can configure one or more trust providers on an endpoint.

**Device posture token**
A signed claim, made available on the device by the device trust provider, that describes the device's health, such as compliance status, disk encryption state, or a risk score. The device posture token is the input Client VPN evaluates to decide whether a device meets your requirements. The AWS provided client refreshes the token on its own schedule, independently of Client VPN's policy re-evaluation.

**Authorization policy**
A policy, written in the Cedar policy language, that defines the requirements a connection must meet. You attach one policy to an endpoint. Client VPN evaluates it when a device connects and on each re-evaluation during the session.

**Shadow mode**
A mode in which Client VPN evaluates the authorization policy and records the decision in your connection logs without blocking any connections. Use shadow mode to validate a policy against real traffic before you enforce it.
