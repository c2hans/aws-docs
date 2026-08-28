---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/entitlements-disable.html
---

# Disabling an entitlement temporarily
<a name="entitlements-disable"></a>

When you disable an entitlement, the content becomes unavailable to the subscriber account immediately. However, the entitlement and the associated output remain on your flow. These resources continue to count toward your quota for outputs and entitlements. Later, you can [enable the entitlement](entitlements-enable.md) to re-instate access.

If you want to stop streaming content to the subscriber’s flow permanently, [revoke](entitlements-revoke.md) the entitlement instead. That action removes the entitlement and the associated output from your flow.

**To disable an entitlement (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that is associated with the entitlement that you want to disable.

   The details page for that flow appears.

1. Choose the **Entitlements** tab.

1. Choose the entitlement that you want to disable.

1. Choose **Disable**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
