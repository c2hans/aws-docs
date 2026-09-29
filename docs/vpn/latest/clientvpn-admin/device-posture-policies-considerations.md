---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-policies-considerations.html
---

# Considerations when writing policies
<a name="device-posture-policies-considerations"></a>

Keep the following in mind when you write authorization policies.
+ A policy document can be a maximum of 10,000 bytes.
+ Namespace availability depends on your trust provider configuration. A namespace is available only when you have configured the corresponding trust provider on the endpoint.
+ User identity signals are captured once when the device connects, and do not change during a session.
