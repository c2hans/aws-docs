---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/device-posture-policy-assistant-step1.html
---

# Step 1: Select filters and test the policy
<a name="device-posture-policy-assistant-step1"></a>

In the **Test policy** view, you select filters to load a connection's context, then edit and test your policy against that context. The Client VPN endpoint is selected automatically. You can set the following filters:
+ **Authorization decision** (required) — the most recent allow or deny decision to use from the connection logs.
+ **Device identifier** (optional) — the unique device identifier.
+ **User** (optional) — the user identifier.
+ **Operating system** (optional) — the device operating system.

**To select filters and test a policy**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Client VPN endpoints**, then choose the endpoint ID for the endpoint you want to work with.

1. Choose the **Authorization** tab, then choose **Test policy**.

1. Set **Authorization decision**, which is required. Optionally, set **Device identifier**, **User**, and **Operating system**.

1. Choose **Search connections**. Test policy displays the trust context sent by your device trust provider, the user identity context, and the Cedar authorization policy for the Client VPN endpoint.

1. Review the trust context alongside the policy. Edit the Cedar policy, then choose **Test policy** to evaluate it against the loaded context. Repeat until you are satisfied with the result.

1. Choose **Save**.

**Note**
The trust and identity contexts are static. You can view them alongside the policy to understand what data is available for your policy conditions, but you cannot edit them.
