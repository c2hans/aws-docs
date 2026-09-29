---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-policies-view.html
---

# View a policy
<a name="device-posture-policies-view"></a>

To retrieve the authorization policy attached to an endpoint, use `get-client-vpn-endpoint-authorization-policy`.

```
aws ec2 get-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE
```
