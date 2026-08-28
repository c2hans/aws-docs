---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/administrator-guide.html
---

# Administrator Guide
<a name="administrator-guide"></a>

This section describes the various actions an Administrator can perform using the web UI.

## Adding new accounts to the account pool
<a name="new-accounts"></a>

As an Administrator, you can add new AWS accounts to your account pool using the web UI. Adding new accounts will increase the number of accounts you can lease to your end users, allowing them to work with temporary AWS accounts. After you add new accounts to the account pool, you can lease these accounts to users.

**Important**
You will need to create the AWS accounts and add them to your organization before adding them to the account pool. The Innovation Sandbox solution cannot create new accounts for you.

1. From the [AWS Organizations](https://console.aws.amazon.com/organizations/) console in your org management account, move accounts that you want to onboard into the **Entry** OU located under the **<NAMESPACE>\_InnovationSandboxAccountPool** OU. This will stage them to be registered with the solution.

1. In the solution web UI go to the **Administration** dropdown and choose **Accounts**. This will display the **Accounts** page.

1. From the top right, choose **Add accounts**. The list of available accounts will only include those located in the **Entry** OU.

1. From the list of available accounts, choose the accounts you want to add to the Account pool, and choose **Register**.

1. Review your selections and choose **Submit** to add the selected accounts to your Account pool.

### Resolving Account Cleanup Failures
<a name="resolving-account-cleanup-failures"></a>

During the account registration process the sandbox accounts go through an initial cleanup process. In some cases the account may fail cleanup and be placed into the **Quarantine** status. In most cases the cleanup failure is due to resources created by services that integrate with AWS Organizations that you may have enabled such as AWS CloudTrail, AWS Security Hub, or Amazon GuardDuty.

In the event that the cleanup process fails in your deployment when registering accounts you will need to modify the AWS Nuke configuration file to filter out the protected resources.

First we must discover the resources that should be ignored for your environment:

1. In the **Hub account** navigate to the [AWS Step Functions console](https://console.aws.amazon.com/states) and choose the account cleaner state machine starting with **AccountCleanerStepFunctionStateMachine**.

1. Choose one of the recent executions with a **Failed** status.

1. From the **Details** tab, copy the executionId provided at the top of the page (It will be in a format like **xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\_xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx**).

1. Navigate to the [Amazon CloudWatch Logs Insights console](https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights).

1. Choose **Saved and sample queries** from the menu on the right.

1. Expand the group name **ISB-<namespace>** and choose the **AccountCleanupLogs** query.

1. In the query editor replace the **PasteStateMachineExecutionIdHere** text with the executionId you copied previously.

1. Ensure that the time range you selected includes the time of the cleanup failure.

1. Choose **Run query**, this will display any resources that failed to be cleaned up.

1. Make a note of any of the resource types in the **resourceType** column that should be filtered out.

Now we must update the AWS Nuke configuration file to ignore these resources:

1. In the **Hub account** navigate to the [applications page in the AWS AppConfig console](https://console.aws.amazon.com/systems-manager/appconfig/applications).

1. Choose the application starting with **InnovationSandboxData-Config-Application**.

1. Choose the configuration profile starting with **InnovationSandboxData-Config-NukeConfigHostedConfiguration**. This is the AWS Nuke config file for the solution.

1. To update the configuration file choose **Create version**.

1. Use the resource types noted in the previous steps to modify the filter to ignore them. Refer to the [AWS Nuke Config documentation](https://aws-nuke.ekristen.dev/config/) for details on how to update filters.

1. Once you have made your modifications, choose **Create hosted configuration version**.

1. Then choose **Start deployment** to update the nuke configuration for the solution.

Assuming you have appropriately modified the filters for your environment you can now retry the cleanup process:

1. Return to the solution web UI and navigate to the **Accounts** page.

1. Select any accounts that are in the **Quarantine** status.

1. Under the **Actions** menu, choose **Retry cleanup**.

This will reinvoke the cleanup process on the account with the new AWS Nuke configurations.

**Note**
If the cleanup process continues to fail, you may have missed a resource that needs to be filtered out. Repeat the previous steps to add the appropriate filters to your AWS Nuke config file for other resources failing the cleanup that should be filtered out.

### Account states in Innovation Sandbox
<a name="understand-states"></a>

This table explains the various states the account can be in at any given time. Most state transitions happen automatically. The exception is the Quarantine state: an Administrator can manually move an account in the Available, Active, or Frozen state into Quarantine using the Quarantine account action. For more information, refer to [Manually quarantining accounts](#manually-quarantining-accounts).

| State | Description |
| --- | --- |
| Available | The account is in the pool and ready to be used as part of a lease. |
| Active | The account is being used for a lease. |
| Frozen | The account is being used for a lease but the user no longer has access to the account. Administrators and Managers can still access the account for evaluation and review purposes.<br /> **Note:** This is an optional state. You will need to configure the account to freeze during the lease template creation. See [Creating and managing lease templates](manager-guide.md#creating-lease-templates) for more information. |
| CleanUp | The account is going through the cleanup process. |
| Quarantine | An account enters Quarantine through one of three paths: the automated cleanup process fails, the drift monitor detects drift on the account, or an Administrator manually quarantines it using the **Quarantine account** action. If the automated cleanup process fails, an Admin must manually resolve any resources that failed to delete before the account returns to the cleanup state for a final cleanup process. To recover, use **Retry cleanup**, or eject the account and re-onboard it into the account pool. |

### Account lifecycle in Innovation Sandbox
<a name="account-lifecycle"></a>

For more information, refer to the [Account lifecycle](account-lifecycle-in-isb.md) section.

## Managing existing accounts
<a name="manage-accounts"></a>

As an Administrator, you can manage any existing accounts. This allows you to manually perform account lifecycle actions such as removing accounts from the pool, and retrying the cleanup process.

![Account management options](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/account-admin-actions.png)

**Account management options**
To manage accounts:

1. From the **Administration** dropdown, navigate to the **Accounts** page.

1. Select the accounts you want to manage to enable the **Actions** dropdown. Using the **Actions** dropdown, you can perform these actions for the selected accounts.

| Action | Description |
| --- | --- |
| Eject account | Removes the account from the pool of available accounts.<br /> **Note**: Administrators can also eject in-use accounts. For example, they might want to preserve work beyond the lease or move the account away from the management provided by Innovation Sandbox. |
| Retry cleanup | Restarts the cleanup process for that account. By default, lapsed or inactive accounts will be cleaned on a periodic basis. If an account cannot be cleaned, Administrators can manually resolve any issues, and use this option to restart the cleanup process. For example, for accounts in a Quarantine state. |
| Quarantine account | Immediately isolates the selected accounts by terminating any active leases, revoking leaseholder access, and moving the accounts to the Quarantine OU. This action is only enabled when all of the selected accounts are in the Available, Active, or Frozen state. For more information, refer to [Manually quarantining accounts](#manually-quarantining-accounts). |

### Viewing cleanup details
<a name="viewing-cleanup-details"></a>

The Accounts list page displays the current cleanup status inline in the **Status** column for any account undergoing cleanup (for example, "Clean Up (Nuke Phase 1)" or "Clean Up (Validating)"). Accounts not in active cleanup display "Clean Up" without a sub-status.

To view detailed cleanup information for a specific account, choose the account ID link in the Accounts list. The account details page shows:
+  **Active cleanup progress**: If a cleanup is currently running, you see the current step and a live status indicator that refreshes automatically.
+  **Start cleanup**: Administrators can initiate cleanup directly from the account details page using the **Start cleanup** button. The button is disabled while a cleanup is already running.
+  **Recent cleanups**: A table of the most recent cleanup reports for the account, with status, reason, start time, and duration. Choose a row to view the full detail.
+  **Step timeline**: An expandable timeline showing each cleanup step’s status, duration, and any error details. Nuke phase steps include a link to the CodeBuild build logs.
+  **Resource summary**: A before-and-after resource type table showing what was cleaned. If validation failed or proceeded with a warning, a **Remaining resources** table shows the specific resources that were not cleaned, with their ARN, type, and region.

### Skipping account cooldown
<a name="skip-cooldown"></a>

When an account is in a post-cleanup cooldown (status shows "Clean Up (Cooling Down)"), Administrators and Managers can skip the remaining cooldown to return the account to the Available pool immediately.

To skip a cooldown:

1. From the **Administration** dropdown, navigate to the **Accounts** page.

1. Choose the account ID link for the account in cooldown.

1. In the cleanup overview section, choose **Skip cooldown**.

1. Review the warning in the confirmation dialog. Skipping the cooldown might result in costs from the previous lease being attributed to the next user.

1. Choose **Skip cooldown** to confirm.

The account returns to the Available pool within a few seconds.

### Manually quarantining accounts
<a name="manually-quarantining-accounts"></a>

As an Administrator, you can manually quarantine an account to temporarily remove it from circulation while preserving the ability to restore it later. Common reasons to manually quarantine an account include exhausted service quotas, suspected compromise or unusual activity on the account, or a policy violation that needs review before the account is returned to use.

Quarantining an account immediately:
+ Terminates any active lease on the account and revokes the leaseholder’s access.
+ Moves the account into the Quarantine OU.
+ Removes the account from the available account pool.

To manually quarantine an account:

1. From the **Administration** dropdown, navigate to the **Accounts** page.

1. Select one or more accounts that are in the **Available**, **Active**, or **Frozen** state.

1. Under **Actions**, choose **Quarantine account**.

1. Review the warning in the confirmation dialog and choose **Submit**.

**Important**
Quarantining an account cannot be reversed. Any leaseholder on the account loses access immediately. To recover a quarantined account, use **Retry cleanup**, or eject the account and re-onboard it into the account pool.

**Note**
Every quarantine action, regardless of cause, is recorded for auditing purposes. For more information, refer to [Monitoring the solution](monitoring-the-solution.md).

## Registering and managing blueprints
<a name="registering-managing-blueprints"></a>

As an Administrator, you can register CloudFormation StackSets as blueprints to provide pre-configured infrastructure to sandbox accounts. Blueprints enable users to receive accounts with ready-to-use resources, reducing manual setup.

![Blueprints list page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/blueprints-list-page.png)

**Blueprints page**
Blueprints are optional. You must create self-managed CloudFormation StackSets outside of Innovation Sandbox before registering them as blueprints.

### Creating self-managed StackSets
<a name="create-stacksets"></a>

Before registering blueprints, create [self-managed CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-getting-started-create.html) in your hub account (the AWS account where Innovation Sandbox is deployed).

 **Prerequisites:**
+ A CloudFormation template that defines the infrastructure to deploy to sandbox accounts
+ IAM roles for cross-account deployment — the solution creates `InnovationSandbox-{NAMESPACE}-IntermediateRole` (administration role) and `InnovationSandbox-{NAMESPACE}-SandboxAccountRole` (execution role)
+ Knowledge of your infrastructure requirements and target regions

 **Example: Create a StackSet using AWS CLI**

```
aws cloudformation create-stack-set \
  --stack-set-name my-blueprint-stackset \
  --template-url https://s3.us-east-1.amazonaws.com/my-bucket/my-template.yaml \
  --administration-role-arn arn:aws:iam::{ACCOUNT-ID}:role/InnovationSandbox-{NAMESPACE}-IntermediateRole \
  --execution-role-name InnovationSandbox-{NAMESPACE}-SandboxAccountRole \
  --managed-execution Active=true \
  --capabilities CAPABILITY_IAM \
  --description "My blueprint infrastructure"
```

Replace `{ACCOUNT-ID}` with your hub account ID and `{NAMESPACE}` with your solution namespace.

**Tip**
The `--managed-execution Active=true` flag enables [managed execution](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ManagedExecution.html) on your StackSet. This allows CloudFormation to run non-conflicting operations concurrently and automatically queue conflicting operations, preventing deployment bottlenecks when multiple leases are approved simultaneously.

**Note**
Do not add deployment targets or specify accounts when creating the StackSet. Innovation Sandbox manages StackSet instance creation automatically when leases are approved.

### Blueprint prerequisites
<a name="blueprint-prerequisites"></a>

Before registering blueprints, ensure you meet these requirements:

 **StackSet Requirements:** \* StackSet must use SELF\_MANAGED permission model \* StackSet must be in ACTIVE status \* StackSet template must be valid and tested

 **Template Validation:** \* Test StackSet deployment to a test account before registration \* Verify template completes within your desired timeframe \* Ensure template is idempotent (can be deployed multiple times safely) \* Validate template works across all target regions

 **To validate your StackSet before registration:**

1. Sign in to the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Navigate to **StackSets** and locate your StackSet.

1. Verify the StackSet status shows **ACTIVE**.

1. Check that the permission model shows **SELF\_MANAGED**.

1. Verify the IAM roles match the recommended ISB role names:
   + Administration Role: `InnovationSandbox-{NAMESPACE}-IntermediateRole`
   + Execution Role: `InnovationSandbox-{NAMESPACE}-SandboxAccountRole`

1. Review recent operations to ensure successful deployments.

1. Test deployment to a sandbox account manually before registering as blueprint.

**Note**
For detailed StackSet creation steps, refer to [Creating self-managed StackSets](#create-stacksets).

**Important**
Test your StackSet deployment before registering it as a blueprint. Untested StackSets may fail during lease provisioning and prevent users from accessing their accounts. Avoid hardcoding credentials or sensitive data in templates — use AWS Secrets Manager or Parameter Store instead. For general template security guidance, refer to [AWS CloudFormation security best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/security-best-practices.html).

### Registering a new blueprint
<a name="registering-blueprint"></a>

To register a blueprint using the registration wizard:

1. From the **Administration** dropdown, choose **Blueprints**.

1. Choose **Register blueprint**.

1. On the **Blueprint Configuration** page, complete the required fields:

   1. For **Name**, enter a descriptive name (1-50 characters).

   1.  *(Optional)* Add tags to provide metadata such as estimated cost, description, or support contact.

   1. Choose **Next**.
![Blueprint Configuration page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/blueprint-registration-wizard-step1.png)

1. On the **StackSet Selection** page:

   1. Select the StackSet you want to register as a blueprint from the list.

   1. Choose **Next**.
![StackSet Selection page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/blueprint-registration-wizard-step2.png)

1. On the **Deployment Configuration** page, configure deployment settings:

   1. For **Regions**, select the AWS Regions where the blueprint will be deployed. You can select multiple regions.
**Note**
The available regions are determined by the **ISB Managed Regions** parameter configured during AccountPool stack deployment. To add or remove regions, update the AccountPool stack parameter. For more information, see [Deploy the AccountPool stack](step1-deploy-accountpool-stack.md). You can view the currently configured managed regions on the **Read-only** tab of the **Settings** page.

   1. For **Deployment Timeout**, enter the maximum time (in minutes) to wait for deployment completion (default: 30 minutes).

   1. For **Deployment Strategy**, choose a strategy:
[See the AWS documentation website for more details](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/administrator-guide.html)

   1. If you selected **Custom**, configure these parameters:
      +  **Region concurrency type**: Sequential (one region at a time) or Parallel (all regions simultaneously)
      +  **Max concurrent percentage**: Percentage of regions to deploy concurrently
      +  **Failure tolerance percentage**: Percentage of regions that can fail before the overall deployment is marked as failed. Set to 0% to stop on the first failure.
      +  **Concurrency mode**: Strict (reduces concurrency on failures) or Soft (maintains maximum concurrency)

         **What success and failure mean in Innovation Sandbox**

        When a lease is approved and the template has a blueprint, Innovation Sandbox deploys the blueprint’s StackSet instances to the sandbox account. The deployment outcome determines what happens next:
        +  **Deployment succeeds**: The user is granted access to the sandbox account with the pre-deployed resources. The lease becomes **Active**.
        +  **Deployment fails**: The lease is terminated, the account is cleaned up and returned to the available pool, and the user does not receive access. If the lease required manual approval, it is reset to **PendingApproval** so the manager can investigate and re-approve. Administrators and managers are notified by email.

        The failure tolerance percentage controls when CloudFormation considers the overall deployment as failed. If the number of region failures stays within the tolerance, CloudFormation marks the deployment as succeeded, even though some regions have no resources. The user receives the account, but resources may be missing in those failed regions. You can review per-region results in the deployment history on the blueprint details page.

         **Example: Blueprint deploys to 3 regions (us-east-1, us-west-2, eu-west-1) with 100% concurrency and 30% failure tolerance**
        +  **1 of 3 regions fails** (33% failure rate, within 30% tolerance rounded up): CloudFormation marks the deployment as **succeeded**. The user receives the sandbox account and the lease becomes Active. However, the failed region has no blueprint resources. The deployment history on the blueprint details page shows the per-region results.
        +  **2 of 3 regions fail** (66% failure rate, exceeds 30% tolerance): CloudFormation marks the deployment as **failed**. The lease is terminated, the account is cleaned up, and the user does not receive access. Administrators and managers are notified by email to investigate the blueprint configuration.
**Tip**
For new blueprints, use the **Default** strategy (0% failure tolerance) until you have validated that the StackSet deploys reliably. Switch to **Custom** with higher failure tolerance only when you understand the trade-off: users may receive accounts with missing resources in failed regions.

   1. Choose **Next**.
![Deployment Configuration page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/blueprint-registration-wizard-step3.png)

      1. On the **Review and Submit** page, review your configuration and choose **Register blueprint**.

After registration completes, a success message confirms the blueprint is available. Managers can now associate it with lease templates.

 **To verify successful registration:**

1. On the **Blueprints** page, confirm the new blueprint appears in the list.

1. Select the blueprint name to view details.

1. Verify all configuration matches your input:
   + Blueprint name is correct
   + StackSet ID matches the selected StackSet
   + Deployment configuration shows your settings
   + Tags are present (if configured)

1. Check the health metrics section shows "0 / 0" deployments (no deployments yet).

1. Verify the StackSet details section shows correct IAM roles and regions.

**Note**
Newly registered blueprints have no deployment history until associated with a lease template and used in a lease. For troubleshooting deployment issues, refer to [Blueprint deployment issues](troubleshooting.md#blueprint-deployment-issues) in the Troubleshooting chapter.

### Monitoring blueprint health
<a name="monitoring-blueprint-health"></a>

To view blueprint health and deployment history:

1. From the **Administration** dropdown, choose **Blueprints**.

1. Select a blueprint name to view details.

![Blueprint details page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/blueprint-details-page.png)

**Blueprint details page**
The blueprint details page shows:
+  **Basic details**: Name, blueprint ID, created by, created date, last updated date
+  **Tags**: Key-value pairs (if configured)
+  **Deployment configuration**: Timeout, region concurrency, concurrent deployments, failure tolerance, concurrency mode
+  **Health metrics**: Total deployments, successful deployments (shown as "X / Y"), last deployment time
+  **Recent deployments**: Table of recent deployments showing Lease ID, Account ID, Status (RUNNING, SUCCEEDED, FAILED, or QUEUED), Started time, and Duration. Select a deployment row to expand the Deployment details panel showing full details including Operation ID, error type, and error details for failed deployments.
+  **StackSet details**: StackSet name, StackSet ID, IAM roles, regions, per-StackSet health metrics

Use this information to assess blueprint reliability and troubleshoot deployment issues.

### Updating blueprint metadata
<a name="updating-blueprint"></a>

To update a blueprint:

1. On the **Blueprints** page, select the blueprint name to view details.

1. Choose **Edit** from the section you want to modify:
   +  **Basic details**: Update name or tags
   +  **Deployment configuration**: Update timeout, deployment strategy, or concurrency settings

1. Make your changes and choose **Save**.
![Edit deployment configuration page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/blueprint-edit-deployment-config.png)

**Note**
Updating blueprint metadata does not affect existing leases. New leases will use the updated configuration.

### Unregistering a blueprint
<a name="deleting-blueprint"></a>

To unregister a blueprint:

1. On the **Blueprints** page, select one or more blueprints you want to unregister.

1. Under **Actions**, choose **Unregister**.
![Unregister action in Actions dropdown](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/blueprint-unregister-action.png)

1. Review the blueprints to be unregistered and choose **Submit**.

**Important**
You cannot unregister blueprints that are associated with active lease templates. Edit the blueprint on all templates and turn off **Enable Blueprint Selection** before unregistering. Unregistering a blueprint removes it from Innovation Sandbox but does not delete the underlying StackSet.

## Viewing or modifying Innovation Sandbox settings
<a name="manage-settings"></a>

You can view and modify your Innovation Sandbox settings on the **Settings** page. From the left navigation pane, choose **Settings**. Administrators can edit every section; Managers see a read-only view of the same sections; sandbox users cannot access the **Settings** page.

![Innovation Sandbox Settings page showing Leases & Cost](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/settings-page-overview.png)

**Innovation Sandbox Settings page**
As an Administrator, you can modify all global settings directly on the **Settings** page. Managers can open the **Settings** page to view the current values, but cannot change them.

**Note**
The account cleanup configuration—the AWS Nuke configuration and the cleanup validator exclusion configuration—remains in AWS AppConfig. The **Settings** page does not manage this configuration. For more information, see [Resolving Account Cleanup Failures](#resolving-account-cleanup-failures) and [Keeping exclusion configurations in sync](troubleshooting.md#validation-exclusion-config-sync).

**Important**
If you upgraded to v1.3.0 or later from an earlier version, your account still contains the **GlobalConfig** and **ReportingConfig** configuration profiles. The solution previously used these profiles in AWS AppConfig, but no longer reads them. Editing these orphaned profiles has no effect. Make all configuration changes on the **Settings** page in the web UI.

### Modify configuration
<a name="modify-configuration"></a>

Settings are organized into four tabs: **Leases & Cost**, **Cleanup**, **General**, and **Read-only**. Each configuration section has its own **Save** button, so saving one section does not affect any other section.

To modify a setting:

1. In the solution web UI, from the left navigation pane, choose **Settings**.

1. Choose the tab that contains the section you want to change. Use **Leases & Cost** for Lease Policies and Cost Reporting, and **Cleanup** for the account cleanup loop. Use **General** for Maintenance Mode, Terms of Service, and Notification.

1. Update the values in the section you want to change.

1. Choose **Save**. A confirmation message, "Settings saved.", displays, and the new values take effect immediately.

**Note**
If another Administrator saves the same section after you loaded the page, your **Save** fails with a **Conflict** error. The error reads: "These settings were modified by another administrator. Reload to see the latest values." Choose **Reload** to load the latest values, reapply your changes, and choose **Save** again. Reloading discards your unsaved edits for that section.

### Completing initial setup
<a name="completing-initial-setup"></a>

Every configuration section starts with built-in default values. Until you save each section for the first time, the **Settings** item in the left navigation pane displays a badge. The badge shows how many sections have not yet been saved. Each unsaved section on the **Settings** page displays a **Using default values** alert. (The **Maintenance Mode** section shows a maintenance-specific warning instead. For more information, see [Managing maintenance mode](#maintenance-mode).) If every section is still unsaved, the **Settings** page also shows an **Initial setup required** banner. Innovation Sandbox is fully operational with the default values in the meantime.

Review each section and choose **Save** to apply it to your deployment. You can save a section with its default values unchanged; doing so removes it from the count of sections needing attention.

### Managing maintenance mode
<a name="maintenance-mode"></a>

Maintenance mode temporarily restricts the solution to Administrators. When maintenance mode is on, Managers and sandbox users lose access to the Innovation Sandbox web application. A maintenance banner displays on every page of the web UI. Their existing sandbox accounts are unaffected, and Administrators retain full access. Use maintenance mode when performing sensitive maintenance work, such as initial setup, troubleshooting, or upgrading the solution.

![Settings page General tab with Maintenance Mode toggle](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/settings-general-maintenance.png)

**Maintenance Mode section on the General tab**
To turn maintenance mode on or off:

1. In the solution web UI, from the left navigation pane, choose **Settings**.

1. Choose the **General** tab.

1. Under **Maintenance Mode**, turn the **Maintenance mode** toggle on or off.

1. Choose **Save**.

1. On the confirmation dialog, choose **Turn on maintenance mode** or **Turn off maintenance mode**.

**Important**
New deployments of Innovation Sandbox on AWS start with maintenance mode turned **ON**. After you finish reviewing the **Settings** page, turn maintenance mode off so Managers and users can access the solution.

### Global configuration settings
<a name="global-settings"></a>

The following tables list the global configuration settings you can view or modify on the **Settings** page, grouped by section. For the cost reporting settings, see [Cost report configuration settings](#cost-report-settings).

 **Lease Policies** (**Leases & Cost** tab)

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| Require max budget | Boolean | On | Require lease templates to define a maximum budget. |
| Max budget | Number (USD) | 50 | Maximum budget, in USD, that a lease template can be created with. Range: 0 to 1,000,000,000. |
| Require max duration | Boolean | On | Require lease templates to define a maximum duration. |
| Max lease duration | Number (hours) | 168 | Maximum duration, in hours, that a lease template can be created with. Range: 0 to 87,600. |
| Max leases per user | Number | 3 | Maximum number of concurrent active leases (including pending requests) a single user can have. |
| Lease record TTL | Number (days) | 30 | Number of days an expired lease record is retained before it is permanently deleted. Deletion might take up to 48 hours after the TTL expires. |
| Allow user lease termination | Boolean | On | When enabled, users can terminate their own active leases. When disabled, only Admins and Managers can. |
| Rate limit window | Number (hours) | 168 | Rolling window, in hours, used to rate-limit lease requests. Must not exceed the **Lease record TTL** converted to hours (days × 24). |
| Max requests per window | Number | 10 | Maximum number of lease requests a user can make within the rate limit window before further requests are rejected. |
| Enable lease sharing | Boolean | Off | When enabled, lease owners can manage assignments on leases that permit sharing. Admins and Managers always retain access. |
| Enable principal search | Boolean | On | When enabled, the user typeahead search used to find and assign principals is available. When disabled, it is unavailable to all roles. |

 **Cleanup** (**Cleanup** tab)

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| Failed attempts before quarantine | Number | 3 | Total failed AWS Nuke attempts before an account fails cleanup and is sent to quarantine. |
| Wait before retry (seconds) | Number | 5 | Delay, in seconds, between failed AWS Nuke attempts. |
| Successful attempts to finish | Number | 2 | Total successful AWS Nuke attempts before an account finishes cleanup and is returned to available. |
| Wait before rerun (seconds) | Number | 30 | Delay, in seconds, between successful AWS Nuke attempts. |
| Account cooldown (hours) | Number | 24 | Hours an account waits after cleanup before it can be leased again. Range: 0 to 8640. Set to 0 for no cooldown. The cooldown also serves as the Resource Explorer staleness buffer for post-cleanup validation. |
| Cleanup report retention (days) | Number | 730 | Days a cleanup report is retained before it is deleted. Range: 14 to 3650. |
| On validation failure | Silent, Warn, or Quarantine | Silent | What happens when post-cleanup validation finds remaining resources. **Silent** (default): validation runs and captures data but takes no action. **Warn**: logs a warning and surfaces remaining resources in the UI, but returns the account to available. **Quarantine**: moves the account to quarantine for manual review. |

 **General** (**General** tab)

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| Maintenance mode | Boolean | On | Restricts web application access to Admins. For more information, see [Managing maintenance mode](#maintenance-mode). |
| Terms of service content | String | Built-in default terms of service text | Terms of service presented to users when requesting a lease. You can customize this with your own words on how users should responsibly use their sandbox account and what they are responsible for. Maximum 10,000 characters. |
| Email from address | String | Empty (notifications disabled) | Sender address used for all email notifications. Leave empty to disable email notifications. The address (or its parent domain) must be a verified identity in Amazon SES. |

### Cost report configuration settings
<a name="cost-report-settings"></a>

The following table includes the **Cost Reporting** settings you can view or modify on the **Leases & Cost** tab of the **Settings** page. Use these settings for cost attribution and reporting.

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| Cost report groups | Array of strings | Empty | List of valid cost report group names that can be assigned to lease templates. Maximum of 100 cost report groups, with each group name limited to 50 characters. |
| Require cost report group | Boolean | Off | Determines whether a cost report group is required on leases and lease templates. When enabled, all new lease template creation and updates require a valid cost report group to be assigned. This is not enforced for existing leases or lease templates; they need to be manually updated. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
