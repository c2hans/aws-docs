---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-step2.html
---

# Step 2: Author an authorization policy
<a name="device-posture-step2"></a>

An authorization policy is a Cedar document that defines the requirements a connection must meet. Client VPN evaluates the policy against a context made up of three kinds of information:
+ Device signals — the health signals carried in the device posture token. Namespaces: `context.crowdstrike.*`, `context.jamf.*`, `context.jumpcloud.*`.
+ User identity — captured once when the device connects. Namespace depends on auth type: `context.saml.*`, `context.active-directory.*`, or `context.mutual-authentication.*`.
+ Connection details — always available: `context.connection.*` (endpoint ID, connection ID, platform, platform version, public IP address, client OpenVPN version, and AWS provided client version).

```
permit(principal, action, resource)
when { context.crowdstrike.assessment.overall > 50 };
```

For more examples, the policy API, and guidance on writing conditions, see [Authoring device posture authorization policies](device-posture-policies.md).
