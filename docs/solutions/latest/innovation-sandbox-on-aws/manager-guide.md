---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/manager-guide.html
---

# Manager Guide

This section describes the various actions a Manager can perform using the web UI.

## Creating lease templates
<a name="creating-lease-templates"></a>

As a manager or administrator, you create lease templates that define the configurations users choose when requesting a lease. A lease template includes settings for blueprints, access, Sandbox Spaces, budget limits, duration, and cost reporting. All of your available lease templates are displayed on the **Lease Templates** page.

To create a lease template, navigate to **Lease Templates** in the web UI and choose **Add new lease template**. This opens a wizard to configure your template.

<a name="step-1-basic-details"></a>****Step 1: Basic details****

On the **Basic details** page, configure the template’s name, description, visibility, and approval requirements.

![Basic details step of the Add Lease Template wizard](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step1-basic-details.png)

1. For **Name**, enter a descriptive name for your lease template so that you can keep track of it.

1.  *(Optional)* For **Description**, specify the intended purpose of the account type.

1. For **Requires Approval**, choose whether manager approval is required:
   +  **Approval required** (default): Managers must manually approve each lease request. Use this for accounts with high budgets or for experienced users.
   +  **No approval required**: Accounts are automatically assigned when requested. Use this for accounts with small budgets, testing, and small workloads.

1. For **Visibility**, choose between **Public** or **Private**:
   +  **Public**: The template appears in the general template listing and users can request leases from it through self-service.
   +  **Private**: The template is only visible to administrators and managers for direct lease assignment purposes. Users cannot see or request leases from private templates.

1. Choose **Next**.

<a name="step-2-blueprint"></a>****Step 2: Blueprint****

On the **Blueprint** page, you can associate a blueprint with this lease template to pre-deploy infrastructure when leases are created.

![Blueprint step of the Add Lease Template wizard with a blueprint selected](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step2-blueprint.png)

1. Blueprint selection is enabled by default. To skip blueprint selection, turn off **Enable Blueprint Selection**.
![Blueprint step of the Add Lease Template wizard with blueprint deployment turned off](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step2-blueprint-disabled.png)

1. Choose a blueprint from the available options.

1. Choose **Next** to continue.

**Note**
When you approve a lease, the blueprint deploys to the sandbox account. If deployment fails, the lease terminates automatically and the account returns to the pool.

<a name="template-access-settings"></a>****Step 3: Access and sharing****

On the **Access and sharing** page, choose who can share leases and which permission sets to allow.

![Access and sharing step of the Add Lease Template wizard with sharing enabled and three selected permission sets, one marked Default](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step3-access-and-sharing.png)

1. For **Allow owner to share lease**, choose whether lease owners can manage user and group assignments. You can turn this on only when lease sharing is enabled globally. Administrators and managers can manage assignments regardless of this setting.

1. Use **Add permission sets** to select up to 20 permission sets, including the default. If you keep the initial selection, leases use the built-in user permission set.

1. In **Selected permission sets**, choose **Set as default** for the permission set that new assignments should use. To remove the current default, first select another default.

1. Choose **Next**.

The allowed list provides choices for assignments. It does not grant every listed permission set to each user. For example, a template can allow both read-only and developer access while using read-only access by default.

Each new lease copies these settings. Later template edits do not change existing leases.

<a name="step-4-sandbox-space"></a>****Step 4: Sandbox Space****

On the **Sandbox Space** page, choose whether to offer users an AI agent workspace, called a Sandbox Space, on leases from this template. For more information, refer to [Using Sandbox Spaces](user-section.md#using-sandbox-spaces). The page has the **Enable Sandbox Space** toggle and a **Models** section where you choose the models that users can pick from.

![Sandbox Space step of the Add Lease Template wizard with Sandbox Space enabled, Selected models only turned on, and two models with one marked Default](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step4-sandbox-space.png)

1. Turn on **Enable Sandbox Space**. The toggle reads **Sandbox Space enabled** when it is on. Every lease created from this template is then provisioned with a Sandbox Space.

1. In the **Models** section, choose which Amazon Bedrock models users can choose from in the Sandbox Space. The section lists the models that an administrator enabled in the **Sandbox Spaces** section of the **Settings** page.
   + To offer every model that is enabled, including models that an administrator enables later, leave **Limit available models** turned off. The toggle reads **All enabled models**.
   + To offer only some models, turn on **Limit available models**. The toggle reads **Selected models only**. For **Add models**, search for and select the models to offer. You must add at least one model.

1.  *(Optional)* In the models table, choose **Set as default** for the model that the Sandbox Space selects when a user first opens it. A user can switch models at any time. The default model is marked with a **Default** badge. If you limit the models, the default model must be one of the models you added. If you don’t choose a default model, the Sandbox Space selects the first available model.

1. To remove a model that you added, choose **Remove** on its row.

1. Choose **Next**.

**Note**
The **Enable Sandbox Space** toggle is unavailable while an administrator has turned off **Enable Sandbox Spaces** in the **Settings** page. For more information, refer to [Managing Sandbox Spaces](administrator-guide.md#manage-sandbox-spaces).
Sandbox Spaces requires Amazon Bedrock token monitoring, so turning on **Enable Sandbox Space** also turns on **Amazon Bedrock token monitoring** on the **Budget** step, where it shows **Required while Sandbox Spaces is enabled.** When you turn off **Enable Sandbox Space**, token monitoring stays on, and you can turn it off in the budget settings. If an administrator turned off **Allow Bedrock token monitoring** in the **Settings** page, turning off **Enable Sandbox Space** also turns off token monitoring.
Spending by the Sandbox Space counts toward the lease budget.

<a name="template-budget-settings"></a>****Step 5: Budget****

On the **Budget** page, configure cost tracking, a maximum budget, budget thresholds, and spend rate thresholds. See [Budget thresholds](#budget-thresholds) for detailed guidance.

![Budget step of the Add Lease Template wizard showing cost tracking, budget thresholds, and spend rate thresholds](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step5-budget.png)

1. In **Cost tracking**, turn on the features for leases created from this template. A toggle is unavailable until an administrator allows the feature. See [Allowing cost tracking features](administrator-guide.md#cost-tracking-settings).
   +  **Estimated cost tracking**: Estimates each lease’s spend since the last billing update. Adds the **Estimated cost** basis for budget thresholds and makes spend rate thresholds available.
   +  **Amazon Bedrock token monitoring**: Monitors and attributes Amazon Bedrock token usage to the lease budget between Cost Explorer reports.

1. To set a maximum budget, keep **Maximum budget** on and enter the amount in the **Terminate lease** row.

1.  *(Optional)* To add a budget threshold, in **Budget thresholds**, choose **Add threshold**.

   1. For **Amount (USD)**, enter the amount.

   1. For **Action**, choose **Send alert** (notifies the lease owner) or **Freeze lease** (removes user access to the account).

   1. For **Cost basis**, keep **Reported cost** or, if **Estimated cost tracking** is on, choose **Estimated cost**. See [Reported cost, estimated cost, and current cost](#threshold-cost-basis).

1.  *(Optional)* To add a spend rate threshold, in **Spend rate thresholds**, choose **Add rate threshold**. The **Spend rate thresholds** section appears only when **Estimated cost tracking** is on. See [Spend rate thresholds](#spend-rate-thresholds).

   1. For **Rate (USD)**, enter the amount.

   1. For **Period**, choose **Per hour** or **Per day**.

   1. For **Action**, choose **Send alert** or **Freeze lease**.

1. Choose **Next**.

<a name="step-6-duration"></a>****Step 6: Duration****

On the **Duration** page, configure time limits and duration thresholds. See [Duration thresholds](#duration-thresholds) for detailed guidance.

![Duration step of the Add Lease Template wizard with a maximum duration and alert and freeze thresholds](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step6-duration.png)

1. Choose whether to set a maximum duration:
   +  **Duration limit enabled**: Enter a value in **Maximum Duration (in hours)**. This determines how long the lease remains active.
   +  **Duration limit disabled**: Leases do not automatically expire (not recommended for production use).

1.  *(Optional)* Add thresholds to send alerts or freeze the account as time remaining decreases:

   1. Choose **Add a threshold**.

   1. Enter a threshold value in hours.

   1. Select an action: **Send Alert** (email notification) or **Freeze Lease** (removes user access to the account).

1. Choose **Next**.

<a name="step-7-cost-reporting"></a>****Step 7: Cost reporting****

On the **Cost reporting** page, optionally assign a cost report group to the lease template for cost attribution and reporting purposes.

![Cost reporting step of the Add Lease Template wizard with a cost report group selected](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-wizard-step7-cost-reporting.png)

1. Choose whether to set a cost report group:
   +  **Cost reporting group enabled**: You must select a cost reporting group.
   +  **Cost reporting group disabled**: No cost reporting group selection required.

1. If cost report groups have been configured by your administrator, select from the available options in the dropdown.

1. Choose **Next**.

**Note**
Cost report groups are used to generate custom cost reports that are delivered to an S3 bucket for detailed cost tracking and chargeback by department, project, or team. If the administrator has enabled the **Require cost report group** setting on the **Settings** page, selecting a cost report group will be mandatory.

<a name="step-8-review-and-submit"></a>****Step 8: Review and submit****

On the **Review and submit** page, review all your settings before creating the template.

1. Review each section of your configuration:
   + Basic Details
   + Blueprint Details
   + Budget Settings
   + Duration Settings
   + Cost Report Settings
   + Sandbox Spaces
   + Access and sharing

1. If you need to make changes, use the wizard navigation to return to a previous step.

1. When you’re satisfied with the configuration, choose **Create lease template** to create the lease template.

**Note**
The new lease template will be available for users to request leases (if public) or for managers to assign leases (if private).

## Updating lease templates
<a name="updating-lease-templates"></a>

After creating a lease template, you can modify its configuration from the lease template details page. Each section of the template can be edited independently.

![Lease template details page showing each configuration section with an Edit button](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-details-page.png)

To update a lease template:

1. On the **Lease Templates** page, select the template name to open the details page.

1. The details page displays all configuration sections with their current settings:
   +  **Basic Details**: Name, Description, ID, Created By, Visibility (Public/Private), Requires Approval (Yes/No)
   +  **Blueprint Details**: Blueprint ID, Blueprint Name (or "No Blueprint" if not configured)
   +  **Budget Settings**: Maximum Budget, Estimated cost tracking, Amazon Bedrock token monitoring, Spend rate thresholds, Budget Thresholds (each with its action and cost basis)
   +  **Duration Settings**: Maximum Duration, Duration Thresholds (with alert and freeze actions)
   +  **Cost Report Settings**: Cost Report Group (or "Not assigned" if not configured)
   +  **Sandbox Spaces**: **Sandbox Spaces** (Enabled, Disabled, or Disabled (overridden)), **Allowed models**, and **Default model**
   +  **Access settings**: **Lease sharing** (Enabled, Disabled, or Disabled (overridden)), the default permission set, and the additional permission sets that are available for assignments

1. Choose the **Edit** button next to the section you want to modify.

1. Make your changes on the edit page for that section.

1. Choose **Save changes** to update the lease template.

To remove a blueprint, choose **Edit** on the Blueprint Details section. Turn off **Enable Blueprint Selection** and choose **Save changes**. New leases created from this template will no longer deploy blueprint infrastructure.

To change the Sandbox Spaces settings of a template, refer to [Editing Sandbox Spaces settings on lease templates and leases](#manage-lease-sandbox-spaces).

To change permission sets:

1. In **Access settings**, choose **Edit**.

1. Add or remove permission sets. For the selection rules, see [Access and sharing](#template-access-settings).

1. To change the default, choose **Set as default** for a selected permission set.

1. Choose **Save changes**.

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

<a name="monitoring-assigned-leases"></a>****Monitoring assigned leases****

Leases you create on behalf of others will show your email address in the "Created by" field, making it easy to track which leases you’ve assigned. You can view all leases you’ve created in the **Leases** page, where they will be clearly identified with assignment details.

## Changing lease access settings
<a name="lease-access-settings"></a>

Administrators and managers can change a lease’s allowed permission sets, default permission set, and sharing setting independently of its template. Changing the default affects new assignments. Existing assignments keep their selected permission set.

1. On the **Leases** page, choose the lease name.

1. In **Access settings**, choose **Edit**.
![Access settings section of the lease details page showing lease sharing enabled, the allowed permission sets, and the Edit button](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-access-settings-section.png)

1. Add or remove permission sets. The limit is 20 permission sets, including the default.
![Edit Access Settings page for a lease with sharing enabled and three selected permission sets, one marked Default](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-edit-access-settings.png)

1. To change the default, choose **Set as default** for a selected permission set.

1. Choose **Save changes**.

To change an existing assignment, use the [Assignments tab](#lease-sharing-add).

Before removing an allowed permission set, change or remove the assignments that use it. If saving reports a conflict, follow the error’s link to the affected lease’s **Assignments** tab, resolve those assignments, and try again. For a frozen lease, unfreeze it before editing assignments.

## Sharing a lease with additional users and groups
<a name="lease-sharing"></a>

Share a lease to collaborate with other users in the same sandbox account. You can add individual users and, when group assignments are enabled, AWS IAM Identity Center groups. For each user or group assignment, select one of the lease’s allowed permission sets. Shared users cannot terminate the lease or change its budget, duration, or other core settings.

**Important**
Lease sharing is turned off by default. An administrator must turn on the **Enable lease sharing** setting, in the **Lease policies** group of the **Settings** page, before lease owners can share leases. While the setting is off, administrators and managers can still view and manage assignments on existing leases. Turning the setting off does not revoke access that has already been granted through sharing; to remove existing shared access, an administrator or manager must remove the principals from each lease individually, or terminate the lease. For more information, refer to [Global configuration settings](administrator-guide.md#global-settings).
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

![Assignments tab on the lease details page showing a permission set for each principal and an expanded staged permission-set change](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-assignments-tab.png)

You manage sharing from the **Assignments** tab on the lease details page. Changes you stage on this tab are applied together when you save, so you can add and remove several principals in a single update.

1. From the **Leases** page, choose the lease name to open the lease details page.

1. Choose the **Assignments** tab.

   The tab lists users and groups, their permission sets, and the status of each assignment. The lease owner appears first, marked with an **Owner** badge.

1. To add a principal, use the search field to find a user by name or email address, then choose the user from the results. When **Allow group assignments** is set to **Allow all groups**, you can also search for and add a group by its name. You can enter an exact email address or, when group assignments are enabled, an exact group name and choose the **Add** option from the dropdown. The principal is added to the list immediately as a staged change.
**Note**
When you choose a group, a confirmation dialog opens. Choose **Add group** to confirm. All current and future members of that group receive access to the sandbox account. Group membership is managed in IAM Identity Center. If you add or remove members of the group there, their access to the sandbox account changes automatically.

1. New assignments use the lease’s default permission set. To use a different one, select another allowed permission set in the principal’s row. You can also change the permission set for an existing assignment, including the owner’s.

1. To remove a principal, choose **Remove** on that row.

1. Review your staged changes, then choose **Save changes** to apply them. Choose **Undo** to reverse a staged removal or permission-set change. To discard all staged changes, choose **Cancel**.

A permission-set change can require both revoking the old assignment and granting the new one. Expand the row to view the operations and their status. Revoking an assignment prevents future sign-ins through it but does not end an existing AWS account session.

Each user or group appears once in the assignment list. A person can still have more than one role in the AWS access portal through separate group memberships or administrative access; a direct user assignment does not override those grants.

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

When you create a lease template, you set a budget, a duration, and thresholds for its leases. These thresholds determine what happens when a lease reaches a budget, spend rate, or duration threshold. This section uses example use cases to show how to set thresholds and why they matter.

Here are the different actions that can be triggered when a threshold is reached.

| Action | Description |
| --- | --- |
| Send alert | Innovation Sandbox notifies the lease owner that the lease reached a budget, spend rate, or duration threshold. |
| Freeze lease | Innovation Sandbox sets the account to the Frozen state. The account stays leased, but the user no longer has access to it. Administrators and managers can still access the account for review. |
| Terminate lease | The cleanup process starts on the account. This action is available only when a maximum budget or duration is set. |

To get started with this guide, follow the instructions in [Creating and managing lease templates](#creating-lease-templates) until you reach the budget section.

### Budget thresholds
<a name="budget-thresholds"></a>

The budget configuration determines the spending limit for the account once leased. Thresholds are set in USD. A threshold triggers its action when the lease’s cost, measured by the threshold’s **Cost basis**, reaches the threshold value. See [Reported cost, estimated cost, and current cost](#threshold-cost-basis).

 **Use case 1: Not setting a budget**

If you turn off **Maximum budget**, the lease doesn’t terminate automatically, even if spending exceeds a certain limit. We recommend this option for experienced users. We also recommend that these leases require approval, so you can limit their use. The lease still terminates if a maximum duration is set.

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
The maximum budget you can set is limited by the **Max budget** setting in the **Lease policies** group of the **Settings** page. An administrator of your Innovation Sandbox environment sets this value. For more information, see [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

When **Maximum budget** is on, a **Terminate lease** row appears below your thresholds. Enter the maximum budget in this row. When the lease’s current cost reaches this amount, Innovation Sandbox terminates the lease and cleans up its account.

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

**Important**
If a lease template or lease uses **Estimated cost tracking**, set a maximum duration of 48 hours or more. A new lease can take up to 2 days to get a spend rate, so **Estimated cost** and spend rate thresholds might never fire on a shorter lease.

### Reported cost, estimated cost, and current cost
<a name="threshold-cost-basis"></a>

Each budget threshold has a **Cost basis**. The maximum budget always uses current cost.

| Cost basis | What it measures |
| --- | --- |
| Reported cost | The lease’s billed cost from AWS Cost Explorer. This is the default. |
| Estimated cost | Reported cost plus an estimate of the spend since the last billing update, based on the lease’s spend rate. With **Amazon Bedrock token monitoring** on, the estimate starts from current cost and projects only non-Bedrock spend. Available while **Estimated cost tracking** is on. |
| Current cost | Reported cost, with billed Amazon Bedrock token charges replaced by their monitored cost while **Amazon Bedrock token monitoring** is on. Current cost is never lower than reported cost. |

Innovation Sandbox checks thresholds every hour. With Amazon Bedrock token monitoring on, it checks budget and spend rate thresholds every 10 minutes. **Reported cost** thresholds then use current cost, so they can fire before the bill reaches their amount.

### Spend rate thresholds
<a name="spend-rate-thresholds"></a>

Spend rate thresholds send an alert or freeze the lease when it’s spending faster than a set amount **Per hour** or **Per day**. They’re available while **Estimated cost tracking** is on. The spend rate is an estimate of how fast the lease’s billed cost is rising, based on its billing updates. **Per hour** uses the two most recent updates, and **Per day** uses about the last 24 hours. A spend rate threshold fires each time the lease’s spend rate rises above it.

 **Use case 5: Combining cost bases and spend rates**

In this example, the template has a maximum budget of USD $50 and **Estimated cost tracking** on. A **Send alert** threshold at USD $25 on **Reported cost** notifies the owner even before the lease has a spend rate. A **Freeze lease** threshold at USD $40 on **Estimated cost** can freeze the lease before the bill reaches USD $40. A **Send alert** spend rate threshold of USD $2 **Per hour** flags a jump in spending since the previous billing update. A **Freeze lease** spend rate threshold of USD $20 **Per day** freezes the lease and removes user access when spending stays high.

### Notifications when a threshold is reached
<a name="threshold-notifications"></a>

The following table shows who Innovation Sandbox notifies.

| Event | Recipients |
| --- | --- |
| A budget, spend rate, or duration threshold sends an alert | Lease owner |
| A threshold freezes the lease | Lease owner, all administrators, and all managers |
| The lease reaches its maximum budget and is terminated | Lease owner, all administrators, and all managers |

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
   + When you update a lease, you can increase the budget, extend the duration, update thresholds, or change the cost report group. To change budget, threshold, or cost tracking settings, see [Changing a lease’s budget settings](#edit-lease-budget).

**Note**
When the **Allow user lease termination** global configuration setting is enabled, sandbox users can also terminate their own Active leases without any Manager involvement. These self-service terminations are recorded with the **Terminated by User** lease status.

**Note**
When updating a lease, you can extend or reduce the budget of the lease. If you reduce the budget and the user has already spent more than the new budget, the account will go through the cleanup process once Innovation Sandbox detects that the new budget has been reached. The detection process runs once every hour.

**Important**
You cannot reactivate terminated leases.

### Changing a lease’s budget settings
<a name="edit-lease-budget"></a>

Administrators and managers can change a lease’s cost tracking features, maximum budget, budget thresholds, and spend rate thresholds without changing its lease template.

To change a lease’s budget settings:

1. On the **Leases** page, choose the lease name.

1. On the lease details page, in **Budget Settings**, choose **Edit**. **Edit** appears only on Active, Frozen, and Provisioning leases.
![Budget Settings section of an active lease showing estimated cost tracking and spend rate thresholds](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-budget-settings-section.png)

1. On the **Edit Budget Settings** page, change the settings. The controls are the same as in [Step 5: Budget](#template-budget-settings) of the lease template wizard.

1. Choose **Save changes**. The message "Budget settings updated successfully." appears.

### Leases states in Innovation Sandbox
<a name="understand-lease-states"></a>

This table explains the various states the leases can be in at any given time.

| State | Description |
| --- | --- |
| Active | The lease is actively being used by a sandbox user. |
| Frozen | The lease has been frozen either by reaching a predefined freeze threshold (based on cost, spend rate, or lease duration) or through manual action by an Admin or Manager. Sandbox users no longer have access to the lease, but the account might still have active AWS resources running in it that you’re billed for. If you want to preserve the resources in the account, we recommend an Admin review and eject the account out of the account pool. |
| Pending Approval | The lease request is pending approval from an Admin or a Manager. |
| Approval Denied | The lease request has been denied by an Admin or a Manager. |
| Lease Duration Expired | The lease has reached its predefined maximum lease duration and the resources in the account are being cleaned up. |
| Lease Manually Terminated | The lease has been manually terminated by an admin or a sandbox manager and the resources in the account are being cleaned up. |
| Terminated by User | The lease has been terminated by the leaseholder, using the self-service **Terminate lease** action, and the resources in the account are being cleaned up. For more information, refer to [Terminating your lease](user-section.md#terminate-your-lease). |
| Account Quarantined | The clean up process failed to terminate some of the resources in the account and manual intervention is required by the Admin to complete clean up. We recommend the [Admin manually clean up the remaining resources in the account and initiate Retry Cleanup](administrator-guide.md#manage-accounts) to complete the clean up process. This state also occurs when an Administrator manually quarantines the backing account; in that case, the lease is terminated as part of the quarantine action. |
| Account Manually Ejected | An Admin has manually ejected the account out of account pool. |
| Provisioning | A blueprint is being deployed to the sandbox account. The user does not have access yet. If deployment succeeds, the lease becomes Active. If it fails, the lease is terminated and the account is cleaned up. |
| Provisioning Failed | Blueprint deployment failed. The lease has been terminated and the account is being cleaned up. |

## Editing Sandbox Spaces settings on lease templates and leases
<a name="manage-lease-sandbox-spaces"></a>

As a Manager or Administrator, you can change the Sandbox Spaces settings of a lease template or of an individual lease. Both use the same **Edit Sandbox Spaces** page.
+  **Lease template**: The changes apply to leases that are created from the template after you save. Existing leases keep the Sandbox Spaces settings they were created with.
+  **Lease**: A lease gets its Sandbox Spaces settings from its lease template when the lease is created. The changes apply to this lease only and take effect on the next message that the user sends. You can edit a lease that is in the **Active**, **Frozen**, or **Provisioning** state.

To edit the Sandbox Spaces settings:

1. Open the **Edit Sandbox Spaces** page:
   + For a lease template, from the left, choose **Lease Templates**, choose the template name, and then choose **Edit** in the **Sandbox Spaces** section.
   + For a lease, from the left, choose **Leases**, choose the lease name, and then choose **Edit** in the **Sandbox Spaces** section.

1. Turn **Enable Sandbox Space** on or off. If an administrator has turned off **Enable Sandbox Spaces** in the **Settings** page, you can turn off a Sandbox Space that is on, but you can’t turn it on until an administrator turns the setting back on. For more information, refer to [Managing Sandbox Spaces](administrator-guide.md#manage-sandbox-spaces).

1. If the Sandbox Space is on, choose the models in the **Models** section:
   +  **Limit available models**: Leave it off (**All enabled models**) to let users choose any model that an administrator enables. Turn it on (**Selected models only**) and use **Add models** to offer only the models you add. You must add at least one model.
   + In the models table, choose **Set as default** for the model that the Sandbox Space selects when a user first opens it. The default model has a **Default** badge. To take a model off the list, choose **Remove**.
   + If an administrator disabled the default model in the **Settings** page, the table shows it as **Disabled**. Choose **Remove** or set another default model before you save.

1. Choose **Save changes**. The button is available after you change a setting and every setting is valid. To leave without saving, choose **Cancel**.

![Edit Sandbox Spaces page for a lease template with Sandbox Space enabled, Selected models only turned on, and two models with one marked Default](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-template-edit-sandbox-spaces.png)

Turning on **Enable Sandbox Space** also turns on Amazon Bedrock token monitoring, which Sandbox Spaces requires, even when **Allow Bedrock token monitoring** is off in **Settings**. When you turn off **Enable Sandbox Space**, the page shows an information message that says whether token monitoring stays on. **Bedrock token monitoring stays on** means that **Allow Bedrock token monitoring** is on, so you can turn token monitoring off in the budget settings. **Bedrock token monitoring turned off** means that an administrator turned off **Allow Bedrock token monitoring** in **Settings**, so turning off Sandbox Spaces also turns off token monitoring. If Sandbox Spaces is globally disabled and you turn it off for an existing lease template, the message also says that existing leases created from the template keep their current settings.

The **Lease Templates** page has a **Sandbox Spaces** column that shows whether each template offers a Sandbox Space (**Enabled**, **Disabled**, or **Disabled (overridden)**). A template shows **Disabled (overridden)** when it has Sandbox Spaces turned on but an administrator turned off **Enable Sandbox Spaces** in the **Settings** page, so it has no effect.

## Viewing lease costs
<a name="lease-costs"></a>

As a manager or administrator, you can view the costs of any lease. Lease owners can view the costs of their own leases. For more information, see [Viewing your lease spend and budget alerts](user-section.md#view-your-lease-spend).

You can view lease costs in these places:
+  **Leases** page, **Budget** column: A progress bar shows the lease’s current cost against its maximum budget. For a definition of current cost, see [Reported cost, estimated cost, and current cost](#threshold-cost-basis).
+ Lease details page, **Summary** tab: **Budget Settings** shows **Budget Status**, **Estimated cost tracking**, **Amazon Bedrock token monitoring**, **Spend rate thresholds**, and **Budget Thresholds**.
+ Lease details page, **Cost** tab: See [Using the lease Cost tab](#lease-cost-tab).

By default, the **Leases** page shows leases in an active state (Pending Approval, Active, Frozen, and Provisioning). To see the costs incurred by terminated leases, adjust the status property filter.

Administrators with access to the organization’s management account can access the [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html) console for full data on spending in their organization.

### Using the lease Cost tab
<a name="lease-cost-tab"></a>

The **Cost** tab shows what a lease has spent, how fast it’s spending, and every threshold that has fired. It’s available for Active, Frozen, and ended leases.

To open the **Cost** tab:

1. On the **Leases** page, choose the lease name.

1. Choose the **Cost** tab.

![Cost tab showing the spend summary, billed and predicted spend, the current-time marker, budget, and threshold lines](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-cost-overview.png)

The tab has these sections:
+  **Spend summary**: **Billed to date**, **Predicted spend now**, **Spend rate**, **Budget exhausted by**, **Lease end date**, and **Billing data covers**. **Predicted spend now**, **Spend rate**, and **Budget exhausted by** need estimated cost tracking turned on for the lease.
+  **Spend over time**: A chart of billed and predicted spend, with the maximum budget and budget thresholds drawn as lines.
+  **Top services**: The lease’s cost by AWS service, as of the last check. Requires **Enable service cost breakdown**. For more information, see [Allowing cost tracking features](administrator-guide.md#cost-tracking-settings).
+  **Bedrock token usage**: The tokens the lease has used, by model or by token type, and their estimated cost. Appears only when Amazon Bedrock token monitoring is turned on for the lease.
+  **Breach history**: Every threshold that has fired, with the value recorded when it fired and the action taken.

![Top services table showing the services with the highest lease cost](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-top-services.png)

![Bedrock token usage panel showing usage by model and the estimated hourly token cost](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-bedrock-token-usage.png)

![Breach history table showing fired projected cost, spend rate, and billed cost thresholds](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-breach-history.png)

On this tab, **Reported cost** thresholds are labeled **billed** (**Billed cost** in **Breach history**), and **Estimated cost** thresholds are labeled **projected** (**Projected cost** in **Breach history**). For more information, see [Reported cost, estimated cost, and current cost](#threshold-cost-basis).

### How lease cost figures are calculated and updated
<a name="lease-cost-figures"></a>

Innovation Sandbox checks the billed cost of each Active and Frozen lease every hour. Billed cost comes from AWS Cost Explorer, which refreshes cost data at least once every 24 hours. For more information, see [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html).

A new lease can take up to 2 days to get a spend rate. Until then, **Predicted spend now**, **Spend rate**, and **Budget exhausted by** show **Not enough data yet**.

With Amazon Bedrock token monitoring on, Innovation Sandbox also reads the lease’s Amazon Bedrock token usage every 10 minutes.

## Accessing user accounts for troubleshooting
<a name="troubleshoot"></a>

Managers or Administrators may need to access a user’s AWS account for troubleshooting.

To access a user’s account, from the **Leases** page, find the lease corresponding to the account. If the lease is active, the **Login** option will be visible under the **Access** column. This will allow you to access the AWS Access portal, where you can log in using one of the available IAM roles.
