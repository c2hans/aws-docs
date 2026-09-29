---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-providers-config.html
---

# Configuring a trust provider
<a name="device-posture-providers-config"></a>

For each trust provider you configure on an endpoint, supply these values in the endpoint's device posture options:

**Trust provider fields**

| Field | Example | Description |
| --- | --- | --- |
| TrustProviderType | crowdstrike, jamf, jumpcloud | The type of device trust provider. |
| TenantId | EXAMPLE-TENANT-ID | Your tenant identifier with the provider. |
| PublicSigningKeyUrl | https://assets-public.falcon.crowdstrike.com/zta/jwk.json | The URL of the provider's public signing key. This example is specific to CrowdStrike. |

**Note**
`PublicSigningKeyUrl` is not required when the trust provider type is `jamf`.
