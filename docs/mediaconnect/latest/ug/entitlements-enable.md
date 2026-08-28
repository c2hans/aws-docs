---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-enable.html
---

# Enabling an entitlement that has been temporarily disabled
<a name="entitlements-enable"></a>

If an entitlement has been [disabled](entitlements-disable.md), you can enable it to start streaming content to the subscriber’s flow again.

**Note**
If the entitlement was [revoked](entitlements-revoke.md), you can't enable it. You must [grant](entitlements-grant.md) a new entitlement.

**To enable an entitlement (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that is associated with the entitlement that you want to enable.

   The details page for that flow appears.

1. Choose the **Entitlements** tab.

1. Choose the entitlement that you want to enable.

1. Choose **Enable**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
