---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/user-section.html
---

# User Guide

This section contains all the information regarding actions available to an Innovation Sandbox user. After you log in to the web UI, the home page displays.

![User home page](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/user-home-page.png)

**Innovation Sandbox home page (User view)**
The home page header includes a **Request lease** button for requesting a new sandbox account lease. Below the header, the **Active Leases** section shows the sandbox accounts you can currently access, including leases you own and leases that others have shared with you. Each lease appears as a card that shows:
+ The lease name, in the format `<lease template name> (<first 8 characters of the lease UUID>)`.
+ The lease status, such as Active, Frozen, or Pending Approval.
+ The owner’s email address, with a **You** badge for leases you own or a **Shared** badge for leases shared with you.
+ The lease template, AWS account ID, time until expiry, and budget consumed.

For an active lease, choose **Login** to access the AWS account. For more information, refer to [Logging in to an account](#account-log-in). To request a new lease, refer to [Requesting a new account lease](#request-new-account-lease).

**Note**
Only leases in the Pending Approval, Active, or Frozen state appear in the **Active Leases** section. To view all of your leases, including leases that are provisioning and leases that have ended, open the **Leases** page.

## Requesting a new account lease
<a name="request-new-account-lease"></a>

You can request account leases to gain access to sandbox AWS accounts.

To request an account:

1. After logging in to the web UI, the home page will display all of your current active leases.

1. Choose **Request lease**.

1. Under **Select lease template**, choose the type of lease you’d like to request. The lease templates are created by your management and administration team.

1. Choose **Next**.

1.  *(Optional)* On the **Share access** step, add the other users you want to collaborate with in the account. When your administrator has enabled group assignments, you can also add groups. This step appears only when your administrator has enabled lease sharing globally and the selected lease template allows the lease owner to share. The step is optional, so you can skip it and share the lease later from the lease details page. For more information, refer to [Sharing a lease with additional users and groups](manager-guide.md#lease-sharing).
![Configure access step in the request lease wizard with the owner and one group, each with a permission set](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/request-lease-configure-access.png)

1. In the **Terms of Service** section, read the terms of service and check the box that says *I accept the terms of service*. Ensure that you understand the risks associated with owning a sandbox account lease.

1. Choose **Next** to proceed.

1. Review your choices and choose **Submit**. Optionally, you can add comments describing why you are requesting this account. Note that these comments are visible to the reviewer of the lease (managers or administrators).

If the account type does not require approval, your request is automatically approved and you can access the console by choosing **Login**. If it requires approval, your request will be in the **Pending Approval** state until an administrator or manager approves the request.

**Note**
If you do not see the account under **Active Leases**, you might need to reload the page. Refresh the page to view your account leases.

**Note**
Lease requests are rate limited. By default, you can request at most 10 leases within a rolling 7-day window; your Administrator can adjust this limit. If you exceed the limit, your request is rejected and the web UI displays a message stating when you can request again, for example: "You’ve reached the lease request limit. You can request another lease after 3:42 PM on April 27."

## Logging in to an account
<a name="account-log-in"></a>

Once you’ve requested an account and the lease is in an **Active** state, you can access the AWS account associated with that lease.

1. On the home page, choose **Login** for the account you want to access. This directs you to the AWS Access portal.

1. In the **Account access details** box, you will find all the available roles that can be used for logging in.

1. Select the role name you want to use. This opens a new page, redirecting you to the AWS console.

1. Alternatively, to retrieve your AWS CLI credentials, choose **Access keys** next to your desired role. This will open a pop-up with instructions for Mac, Linux, Windows and PowerShell environments.

## Using Sandbox Spaces
<a name="using-sandbox-spaces"></a>

A Sandbox Space is an AI agent chat that is attached to your lease. You describe what you want to build in plain language, and the agent creates, changes, and inspects AWS resources in your sandbox account for you. The agent runs on Amazon Bedrock models, and its usage counts toward your lease budget.

### Before you start
<a name="sandbox-spaces-requirements"></a>

To use a Sandbox Space, you need the following:
+ An **Active** lease from a lease template that offers a Sandbox Space. When you choose a lease template to request, templates that offer a Sandbox Space show a **Sandbox Space** label. For more information, refer to [Requesting a new account lease](#request-new-account-lease).
+ Sandbox Spaces turned on by your administrator. If it is turned off, the Sandbox Spaces on active leases are unavailable until it is turned on again.
+ Access to the lease as its owner, or as a user who was added to the lease individually. If you have access to the lease only through a group, you can’t open its Sandbox Space.
+ A permission set that your administrator assigned to you on the lease. The agent has the permissions of your permission set. If the permission set has a permissions boundary, the agent can’t use it. In that case, or if you have no permission set, ask your administrator for help.

### Opening a Sandbox Space
<a name="sandbox-spaces-open"></a>

You can open a Sandbox Space in any of the following ways:
+ On the home page, in the **Active Leases** section, choose **Open Space** on the lease card.
![The Active Leases section of the home page with the Open Space button on a lease card](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/home-page-open-space.png)
+ On the lease details page, choose **Open Space** at the top of the page. The page has **Summary**, **Cost**, and **Assignments** tabs, and **Open Space** is available from every tab.
![The lease details page with the Open Space button and the Summary, Cost, and Assignments tabs](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/lease-details-open-space.png)
+ On the **Leases** page, in the **Access** column of the lease, choose the down arrow (**More access options**) next to **Login**, and then choose **Open Space** from the menu.
![The Leases page with the Access column menu open to show the Open Space item next to Login](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/leases-page-open-space.png)

 **Open Space** appears only on an Active lease that has Sandbox Spaces turned on, while Sandbox Spaces is turned on for the deployment. If **Open Space** is turned off, move the pointer over it to see the reason. On the **Leases** page, the **Open Space** menu item appears only for leases where you can open the Sandbox Space. You can open a Sandbox Space only on a lease you own or were added to individually, not through a group. If the page shows **Sandbox Space unavailable**, your lease isn’t active, Sandbox Spaces is turned off, or you don’t have individual access to the lease.

The Sandbox Space page shows the lease name and the AWS account that the agent works in. Choose **Login** next to the account ID to open the account in the AWS access portal. When the conversation is empty, the page also shows a **Welcome to your Sandbox Space** message with three suggested prompts: **Create an S3 bucket for my dataset**, **List the EC2 instances in this account**, and **Set up a DynamoDB table for a todo app**.

![The Sandbox Space page showing the Login link next to the AWS account ID, with the welcome message, suggested prompts, and the message box below](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/sandbox-space-page.png)

### Chatting with the agent
<a name="sandbox-spaces-chat"></a>

1. Enter a request in the message box, and then choose the send button. When the conversation is empty, you can also choose a suggested prompt, such as *Create an S3 bucket for my dataset*. The Sandbox Space sends the prompt as soon as you choose it.

1. The response appears as the agent writes it. Until the first text arrives, the page shows **Generating a response**. You can’t send another message until the response is complete.

1. To copy a response, choose the copy button that appears after it. Each agent response shows when it was sent as a relative time, such as **5 minutes ago**. Select the time to see the exact date and time.

![Sandbox Space page showing the lease name, the AWS account with a Login link, a user message, an agent response, and the message box with the model picker](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/sandbox-space-chat.png)

If the agent can’t process a message, the page shows an error. The heading names the cause, such as **Content filter stopped the reply**, **Safety filter blocked the message**, **Model is busy**, or **Time limit reached**, and the message says what to do. If the error can be retried, choose **Try again**. If the agent had already run commands when the error happened, the error doesn’t offer **Try again**. Check the results of the commands before you send the request again, because sending it again could run them twice. If the connection is interrupted, a **Connection interrupted** banner appears. Wait for the Sandbox Space to reconnect, or choose **Reconnect**. You can’t type a message until it reconnects. If the page tells you that the agent started working on your request but the full response wasn’t delivered, check the conversation history and the resources in your account before you send the request again. Some of the actions might already be complete.

### Choosing a model
<a name="sandbox-spaces-model"></a>

Use the model picker in the message box to choose the Amazon Bedrock model that answers your next message. Models are grouped by provider. When you open the Sandbox Space, the picker selects the default model that your manager chose for the lease. If the default model is no longer available, the page shows a message and you can choose any model from the list. You can switch models between messages, but not while a response is in progress. Each message is charged at the rate of the model that you chose for it.

Models differ in how reliably they run actions in your account. If a model describes what it would do without making the change, switch to a different model.

### Tracking your spending
<a name="sandbox-spaces-budget"></a>

The agent’s model usage counts toward the budget of your lease. In the message box, choose the budget ring icon, which fills as the lease uses its budget. The **Lease budget** popover shows how much of the lease budget is used, and an estimate of how much your Sandbox Space used. The two amounts come from separate sources, so don’t add them together. The lease amount updates about every 10 minutes through Amazon Bedrock token monitoring, so the ring doesn’t move right after each message. The Sandbox Space estimate is for information only. It isn’t added to the lease spend and doesn’t trigger budget thresholds. The ring turns to a warning color when the lease reaches its first alert threshold, and to an error color at the first freeze threshold or the maximum budget. If the lease has no maximum budget, the ring stays empty. If you own the lease, the **Cost** tab on the lease details page shows what the lease spent, including Amazon Bedrock token usage, while the lease is **Active** or **Frozen** and after it ends.

![The Lease budget popover in a Sandbox Space showing the lease spend and the estimated Sandbox Space spend](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/sandbox-space-lease-budget.png)

When the lease reaches a budget threshold, the action that is configured for the threshold applies. For example, a lease that freezes at a threshold also becomes unavailable in the Sandbox Space. For more information, refer to [Choosing the right budget and duration configuration](manager-guide.md#choosing-thresholds).

### Conversation history
<a name="sandbox-spaces-history"></a>

Your conversation stays with your lease. If you close the browser and return, or leave the page and open the Sandbox Space again, your earlier messages load automatically as you scroll up. Each lease has one conversation for each user, and you can’t start a new conversation. If earlier messages can’t be loaded, an alert tells you so. Choose **Retry** in the alert to load them again.

When your lease ends, you can no longer open its Sandbox Space. The solution deletes what the agent remembered about the lease when the lease terminates, and your stored conversation history expires no later than 30 days after each message.

### What the agent can access
<a name="sandbox-spaces-boundaries"></a>

The agent works only in the sandbox account of your lease, with the permissions of your permission set. The service control policies that apply to sandbox accounts also apply to the agent. An action that your permission set or the service control policies don’t allow fails with an access denied error, the same as it would in the AWS Management Console. The agent can’t change the solution’s own resources in your account, and it can’t use AWS Organizations, IAM Identity Center, or account management services.

A content safety guardrail screens your messages and the output of the commands that the agent runs. If the guardrail blocks a message, rephrase it and try again.

**Note**
The agent can change and delete the resources in your sandbox account that you can change and delete. Review the changes that you ask it to make, the same as you would when you work in the account yourself.

## Viewing your lease spend and budget alerts
<a name="view-your-lease-spend"></a>

You can track the spend of a lease you own in these places:
+ Home page lease card: **Budget** shows the lease’s current cost against its maximum budget.
+ Lease details page, **Summary** tab: **Budget Settings** shows **Budget Status**, **Estimated cost tracking**, **Amazon Bedrock token monitoring**, and **Spend rate thresholds**.
+ Lease details page, **Cost** tab: See [Using the lease Cost tab](manager-guide.md#lease-cost-tab).

Your lease’s budget, thresholds, and cost tracking settings come from its lease template, and only administrators and managers can change them. To ask for a higher budget, see [Requesting a lease extension](#lease-extension).

If an administrator turns on email notifications and configures a sender address, you receive an email notification when your lease reaches a budget, spend rate, or duration threshold. This includes when a threshold freezes the lease or its maximum budget terminates it. An administrator can use the SNS integration topic instead of email, use both notification channels, or turn both channels off. For more information, see [Notifications when a threshold is reached](manager-guide.md#threshold-notifications) and [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings).

## Terminating your lease
<a name="terminate-your-lease"></a>

If you finish using your sandbox account before your lease’s budget or duration limit is reached, you can terminate the lease yourself. Terminating your lease returns the account for cleanup and reuse, with no action required from an Admin or Manager.

**Note**
Your Administrator controls this self-service action through the **Allow user lease termination** global configuration setting, which is enabled by default. The **Terminate lease** button is only available on your own leases that are in the **Active** state. Leases that are not in the **Active** state cannot be self-terminated; contact your Admin or Manager if you need to terminate one of these leases.

To terminate your lease:

1. Locate the **Active** lease you want to terminate, and choose **Terminate lease**. This action is available on the lease card in the **Active Leases** section of the home page, and on the lease details page.

1. In the confirmation dialog, review the warning and verify the **AWS Account ID** and **Lease ID** shown.

1. Enter `terminate` into the confirmation field.

1. Choose **Terminate Lease**.

**Important**
Terminating a lease cannot be undone. Your access to the account is revoked immediately. If you need to use a sandbox account again, you need to request a new lease. New lease requests are subject to rate limiting; for more information, refer to [Requesting a new account lease](#request-new-account-lease).

## Viewing leases shared with you
<a name="shared-leases"></a>

When another user or a manager shares a lease with you (directly or through a group you belong to), you can access the sandbox account without requesting your own lease. Shared leases appear in two places:
+ The **Active Leases** section on your home page, alongside leases you own, for any lease in an active state. For an active lease, choose **Login** to access the AWS account, the same way you access a lease you own. For more information on logging in, refer to [Logging in to an account](#account-log-in).
+ The **Shared with me** tab on the **Leases** page, which lists every lease others have shared with you, along with its owner, account ID, status, and how it was shared (directly or through a group).

**Note**
You have the same account access as the lease owner, but you cannot terminate the lease or change its settings. Managers and administrators can manage any lease. Depending on your solution’s configuration, the lease owner can also terminate their own lease and manage who it is shared with.

**Note**
If a lease is shared with you through a group, it can take up to 24 hours for changes to your group membership to be reflected in the shared lease views. Your access to the AWS account itself updates immediately through IAM Identity Center.

## Requesting a lease extension
<a name="lease-extension"></a>

If you would like to extend your **Active** lease, contact your Admin or Manager to [update your lease to extend lease duration or increase the budget](manager-guide.md#manage-leases). They will receive a notification and update the lease (subject to availability).

**Note**
If the lease has already expired, you cannot extend the lease and will need to request a new lease.
