---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-policies-delete.html
---

# Delete a policy
<a name="device-posture-policies-delete"></a>

To remove the authorization policy from an endpoint, use `delete-client-vpn-endpoint-authorization-policy`. This stops evaluation for both new connections and existing sessions on the endpoint.

```
aws ec2 delete-client-vpn-endpoint-authorization-policy \
  --client-vpn-endpoint-id cvpn-endpoint-EXAMPLE
```
