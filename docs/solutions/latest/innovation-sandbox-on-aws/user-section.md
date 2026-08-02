---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/user-section.html
---

# User Guide
<a name="user-section"></a>

This section contains all the information regarding actions available to an Innovation Sandbox user. After logging in to the web UI, the following page displays.

![User home page](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/user-home-page.png)

**Innovation Sandbox Home Page (User view)**
From the home page, you can:

1. Request a new account lease. For more information see, [Requesting a new account lease](#request-new-account-lease).

1. View all of your current leases.

1. View the current state of your requested leases. In Figure 1, the user has one active lease and one lease pending approval from a manager or administrator.

1. See when your lease expires. You can hover on the status to see the exact date and time.

1. See how much of the allocated budget you have spent.

1. Log in to an account. This is only available if your lease in the **Active** state. For more information see on logging in, [Logging in to an account](#account-log-in).

## Requesting a new account lease
<a name="request-new-account-lease"></a>

You can request account leases to gain access to sandbox AWS accounts.

To request an account:

1. After logging in to the web UI, the home page will display all of your current active leases.

1. Choose **Request a new account**.

1. Under **Select lease template**, choose the type of lease you’d like to request. The lease templates are created by your management and administration team.

1. Choose **Next**.

1. In the **Terms of Service** section, read the terms of service and check the box that says *I accept the terms of service*. Ensure that you understand the risks associated with owning a sandbox account lease.

1. Choose **Next** to proceed.

1. Review your choices and choose **Submit**. Optionally, you can add comments describing why you are requesting this account. Note that these comments are visible to the reviewer of the lease (managers or administrators).

If the account type does not require approval, your request is automatically approved and you can access the console by choosing **Login to account**. If it requires approval, your request will be in the **Pending Approval** state until an administrator or manager approves the request.

**Note**
If you do not see the account under **My Accounts**, you may need to reload the page. Refresh the page to view your account leases.

## Logging in to an account
<a name="account-log-in"></a>

Once you’ve requested an account and the lease is in an **Active** state, you can access the AWS account associated with that lease.

1. On the home page, select **Login to account** for the account you want to access. This directs you to the AWS Access portal.

1. In the **Account access details** box, you will find all the available roles that can be used for logging in.

1. Select the role name you want to use. This opens a new page, redirecting you to the AWS console.

1. Alternatively, to retrieve your AWS CLI credentials, choose **Access keys** next to your desired role. This will open a pop-up with instructions for Mac, Linux, Windows and PowerShell environments.

## Requesting a lease extension
<a name="lease-extension"></a>

If you would like to extend your **Active** lease, contact your Admin or Manager to [update your lease to extend lease duration or increase the budget](manager-guide.md#manage-leases). They will receive a notification and update the lease (subject to availability).

**Note**
If the lease has already expired, you cannot extend the lease and will need to request a new lease.
