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

![Basic Details page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-wizard-step1-basic-details.png)

1. For **Name**, enter a descriptive name for your lease template so that you can easily keep track of it.

1.  *(Optional)* For **Description**, specify the intended purpose of the account type.

1. For **Requires Approval**, choose whether manager approval is required:
   +  **Approval required** (default): Managers must manually approve each lease request. Use this for accounts with high budgets or for experienced users.
   +  **No approval required**: Accounts are automatically assigned when requested. Use this for accounts with small budgets, testing, and small workloads.

1. For **Visibility**, choose between **Public** or **Private**:
   +  **Public**: The template appears in the general template listing and users can request leases from it through self-service.
   +  **Private**: The template is only visible to administrators and managers for direct lease assignment purposes. Users cannot see or request leases from private templates.

1. Choose **Next**.

On the **Blueprint** page, you can associate a blueprint with this lease template to pre-deploy infrastructure when leases are created.

![Blueprint page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-wizard-step2-blueprint.png)

1. Blueprint selection is enabled by default. To skip blueprint selection, turn off **Enable Blueprint Selection**.
![Blueprint page with selection disabled](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-wizard-step2-blueprint-disabled.png)

1. Choose a blueprint from the available options.

1. Choose **Next** to continue.

**Note**
When you approve a lease, the blueprint deploys to the sandbox account. If deployment fails, the lease terminates automatically and the account returns to the pool.

On the **Budget** page, configure spending limits and budget thresholds. See [Budget thresholds](#budget-thresholds) for detailed guidance.

![Budget Settings page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-wizard-step3-budget.png)

1. Choose whether to set a maximum budget:
   +  **Budget limit enabled**: Enter a value in **Maximum Spend** (measured in $USD).
   +  **Budget limit disabled**: No spending limit is enforced (not recommended for production use).

1.  *(Optional)* Add additional thresholds to send alerts or freeze the account at different spending levels:

   1. Choose **Add Threshold**.

   1. Enter a threshold value in $USD.

   1. Select an action: **Send Alert** (email notification) or **Freeze Lease** (prevents new resource creation).

1. Choose **Next**.

On the **Lease Duration** page, configure time limits and duration thresholds. See [Duration thresholds](#duration-thresholds) for detailed guidance.

![Lease Duration page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-wizard-step4-duration.png)

1. Choose whether to set a maximum duration:
   +  **Duration limit enabled**: Enter a value in **Maximum Duration (in hours)**. This determines how long the lease remains active.
   +  **Duration limit disabled**: Leases do not automatically expire (not recommended for production use).

1.  *(Optional)* Add thresholds to send alerts or freeze the account as time remaining decreases:

   1. Choose **Add a threshold**.

   1. Enter a threshold value in hours.

   1. Select an action: **Send Alert** (email notification) or **Freeze Lease** (prevents new resource creation).

1. Choose **Next**.

On the **Cost Report Group** page, optionally assign a cost report group to the lease template for cost attribution and reporting purposes.

![Cost Report Group page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-wizard-step5-cost-report.png)

1. Choose whether to set a cost report group:
   +  **Cost reporting group enabled**: You must select a cost reporting group.
   +  **Cost reporting group disabled**: No cost reporting group selection required.

1. If cost report groups have been configured by your administrator, select from the available options in the dropdown.

1. Choose **Next**.

**Note**
Cost report groups are used to generate custom cost reports that are delivered to an S3 bucket for detailed cost tracking and chargeback by department, project, or team. If the administrator has enabled the `requireCostReportGroup` setting, selecting a cost report group will be mandatory.

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

![Lease Template Details page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-details-page.png)

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

![Delete action in Actions dropdown](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/lease-template-delete-action.png)

To delete a lease template:

1. On the **Lease Templates** page, select the lease template you want to delete.

1. This will enable the **Actions** dropdown. Under **Actions**, select **Delete**.

1. Confirm your choice in the confirmation dialog and choose **Delete** to delete the template.

**Note**
Deleting a lease template will not affect any existing leases with the deleted lease template. Existing leases will continue to function normally until they expire or are terminated.

## Assigning leases to users
<a name="assigning-leases"></a>

As a Manager or Administrator, you can create leases directly on behalf of other users without requiring approval. This lease assignment feature is particularly useful for controlled distribution scenarios such as educational workshops, hackathons, or enterprise innovation initiatives where accounts need to be pre-allocated to specific users.

**Important**
The target user must exist in AWS IAM Identity Center before you can assign a lease to them. Users will receive an email notification when a lease is created on their behalf.

To assign a lease to a user:

1. In the web UI, from the left, select **Leases**.

1. Choose **Assign lease**.

1. On the **Assign lease** page, complete the wizard forms:

   1. For **Select lease template**, select from any available lease template (both public and private templates are available for assignment).

   1. For **Select User**, enter the email address of the user you want to assign the lease to. This must match their email address in AWS IAM Identity Center.

   1. For **Terms of Service**, check the box confirming that you accept the terms of service on behalf of the assigned user.

   1.  *(Optional)* For **Review & Assign**, add any relevant notes about the lease assignment for audit purposes.

1. Review your settings and choose **Submit** to create the lease assignment.

The lease will be created immediately without requiring approval, and the target user will receive an email notification with details about their new sandbox account access.

Leases you create on behalf of others will show your email address in the "Created by" field, making it easy to track which leases you’ve assigned. You can view all leases you’ve created in the **Leases** page, where they will be clearly identified with assignment details.

## Approving and rejecting leases
<a name="approve-reject-account-lease"></a>

Certain accounts require approval to be requested for a lease. When a user requests such an account, Managers or Admins need to approve the request for the user to be granted a lease.

1. From the left, select **Approvals** to view your approval requests.

1. Select the request that you would like to approve/reject. You can select multiple requests at the same time.

1. Using the **Actions** dropdown, select either **Approve request(s)** or **Deny request(s)** depending on your use case.

1. On the dialog box asking you to confirm, select **Approve** or **Deny**.

## Choosing the right budget and duration configuration
<a name="choosing-thresholds"></a>

When creating lease templates, you will be prompted to set budget and duration for the lease as well as thresholds. These thresholds determine the behavior of the lease once a budget or duration is reached. In this section, we will explore in more detail how to set these thresholds and why they are important to your Innovation Sandbox environment by looking at different use cases.

Here are the different actions that can be triggered when a threshold is reached.

| Action | Description |
| --- | --- |
| Send Alert | An alert is sent to the user notifying them that the budget or duration threshold has been reached. |
| Freeze account | The account is set to the Frozen state. The account is being used for a lease but the user no longer has access to the account. Administrators and Managers can still access the account for evaluation and review purposes. |
| Terminate account | The clean-up process will start on the account. Note that this action is only available when a maximum budget or duration is set. |

To get started with this guide, follow the instructions in [Creating and managing lease templates](#creating-lease-templates) until you reach the budget section.

### Budget thresholds
<a name="budget-thresholds"></a>

The budget configuration determines the spending limit for the account once leased. The thresholds are measured in $USD and actions are triggered when the account spending reaches the threshold value.

 **Use case 1: Not setting a budget**

If you select **Do not set a budget**, the lease will not automatically terminate, even if spending exceeds a certain limit. We recommend using this option for experienced users. It is also recommended for these leases to require approval, so you can limit their use. Bear in mind that the lease will terminate if a maximum duration is set.

You can still set thresholds on a lease with no budget. It is encouraged that you do so users can keep track of the lease usage and take action if necessary. The following figure shows an example of a lease with no budget but with thresholds set.

![Setting thresholds and no budget](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/no-budget-thresholds.png)

**Setting thresholds with no budget**
In this example, an alert is sent when the budget reaches $100, $500 and $750, and the account is frozen when the budget reaches $1000. Freezing the account prevents further user activity on the account, as any active resources will continue to incur costs. It gives managers time to investigate the spending, if needed. The user can also keep track on the spending using alerts.

 **Use case 2: Setting a budget with thresholds**

Choosing to add a budget creates an extra layer of protection around the account once it is leased. Accounts with a budget are wiped automatically when the budget is reached. The right budget for your lease can depend on multiple factors including (but not limited to):
+ The type of workloads that will be run on the accounts: For instance, you might want to set a higher budget for accounts that will be used for machine learning workloads.
+ The experience of the user: A user with little or no experience with AWS might incur more costs than an experienced user.
+ The purpose of the account: Accounts used for testing might have a lower budget than other accounts.

**Note**
The maximum budget you can set is limited by the maximum budget set in the Global configuration set by the administrator of your Innovation Sandbox environment. See [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings) for more information.

When you set a maximum budget a threshold is automatically created for you. This threshold will wipe the account once that budget is reached.

![Default threshold when a budget is set](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/auto-budget-threshold.png)

**Default threshold when a budget is set**
You can also set additional thresholds to send alerts or freeze the account at different budget levels. They can be used to keep track of the spending and take action if necessary.

### Duration thresholds
<a name="duration-thresholds"></a>

 **Use case 3: Not setting a duration**

Leases with no duration will only terminate if a maximum budget is set, or if manually terminated by a manager or administrator. Hence, it is important to keep this in mind when choosing **Do not set a maximum duration**. In addition, choosing this option will not allow you to set any thresholds. We recommend using leases with no durations, for workloads that are expected to run for an unknown amount of time.

 **Use case 4: Setting a duration with thresholds**

The duration configuration determines how long the account is available once leased to a user. The thresholds are measured in hours. It is important to note that the threshold’s actions are only triggered when a certain amount of hours is left.

![Standard duration threshold](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/standard-duration-threshold.png)

**Standard duration threshold**
In this example, an alert is sent when 5 hours are left on the lease. It gives the user time to save their work if they want. Once the lease terminates, the account goes through the clean-up process.

## Managing leases
<a name="manage-leases"></a>

As a Manager or Administrator, you can view and manage the status of leases. Leases give users access to a temporary AWS account. Their budget and duration configuration are defined by its corresponding lease template. A lease is assigned to a user and cannot be shared.

You can view all leases on the **Leases** page. Under **Filter options**, you can filter your leases, either by **lease status** (Active, Pending Approval) or **Lease Template** assigned to the lease.

To change lease status:

1. On the Lease page, select a lease from the list of leases.

1. Under **Actions**, choose the appropriate option to **Freeze**, **Terminate**, **Unfreeze** or **Update** a lease.
   + When a lease is frozen, the user can view leases under their accounts, but cannot access the account through the AWS console.
   + When a lease is terminated, the user loses all access to the AWS account and will need to request a new lease.
   + When a lease is unfrozen, the user regains full access to their AWS account and can continue working with their resources. Only frozen leases can be unfrozen.
   + Updating a lease allows you to increase the budget, extend the duration, update thresholds or change the cost report group of the lease.

**Note**
When updating a lease, you can extend or reduce the budget of the lease. If you reduce the budget and the user has already spent more than the new budget, the account will go through the clean-up process once Innovation Sandbox detects that the new budget has been reached. The detection process runs once every hour.

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
| Approval Denied | The lease request has been denied by an Admin or a a Manager. |
| Lease Duration Expired | The lease has reached its predefined maximum lease duration and the resources in the account are being cleaned up. |
| Lease Manually Terminated | The lease has been manually terminated by an admin or a sandbox manager and the resources in the account are being cleaned up. |
| Account Quarantined | The clean up process failed to terminate some of the resources in the account and manual intervention is required by the Admin to complete clean up. We recommend the [Admin manually clean up the remaining resources in the account and initiate Retry Cleanup](administrator-guide.md#manage-accounts) to complete the clean up process. |
| Account Manually Ejected | An Admin has manually ejected the account out of account pool. |

## Viewing your lease costs
<a name="lease-costs"></a>

As a Manager or Administrator, you can view the costs incurred by the leases. This allows you to keep track of the costs of your leased accounts.

You can view all leases on the **Leases** page. Each lease will display the amount spent on the lease so far under the **Budget** column. If the lease has a fixed budget, you will be shown a progress bar, showing how close the lease is to reaching the budget. All leases will also display the current spent inside the lease.

By default, the **Leases** page will only display the **Active** and **Frozen** leases. If you’d like to see the costs incurred by terminated leases, you can use the **Status** filter.

Administrators with access to the organization’s management account can access the [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html) console for full data on spending in their organization.

**Note**
Cost Explorer refreshes your cost data at least once every 24 hours. For more information, refer to the [Analyzing your costs and usage with AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) page.

## Accessing user accounts for troubleshooting
<a name="troubleshoot"></a>

Managers or Administrators may need to access a user’s AWS account for troubleshooting.

To access a user’s account, from the **Leases** page, find the lease corresponding to the account. If the lease is active, the **Login to account** option will be visible under the **Access** column. This will allow you to access the AWS Access portal, where you can log in using one of the available IAM roles.
