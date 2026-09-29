---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-step4.html
---

# Step 4: Enforce the policy
<a name="device-posture-step4"></a>

When you are satisfied with the shadow-mode results, disable shadow mode to start enforcing the policy.

```
aws ec2 modify-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE \
  --shadow-mode disabled
```

**Note**
Client VPN disconnects all active sessions on an endpoint when you add or update a Cedar policy with shadow mode disabled, or when you change shadow mode from enabled to disabled.

To stop evaluating device posture, remove the policy with `delete-client-vpn-endpoint-authorization-policy`. This stops evaluation for both new connections and existing sessions on the endpoint, but the AWS provided client continues to provide a device posture token as long as the client profile contains the `aws-auth-device-posture` directive. To turn off device posture completely, also remove the trust provider from the endpoint's device posture options, then have users download the client configuration again and re-import the profile so that the device posture configuration is no longer present.

For information about monitoring device posture decisions, see [Monitoring AWS Client VPN](monitoring-overview.md). For device posture considerations and limits, see [AWS Client VPN quotas](limits.md).
