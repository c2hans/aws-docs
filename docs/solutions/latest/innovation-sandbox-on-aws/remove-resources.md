---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/remove-resources.html
---

# End leases and eject accounts
<a name="remove-resources"></a>

## Enable maintenance mode
<a name="enable-maintenance-mode"></a>

Enable maintenance mode before you continue, so that managers and users cannot make API requests to the solution while you remove leases and accounts.

1. Log in to the web UI as an **Administrator**.

1. From the left pane, choose **Settings**, then choose the **General** tab.

1. Under **Maintenance Mode**, turn on the **Maintenance mode** toggle, and choose **Save**.

1. On the confirmation dialog, choose **Turn on maintenance mode**.

This will set the solution to maintenance mode. For more information, see [Managing maintenance mode](administrator-guide.md#maintenance-mode).

## End all Active and Frozen leases
<a name="end-active-leases"></a>

In this step, you terminate all active and frozen leases to stop incurring costs for these accounts.

1. Log in to the web UI as an **Administrator**.

1. From the left pane, choose **Leases**.

1. On the Leases page, under Filter options, for status, filter for all *Active* and *Frozen* leases if not already selected by default.

1. Under the **Leases** section, select all the leases matching the filter criteria.

1. From the **Actions** dropdown, choose **Terminate**.

 **Note**: If there are multiple pages of leases, repeat this for all leases that match the *Active* and *Frozen* filters.

This will terminate the leases and submit the accounts for cleanup. Depending on the number of accounts, cleanup may take a few minutes.

## Eject accounts
<a name="eject-accounts"></a>

In this step, you manually eject accounts that have been cleaned up, and are available for reuse.

1. Log in to the web UI as an **Administrator**.

1. From the left pane, choose **Administration** > **Accounts**. The Accounts page displays all the accounts currently in the account pool.

1. Search for, and select all the accounts you want to eject from the account pool. You can eject any accounts from the account pool, except those in the **Clean up** state.

**Note**
Accounts in Quarantine might still contain resources that incur cost. Resolve any quarantined accounts before uninstalling the solution, either by retrying cleanup or ejecting them directly. For more information, refer to the [Investigating quarantined accounts](troubleshooting.md#investigating-accounts) section.

1. From the **Actions** dropdown, choose **Eject account**.

1. On the confirmation dialog, choose **Submit** to confirm.

 **Note**: If there are multiple pages for accounts, repeat this for all accounts you want to eject.

This will eject the accounts from the Account pool.

## Move accounts out of the Organizational Unit
<a name="move-accounts"></a>

In this step, you move accounts out of the Organization Unit so that the StackSet can delete all the stack instances from the sandbox account.

1. Log in to the Organization Management account, and navigate to [AWS Organizations](https://console.aws.amazon.com/organizations/).

1. From the left pane, choose **AWS Accounts**.

1. From the organization structure tree, select the Innovation Sandbox OU, named *<NAMESPACE>\_InnovationSandboxAccountPool*. For example, *myisb\_InnovationSandboxAccountPool*.

1. Confirm that there are no other accounts in the OUs other than the *Exit* or *Entry* OUs. If there are accounts in other Account Pool OUs, eject these accounts using steps described in the [Eject accounts](#eject-accounts) section.

1. Move the accounts in *Exit* to outside the Innovation Sandbox OU, or the root OU.

This ensures that there are no accounts in the OU before you uninstall the stacks for the solution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
