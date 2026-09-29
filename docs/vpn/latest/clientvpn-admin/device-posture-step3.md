---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-step3.html
---

# Step 3: Test the policy in shadow mode
<a name="device-posture-step3"></a>

Attach the policy with shadow mode enabled. In shadow mode, Client VPN evaluates the policy and records the decision in your connection logs, but never blocks a connection.

```
aws ec2 modify-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE \
  --policy-document 'permit(principal, action, resource) when { context.crowdstrike.assessment.overall > 50 };' \
  --description "Require CrowdStrike ZTA" \
  --shadow-mode enabled
```

Confirm the attached policy with `get-client-vpn-endpoint-authorization-policy`.
