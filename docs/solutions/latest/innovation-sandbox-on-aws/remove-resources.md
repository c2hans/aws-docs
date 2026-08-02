---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/remove-resources.html
---

# End leases and eject accounts
<a name="remove-resources"></a>

## Enable maintenance mode
<a name="enable-maintenance-mode"></a>

Maintenance mode allows Admins to perform sensitive maintenance work like setup, troubleshooting, upgrading, or teardown of the solution.

When you enable maintenance mode, it will stop users and managers from making API requests to the solution, and any new API requests will not interfere with maintenance tasks being performed by the Admin.

To enable maintenance mode:

1. Log in to the AWS account where the Innovation Sandbox Hub and data stacks are deployed, and select the correct home Region.

1. Navigate to [AWS AppConfig](https://console.aws.amazon.com/systems-manager/appconfig/), and from the left pane, select **Applications**.

1. On the Applications page, select **InnovationSandboxData-Config-Application-XXXXXXX**. The Application details display.

1. Under **Configuration Profiles and Feature Flags**, select **InnovationSandboxData-Config-GlobalConfigHostedConfiguration-XXXXX** configuration profile, and choose **Create**.

1. Update the **maintenanceMode** value to `true`.

```
...
# Put the solution into maintenance mode
maintenanceMode: true
...
```

1. Select **Create hosted configuration version**.

1. Select **Start Deployment**, and choose the latest hosted configuration version you just created.

1. Choose **Start Deployment**.

This will set the account to Maintenance mode.

## End all Active and Frozen leases
<a name="end-active-leases"></a>

In this step, you will terminate all active and frozen leases to stop incurring costs for these accounts.

1. Log in to the web UI as an **Administrator**.

1. From the left pane, select **Leases**.

1. On the Leases page, under Filter options, for status, filter for all *Active* and *Frozen* leases if not already selected by default.

1. Under the **Leases** section, select all the leases matching the filter criteria.

1. From the **Actions** dropdown, select **Terminate**.

 **Note**: If there are multiple pages of leases, repeat this for all leases that match the *Active* and *Frozen* filters.

This will terminate the leases and submit the accounts for clean-up. Depending on the number of accounts, clean-up may take a few minutes.

## Eject accounts
<a name="eject-accounts"></a>

In this step, you will manually eject accounts that have been cleaned up, and are available for reuse.

1. Log in to the web UI as an **Administrator**.

1. From the left pane, select **Administration** > **Accounts**. The Accounts page displays all the accounts currently in the account pool.

1. Search for, and select all the accounts you want to eject from the account pool. You can eject any accounts from the account pool, except those in the **Clean up** state.

**Note**
If a clean-up failed on an account, that account will be moved to a Quarantine state. After you troubleshoot these accounts, you can manually clean-up accounts in Quarantine. Accounts in Quarantine will continue to incur cost, so make sure you manually troubleshoot these accounts before attempting to clean-up these accounts.

1. From the **Actions** dropdown, select **Eject account**.

1. On the confirmation dialog, select **Submit** to confirm.

 **Note**: If there are multiple pages for accounts, repeat this for all accounts you want to eject.

This will eject the accounts from the Account pool.

## Move accounts out of the Organizational Unit
<a name="move-accounts"></a>

In this step, you will move accounts out of the Organization Unit so that the StackSet can delete all the stack instances from the sandbox account.

1. Log in to the Organization Management account, and navigate to [AWS Organizations](https://console.aws.amazon.com/organizations/).

1. From the left pane, select **AWS Accounts**.

1. From the organization structure tree, select the Innovation Sandbox OU, named *<NAMESPACE>\_InnovationSandboxAccountPool*. For example, *myisb\_InnovationSandboxAccountPool*.

1. Confirm that there are no other accounts in the OUs other than the *Exit* or *Entry* OUs. If there are accounts in other Account Pool OUs, eject these accounts using steps described in the [Eject accounts](#eject-accounts) section.

1. Move the accounts in *Exit* to outside the Innovation Sandbox OU, or the root OU.

This will ensure that there are no accounts in the OU before you uninstall the stacks for the solution.
