---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-unsubscribe-users.html
---

# Unsubscribe users from user-based product subscriptions in License Manager
<a name="usubs-unsubscribe-users"></a>

You must unsubscribe a user from a Microsoft Office or Visual Studio user-based subscription product to stop incurring charges for them. Microsoft RDS is billed on a per user, per month basis based on a combination of the user subscription and the client access license (CAL) token that's issued from the license server when the user connects to an instance that provides the subscription product. For more information, see [Microsoft RDS billing in License Manager](user-based-subscriptions.md#usubs-billing-rds).

**Important**
For Microsoft Office or Visual Studio user-based subscription products, you must first disassociate the Active Directory user from all instances where they are currently associated before you can unsubscribe them.

**Unsubscribe users from user-based product subscriptions**

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, under **User-based subscriptions**, choose **Products**.

1. Select the product that you want to unsubscribe users from.

1. Select the user names to unsubscribe, then choose **Unsubscribe users**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
