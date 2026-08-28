---
source_url: https://docs.aws.amazon.com/license-manager/latest/userguide/usubs-deregister-ad.html
---

# Deregister an Active Directory from License Manager settings
<a name="usubs-deregister-ad"></a>

You can deregister an Active Directory from License Manager settings if you no longer want to use it for user-based subscriptions. Deregistering the directory configuration from License Manager settings doesn't delete the directory. When you deregister the directory from the settings, you can no longer associate users from that directory for user-based subscriptions in License Manager.

If you have multiple Active Directories registered, deregistering one directory does not affect instances or user associations for your other registered directories.

**Prerequisites**
Before you deregister the directory from License Manager settings, you must perform the following tasks:

1. [Disassociate users from an instance](usubs-disassociate-users.md) from each instance that references the directory that you want to deregister.

1. After all of the subscription users are disassociated from the instance, terminate the instance. Repeat until all instances associated with the Active Directory you are deregistering are terminated. Instances associated with other registered Active Directories are not affected.

1. You also need to [Unsubscribe users](usubs-unsubscribe-users.md) that belong to the Active Directory you will deregister to stop incurring changes for them.

**Deregister**

**Important**
If your Active Directory is used for Microsoft RDS SAL users, you must delete the associated license server endpoint before you deregister and delete the AD.

**Deregister the Active Directory from License Manager settings**

After you've completed all of the prerequisite tasks, open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the left navigation pane, choose **Settings**.

1. On the **Settings** page, under the AWS Managed Microsoft AD section, choose **Remove**.

1. Enter the required text to confirm that you want to remove the directory and choose **Remove**.

After you choose **Remove**, the **AWS Managed Microsoft AD** section on the **Settings** page displays your **Directory ID** with the **Status** of **Configuring**. Once the configuration process is complete, the directory is removed from the **AWS Managed Microsoft AD** section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
