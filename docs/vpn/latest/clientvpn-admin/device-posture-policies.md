---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-policies.html
---

# Authoring device posture authorization policies
<a name="device-posture-policies"></a>

A device posture authorization policy defines the requirements a device must meet to connect to your Client VPN endpoint and to stay connected. You write the policy in Cedar, an open-source policy language. Client VPN evaluates the policy against a context that combines the device posture token, the authenticated user identity, and the connection details, and returns an allow or deny decision.

For an introduction to the Cedar language and its syntax, see the [Cedar documentation](https://docs.cedarpolicy.com/) and the [Cedar policy syntax reference](https://docs.cedarpolicy.com/policies/syntax-policy.html).
