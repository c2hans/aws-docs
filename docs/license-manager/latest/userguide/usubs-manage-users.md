---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-manage-users.html
---

# Manage subscription users for License Manager user-based subscriptions
<a name="usubs-manage-users"></a>

To ensure the accuracy of billing and reporting for Microsoft Office and Visual Studio product subscriptions in License Manager, and to prevent unauthorized access to subscription resources, you can manage user access as follows.

[Disassociate users from an instance](usubs-disassociate-users.md)
Disassociate a user from an instance that hosts a License Manager user-based Microsoft Office or Visual Studio product subscription to remove access to the resource.

[Unsubscribe users](usubs-unsubscribe-users.md)
Unsubscribe users from user-based Microsoft Office or Visual Studio product subscriptions in AWS License Manager to stop incurring subscription charges for those individuals.

**Note**
Deleting a user from Active Directory will not alter user associations or subscriptions for Microsoft Office and Visual Studio products. You must disassociate the user in License Manager from the subscription product details page to remove their association with an instance. Then you must unsubscribe the user.
This topic does not cover Active Directory administration.

**Topics**
+ [Disassociate users from an instance](usubs-disassociate-users.md)
+ [Unsubscribe users](usubs-unsubscribe-users.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
