---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/user-section.html
---

# User Guide
<a name="user-section"></a>

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

1.  *(Optional)* On the **Share access** step, add the other users and groups you want to collaborate with in the account. This step appears only when your administrator has enabled lease sharing globally and the selected lease template allows the lease owner to share. The step is optional, so you can skip it and share the lease later from the lease details page. For more information, refer to [Sharing a lease with additional users and groups](manager-guide.md#lease-sharing).
![Share access step in the request lease wizard](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/request-lease-share-access.png)

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
