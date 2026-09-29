---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-step1.html
---

# Step 1: Configure a device trust provider
<a name="device-posture-step1"></a>

Configure your device trust provider on the endpoint using device posture options. You can set this when you create an endpoint or modify an existing one. Set `Enabled` to `true` to turn on device posture, and provide one or more trust providers. Each trust provider specifies the provider type, your tenant identifier with that provider, and the URL of the provider's public signing key, which Client VPN uses to validate the device posture tokens it receives.

```
aws ec2 create-client-vpn-endpoint \
  --client-cidr-block 10.0.0.0/16 \
  --server-certificate-arn arn:aws:acm:us-east-1:111122223333:certificate/EXAMPLE \
  --authentication-options Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:us-east-1:111122223333:certificate/EXAMPLE} \
  --device-posture-options '{"Enabled":true,"TrustProviders":[{"TrustProviderType":"crowdstrike","TenantId":"EXAMPLE-TENANT-ID","PublicSigningKeyUrl":"https://assets-public.falcon.crowdstrike.com/zta/jwk.json"}]}' \
  --connection-log-options '{"Enabled":true,"CloudwatchLogGroup":"/aws/clientvpn/logs","CloudwatchLogStream":"cvpn-stream","IncludeAuthorizationPolicyContext":true}'
```

You can configure more than one trust provider on a single endpoint (for example, to allow both macOS devices managed by Jamf and Windows devices managed by CrowdStrike). Verify the configuration with `describe-client-vpn-endpoints`; the response includes a `DevicePostureOptions` block listing each configured trust provider.
