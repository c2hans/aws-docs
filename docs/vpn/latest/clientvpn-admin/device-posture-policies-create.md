---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-policies-create.html
---

# Create or update a policy
<a name="device-posture-policies-create"></a>

To attach or replace the authorization policy on an endpoint, use `modify-client-vpn-endpoint-authorization-policy`.

```
aws ec2 modify-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE \
  --policy-document 'permit(principal, action, resource) when { context.crowdstrike.assessment.overall > 50 };' \
  --description "Require CrowdStrike ZTA" \
  --shadow-mode enabled
```
