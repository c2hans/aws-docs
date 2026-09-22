---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/manager-guide.html
---

# Manager Guide
<a name="manager-guide"></a>

This section describes the various actions a Manager can perform using the web UI.

## Creating lease templates
<a name="creating-lease-templates"></a>

Managers (and Administrators) can create lease templates that define specific configurations users can choose when requesting a lease. A lease template includes settings for blueprints, budget limits, duration, and cost reporting. All of your available lease templates are displayed on the **Lease Templates** page.

To create a lease template, navigate to **Lease Templates** in the web UI and choose **Add new lease template**. This opens a wizard to configure your template.

On the **Basic details** page, configure the template’s name, description, visibility, and approval requirements.

![Basic Details page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step1-basic-details.png)

1. For **Name**, enter a descriptive name for your lease template so that you can keep track of it.

1.  *(Optional)* For **Description**, specify the intended purpose of the account type.

1. For **Requires Approval**, choose whether manager approval is required:
   +  **Approval required** (default): Managers must manually approve each lease request. Use this for accounts with high budgets or for experienced users.
   +  **No approval required**: Accounts are automatically assigned when requested. Use this for accounts with small budgets, testing, and small workloads.

1. For **Visibility**, choose between **Public** or **Private**:
   +  **Public**: The template appears in the general template listing and users can request leases from it through self-service.
   +  **Private**: The template is only visible to administrators and managers for direct lease assignment purposes. Users cannot see or request leases from private templates.

1.  *(Optional)* For **Allow owner to share lease**, choose whether users who own a lease created from this template can share it with additional users and groups. This setting appears only when lease sharing is enabled globally. When turned off, only administrators and managers can manage sharing on leases created from this template. For more information, refer to [Sharing a lease with additional users and groups](#lease-sharing).

1. Choose **Next**.

On the **Blueprint** page, you can associate a blueprint with this lease template to pre-deploy infrastructure when leases are created.

![Blueprint page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step2-blueprint.png)

1. Blueprint selection is enabled by default. To skip blueprint selection, turn off **Enable Blueprint Selection**.
![Blueprint page with selection disabled](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step2-blueprint-disabled.png)

1. Choose a blueprint from the available options.

1. Choose **Next** to continue.

**Note**
When you approve a lease, the blueprint deploys to the sandbox account. If deployment fails, the lease terminates automatically and the account returns to the pool.

On the **Budget** page, configure spending limits and budget thresholds. See [Budget thresholds](#budget-thresholds) for detailed guidance.

![Budget Settings page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step3-budget.png)

1. Choose whether to set a maximum budget:
   +  **Budget limit enabled**: Enter a value in **Maximum Spend** (measured in $USD).
   +  **Budget limit disabled**: No spending limit is enforced (not recommended for production use).

1.  *(Optional)* Add additional thresholds to send alerts or freeze the account at different spending levels:

   1. Choose **Add Threshold**.

   1. Enter a threshold value in $USD.

   1. Select an action: **Send Alert** (email notification) or **Freeze Lease** (prevents new resource creation).

1. Choose **Next**.

On the **Lease Duration** page, configure time limits and duration thresholds. See [Duration thresholds](#duration-thresholds) for detailed guidance.

![Lease Duration page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step4-duration.png)

1. Choose whether to set a maximum duration:
   +  **Duration limit enabled**: Enter a value in **Maximum Duration (in hours)**. This determines how long the lease remains active.
   +  **Duration limit disabled**: Leases do not automatically expire (not recommended for production use).

1.  *(Optional)* Add thresholds to send alerts or freeze the account as time remaining decreases:

   1. Choose **Add a threshold**.

   1. Enter a threshold value in hours.

   1. Select an action: **Send Alert** (email notification) or **Freeze Lease** (prevents new resource creation).

1. Choose **Next**.

On the **Cost Report Group** page, optionally assign a cost report group to the lease template for cost attribution and reporting purposes.

![Cost Report Group page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step5-cost-report.png)

1. Choose whether to set a cost report group:
   +  **Cost reporting group enabled**: You must select a cost reporting group.
   +  **Cost reporting group disabled**: No cost reporting group selection required.

1. If cost report groups have been configured by your administrator, select from the available options in the dropdown.

1. Choose **Next**.

**Note**
Cost report groups are used to generate custom cost reports that are delivered to an S3 bucket for detailed cost tracking and chargeback by department, project, or team. If the administrator has enabled the **Require cost report group** setting on the **Settings** page, selecting a cost report group will be mandatory.

On the **Review and Submit** page, review all your settings before creating the template.

1. Review each section of your configuration:
   + Basic Details
   + Blueprint (if configured)
   + Budget Settings
   + Lease Duration
   + Cost Report Group (if configured)

1. If you need to make changes, use the wizard navigation to return to a previous step.

1. When you’re satisfied with the configuration, choose **Create lease template** to create the lease template.

**Note**
The new lease template will be available for users to request leases (if public) or for managers to assign leases (if private).

## Updating lease templates
<a name="updating-lease-templates"></a>

After creating a lease template, you can modify its configuration from the lease template details page. Each section of the template can be edited independently.

![Lease Template Details page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-details-page.png)

To update a lease template:

1. On the **Lease Templates** page, select the template name to open the details page.

1. The details page displays all configuration sections with their current settings:
   +  **Basic Details**: Name, Description, ID, Created By, Visibility (Public/Private), Requires Approval (Yes/No)
   +  **Blueprint Details**: Blueprint ID, Blueprint Name (or "No Blueprint" if not configured)
   +  **Budget Settings**: Maximum Budget, Budget Thresholds (with alert and freeze actions)
   +  **Duration Settings**: Maximum Duration, Duration Thresholds (with alert and freeze actions)
   +  **Cost Report Settings**: Cost Report Group (or "Not assigned" if not configured)

1. Choose the **Edit** button next to the section you want to modify.

1. Make your changes on the edit page for that section.

1. Choose **Save changes** to update the lease template.

To remove a blueprint, choose **Edit** on the Blueprint Details section. Turn off **Enable Blueprint Selection** and choose **Save changes**. New leases created from this template will no longer deploy blueprint infrastructure.

**Note**
Modifying a lease template will not affect any existing leases with the old configuration. This includes blueprints - existing leases continue using their original blueprint configuration.

## Deleting lease templates
<a name="deleting-lease-templates"></a>

You can delete lease templates that are no longer needed. Deleting a template removes it from the available templates list but does not affect existing leases created from that template.

![Delete action in Actions dropdown](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-delete-action.png)

To delete a lease template:

1. On the **Lease Templates** page, select the lease template you want to delete.

1. This will enable the **Actions** dropdown. Under **Actions**, choose **Delete**.

1. Confirm your choice in the confirmation dialog and choose **Delete** to delete the template.

**Note**
Deleting a lease template will not affect any existing leases with the deleted lease template. Existing leases will continue to function normally until they expire or are terminated.

## Assigning leases to users
<a name="assigning-leases"></a>

As a Manager or Administrator, you can create leases directly on behalf of other users without requiring approval. This lease assignment feature is particularly useful for controlled distribution scenarios such as educational workshops, hackathons, or enterprise innovation initiatives where accounts need to be pre-allocated to specific users.

**Important**
The target user must exist in AWS IAM Identity Center before you can assign a lease to them. Users will receive an email notification when a lease is created on their behalf.

To assign a lease to a user:

1. In the web UI, from the left, choose **Leases**.

1. Choose **Assign lease**.

1. On the **Assign lease** page, complete the wizard forms:

   1. For **Select lease template**, select from any available lease template (both public and private templates are available for assignment).

   1. For **Select User**, enter the email address of the user you want to assign the lease to. This must match their email address in AWS IAM Identity Center.

   1. For **Terms of Service**, check the box confirming that you accept the terms of service on behalf of the assigned user.

   1.  *(Optional)* For **Review & Assign**, add any relevant notes about the lease assignment for audit purposes.

1. Review your settings and choose **Submit** to create the lease assignment.

The lease will be created immediately without requiring approval, and the target user will receive an email notification with details about their new sandbox account access.

**Note**
Managers and Administrators are exempt from the lease request rate limit when assigning leases. However, each lease you assign still counts toward the target user’s own rolling rate-limit window (by default, 10 leases per 7 days). As a result, a heavily-assigned user might be temporarily unable to self-request new leases until their window slides.

Leases you create on behalf of others will show your email address in the "Created by" field, making it easy to track which leases you’ve assigned. You can view all leases you’ve created in the **Leases** page, where they will be clearly identified with assignment details.

## Sharing a lease with additional users and groups
<a name="lease-sharing"></a>

Lease sharing lets multiple users collaborate in the same sandbox account instead of provisioning separate accounts for each team member. You can share a lease with individual users and, when group assignments are enabled, with entire AWS IAM Identity Center groups. Shared users and group members receive the same AWS account access as the lease owner through the same permission set, but they cannot terminate the lease or change its budget, duration, or other core settings.

**Important**
Lease sharing is turned off by default. An administrator must turn on the **Enable lease sharing** setting, in the **Lease Policies** section of the **Settings** page, before lease owners can share leases. While the setting is off, administrators and managers can still view and manage assignments on existing leases. Turning the setting off does not revoke access that has already been granted through sharing; to remove existing shared access, an administrator or manager must remove the principals from each lease individually, or terminate the lease. For more information, refer to [Global configuration settings](administrator-guide.md#global-settings).
Group assignments are controlled separately by the **Allow group assignments** setting and are disabled by default. When group assignments are disabled, users, administrators, and managers can add only individual users. Existing group assignments keep their access and can still be removed.

### Who can share a lease
<a name="lease-sharing-who-can-share"></a>

| Role | Sharing capability |
| --- | --- |
| Administrator, Manager | Can manage assignments on any lease in **Active** status, regardless of the template or lease setting. On frozen and terminated leases, the assignments tab is read-only. |
| Lease owner | Can manage assignments only when lease sharing is enabled globally and the lease’s **Allow owner to share lease** setting is turned on. This setting is inherited from the lease template when the lease is created, and administrators or managers can change it on an individual lease. |
| User (not the owner) | Cannot manage assignments. Users can view leases shared with them. For more information, refer to [Viewing leases shared with you](user-section.md#shared-leases). |

### Adding or removing users and groups on a lease
<a name="lease-sharing-add"></a>

![Assignments tab on the lease details page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-assignments-tab.png)

You manage sharing from the **Assignments** tab on the lease details page. Changes you stage on this tab are applied together when you save, so you can add and remove several principals in a single update.

1. From the **Leases** page, choose the lease name to open the lease details page.

1. Choose the **Assignments** tab. The tab lists the current users and groups with access, and shows each one’s **Status**, who added it, and when. The lease owner appears first, marked with an **Owner** badge.

1. To add a principal, use the search field to find a user by name or email address, then choose the user from the results. When **Allow group assignments** is set to **Allow all groups**, you can also search for and add a group by its name. You can enter an exact email address or, when group assignments are enabled, an exact group name and choose the **Add** option from the dropdown. The principal is added to the list immediately as a staged change.
**Note**
When you choose a group, a confirmation dialog opens. Choose **Add group** to confirm. All current and future members of that group receive access to the sandbox account. Group membership is managed in IAM Identity Center. If you add or remove members of the group there, their access to the sandbox account changes automatically.

1. To remove a principal, choose **Remove** on that row.

1. Review your staged changes, then choose **Save changes** to apply them. To discard all staged changes instead, choose **Cancel**.

Staged additions and removals show a **Pending add** or **Pending remove** status until you save. After you save, the solution processes the access changes in the background, and the status changes to **Granting** or **Revoking** while each change is applied, then to **Active** once access is granted. Added users receive an email notification when their access is granted. The lease owner is notified when a principal’s access is revoked. On frozen leases, principals show **Access suspended**; on ended leases, they show **Access ended**. If a change does not complete, the status changes to **Grant failed** or **Revoke failed**, and the tab displays a **Retry** option. For more information, refer to [Lease sharing issues](troubleshooting.md#lease-sharing-issues).

**Note**
Recently added Identity Center users and group members can take slightly over an hour to appear in search results (the cache refreshes hourly with a five-minute flexible window). If you can’t find someone, enter their exact email address instead. When group assignments are enabled, you can enter the exact group name.

**Note**
A lease supports up to 20 principals in total, including the lease owner (the owner plus up to 19 additional users and groups).
You can change assignments only while the lease is in the **Active** state. The **Assignments** tab is still available on frozen and terminated leases, but it is read-only: on a frozen lease it shows the access that unfreezing restores, and on a terminated lease it shows who last had access. Freezing a lease removes access for all shared users and groups; unfreezing the lease restores their access.

**Important**
When you share a lease with a group, access follows the group’s membership in IAM Identity Center. Anyone who is a member of the group, now or in the future, gains access to the sandbox account without a separate approval in Innovation Sandbox. Before sharing leases with groups, confirm that the group’s membership is governed appropriately for sandbox access.
Innovation Sandbox logs the actions taken within the solution (adding and removing principals). To audit who actually accessed a sandbox account through the IAM Identity Center access portal, including access gained through group membership, use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## Approving and rejecting leases
<a name="approve-reject-account-lease"></a>

Certain accounts require approval to be requested for a lease. When a user requests such an account, Managers or Admins need to approve the request for the user to be granted a lease.

1. From the left, choose **Approvals** to view your approval requests.

1. Select the request that you would like to approve/reject. You can select multiple requests at the same time.

1. Using the **Actions** dropdown, choose either **Approve request(s)** or **Deny request(s)** depending on your use case.

1. On the dialog box asking you to confirm, choose **Approve** or **Deny**.

## Choosing the right budget and duration configuration
<a name="choosing-thresholds"></a>

When creating lease templates, you will be prompted to set budget and duration for the lease as well as thresholds. These thresholds determine the behavior of the lease once a budget or duration is reached. In this section, we will explore in more detail how to set these thresholds and why they are important to your Innovation Sandbox environment by looking at different use cases.

Here are the different actions that can be triggered when a threshold is reached.

| Action | Description |
| --- | --- |
| Send Alert | An alert is sent to the user notifying them that the budget or duration threshold has been reached. |
| Freeze account | The account is set to the Frozen state. The account is being used for a lease but the user no longer has access to the account. Administrators and Managers can still access the account for evaluation and review purposes. |
| Terminate account | The cleanup process will start on the account. Note that this action is only available when a maximum budget or duration is set. |

To get started with this guide, follow the instructions in [Creating and managing lease templates](#creating-lease-templates) until you reach the budget section.

### Budget thresholds
<a name="budget-thresholds"></a>

The budget configuration determines the spending limit for the account once leased. The thresholds are measured in $USD and actions are triggered when the account spending reaches the threshold value.

 **Use case 1: Not setting a budget**

If you turn off **Enable Maximum Budget**, the lease will not automatically terminate, even if spending exceeds a certain limit. We recommend using this option for experienced users. It is also recommended for these leases to require approval, so you can limit their use. Bear in mind that the lease will terminate if a maximum duration is set.

You can still set thresholds on a lease with no budget. It is encouraged that you do so users can keep track of the lease usage and take action if necessary. The following figure shows an example of a lease with no budget but with thresholds set.

![Setting thresholds and no budget](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/no-budget-thresholds.png)

**Setting thresholds with no budget**
In this example, an alert is sent when the budget reaches $100, $500 and $750, and the account is frozen when the budget reaches $1000. Freezing the account prevents further user activity on the account, as any active resources will continue to incur costs. It gives managers time to investigate the spending, if needed. The user can also keep track on the spending using alerts.

 **Use case 2: Setting a budget with thresholds**

Choosing to add a budget creates an extra layer of protection around the account once it is leased. Accounts with a budget are wiped automatically when the budget is reached. The right budget for your lease can depend on multiple factors including (but not limited to):
+ The type of workloads that will be run on the accounts: For instance, you might want to set a higher budget for accounts that will be used for machine learning workloads.
+ The experience of the user: A user with little or no experience with AWS might incur more costs than an experienced user.
+ The purpose of the account: Accounts used for testing might have a lower budget than other accounts.

**Note**
The maximum budget you can set is limited by the **Max budget** setting in the **Lease Policies** section of the **Settings** page. An administrator of your Innovation Sandbox environment sets this value. For more information, see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

When you set a maximum budget a threshold is automatically created for you. This threshold will wipe the account once that budget is reached.

![Default threshold when a budget is set](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/auto-budget-threshold.png)

**Default threshold when a budget is set**
You can also set additional thresholds to send alerts or freeze the account at different budget levels. They can be used to keep track of the spending and take action if necessary.

### Duration thresholds
<a name="duration-thresholds"></a>

 **Use case 3: Not setting a duration**

Leases with no duration will only terminate if a maximum budget is set, if manually terminated by a manager or administrator, or if terminated by the leaseholder when the **Allow user lease termination** setting is enabled (see [Terminating your lease](user-section.md#terminate-your-lease)). Hence, it is important to keep this in mind when turning off **Enable Maximum Duration**. In addition, choosing this option will not allow you to set any thresholds. We recommend using leases with no durations, for workloads that are expected to run for an unknown amount of time.

 **Use case 4: Setting a duration with thresholds**

The duration configuration determines how long the account is available once leased to a user. The thresholds are measured in hours. It is important to note that the threshold’s actions are only triggered when a certain amount of hours is left.

![Standard duration threshold](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/standard-duration-threshold.png)

**Standard duration threshold**
In this example, an alert is sent when 5 hours are left on the lease. It gives the user time to save their work if they want. Once the lease terminates, the account goes through the cleanup process.

## Managing leases
<a name="manage-leases"></a>

As a Manager or Administrator, you can view and manage the status of leases. Leases give users access to a temporary AWS account. Their budget and duration configuration are defined by its corresponding lease template.

A lease is owned by the user who requested it. When lease sharing is enabled, a lease can also be shared with additional users and groups for collaboration. For more information, refer to [Sharing a lease with additional users and groups](#lease-sharing).

![Leases page showing the All Leases tab with property filter and Access Type column](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/leases-page.png)

You can view all leases on the **Leases** page. The page organizes leases into three tabs: **All Leases**, **My Leases** (leases you own), and **Shared with me** (leases others have shared with you). The **Name** column identifies each lease as `<lease template name> (<first 8 characters of the lease UUID>)`. The **UUID** column shows the same value in full. Use the property filter to narrow the list by properties such as lease name, owner, status, lease template, AWS account, or access type, and use the table preferences to choose which columns are visible. By default, each tab shows leases in an active state (Pending Approval, Active, Frozen, and Provisioning).

To change lease status:

1. On the Lease page, select a lease from the list of leases.

1. Under **Actions**, choose the appropriate option to **Freeze**, **Terminate**, **Unfreeze** or **Update** a lease.
   + When a lease is frozen, the user can view leases under their accounts, but cannot access the account through the AWS console.
   + When a lease is terminated, the user loses all access to the AWS account and will need to request a new lease.
   + When a lease is unfrozen, the user regains full access to their AWS account and can continue working with their resources. Only frozen leases can be unfrozen.
   + Updating a lease allows you to increase the budget, extend the duration, update thresholds or change the cost report group of the lease.

**Note**
When the **Allow user lease termination** global configuration setting is enabled, sandbox users can also terminate their own Active leases without any Manager involvement. These self-service terminations are recorded with the **Terminated by User** lease status.

**Note**
When updating a lease, you can extend or reduce the budget of the lease. If you reduce the budget and the user has already spent more than the new budget, the account will go through the cleanup process once Innovation Sandbox detects that the new budget has been reached. The detection process runs once every hour.

**Important**
You cannot reactivate terminated leases.

### Leases states in Innovation Sandbox
<a name="understand-lease-states"></a>

This table explains the various states the leases can be in at any given time.

| State | Description |
| --- | --- |
| Active | The lease is actively being used by a sandbox user. |
| Frozen | The lease has been frozen either by reaching a predefined freeze threshold (based on spend or lease duration) or through manual action by an Admin or Manager. Sandbox users will no longer have access to the lease but the account could still have active AWS Resources running in it, that you will be billed for. If you want to preserve the resources in the account, we recommend an Admin review and eject the account out of the account pool. |
| Pending Approval | The lease request is pending approval from an Admin or a Manager. |
| Approval Denied | The lease request has been denied by an Admin or a Manager. |
| Lease Duration Expired | The lease has reached its predefined maximum lease duration and the resources in the account are being cleaned up. |
| Lease Manually Terminated | The lease has been manually terminated by an admin or a sandbox manager and the resources in the account are being cleaned up. |
| Terminated by User | The lease has been terminated by the leaseholder, using the self-service **Terminate lease** action, and the resources in the account are being cleaned up. For more information, refer to [Terminating your lease](user-section.md#terminate-your-lease). |
| Account Quarantined | The clean up process failed to terminate some of the resources in the account and manual intervention is required by the Admin to complete clean up. We recommend the [Admin manually clean up the remaining resources in the account and initiate Retry Cleanup](administrator-guide.md#manage-accounts) to complete the clean up process. This state also occurs when an Administrator manually quarantines the backing account; in that case, the lease is terminated as part of the quarantine action. |
| Account Manually Ejected | An Admin has manually ejected the account out of account pool. |
| Provisioning | A blueprint is being deployed to the sandbox account. The user does not have access yet. If deployment succeeds, the lease becomes Active. If it fails, the lease is terminated and the account is cleaned up. |
| Provisioning Failed | Blueprint deployment failed. The lease has been terminated and the account is being cleaned up. |

## Viewing your lease costs
<a name="lease-costs"></a>

As a Manager or Administrator, you can view the costs incurred by the leases. This allows you to keep track of the costs of your leased accounts.

You can view all leases on the **Leases** page. Each lease will display the amount spent on the lease so far under the **Budget** column. If the lease has a fixed budget, you will be shown a progress bar, showing how close the lease is to reaching the budget. All leases will also display the current spent inside the lease.

By default, the **Leases** page shows leases in an active state (Pending Approval, Active, Frozen, and Provisioning). To see the costs incurred by terminated leases, adjust the status property filter.

Administrators with access to the organization’s management account can access the [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html) console for full data on spending in their organization.

**Note**
Cost Explorer refreshes your cost data at least once every 24 hours. For more information, refer to the [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) page.

## Accessing user accounts for troubleshooting
<a name="troubleshoot"></a>

Managers or Administrators may need to access a user’s AWS account for troubleshooting.

To access a user’s account, from the **Leases** page, find the lease corresponding to the account. If the lease is active, the **Login** option will be visible under the **Access** column. This will allow you to access the AWS Access portal, where you can log in using one of the available IAM roles.
