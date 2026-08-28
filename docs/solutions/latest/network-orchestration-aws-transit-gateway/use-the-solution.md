---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/use-the-solution.html
---

# Use the solution
<a name="use-the-solution"></a>

This section provides a user guide for the solution’s web UI and instructions to [using and customizing route tables](using-and-customizing-route-tables.md).

## Use the web UI
<a name="use-the-web-ui"></a>

**Important**
If you don’t deploy the UI, you can’t approve or reject a network change. All the network changes will be auto-approved. You can use the compliance rules to auto-approve and auto-reject network changes.

### Sign in to the web UI
<a name="sign-in-to-the-web-ui"></a>

After the hub stack is successfully deployed, you receive two emails containing a link to the web UI and sign-in credentials. By default, the solution creates one Amazon Cognito `adminuser` (in the admin group) and one Amazon Cognito `readonlyuser` (in the read-only group). For more information, refer to [Managing and searching for user accounts](https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html) in the *Amazon Cognito Developer Guide*.

**Note**
If you configured an external SAML-based identity provider in [step 3](step-3-launch-the-hub-stack.md) (**SAML Provider Name** parameter), instead of signing in with sign-in credentials, you can choose the button that redirects to your identity provider’s sign in page. On the first sign in, the solution automatically adds every user to the **ReadOnlyUserGroup** and thereby grants them read access to the web UI. After a user signs in with read access, you can assign them to the **AdminGroup** with Amazon Cognito if needed. For more information, see [Adding groups to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-user-groups.html) in the *Amazon Cognito Developer Guide*.

Follow the step-by-step instructions in this section to sign in to the web UI.

1. Choose the link to open the web UI.

1. Enter the provided user credentials to sign in. You must change the system-generated password the first time that you sign in.
**Note**
The temporary account expires if you don’t sign in within seven days. Your new password must be at least ten characters long.

### Manage network activities
<a name="manage-network-activities"></a>

You can use the web UI to access the dashboard to view network changes, access action items to view, approve or reject network requests when manual approval is required, and view the history of all changes made within the solution.

**Note**
Information and history for a VPC are set to expire based on the time you specify in the hub template at stack launch. The default time is 90 days. Expired requests are automatically deleted from DynamoDB within 48 hours and are not shown in the web UI after deletion.

#### Access the dashboard
<a name="access-the-dashboard"></a>

The **Dashboard** tab displays fields containing information about network changes stored in DynamoDB such as **VPC ID**, **VPC CIDR**, **Status**, **Association Route Table**, **Propagation Route Tables**, **Spoke Account**, **Subnet ID**, **Availability Zone**, and other relevant information. You can sort by these fields. You can also view the **Status** of each network change, including whether it was approved, rejected, auto-approved, or auto-rejected.

#### Access action items
<a name="access-action-items"></a>

The **Action Items** tab displays the requests that require [manual approval](manual-approval.md). If you chose to [automatically approve](automated-approval.md) requests, this tab will be empty. For manual approvals, each request contains the same fields as those in the **Dashboard** tab. Requests can have the following status: `requested`, `processing`, or `failed`. The reason for the failure displays in the comment column.

#### Approve or reject requests
<a name="approve-or-reject-requests"></a>

When you enable [manual approval](manual-approval.md) for requests, the administrator approves or rejects the request using the web UI. Only users in the admin group can approve or reject requests. Users from the read only group can only view requests. When an administrator approves or rejects the request, the status is set to `processing`.

When a request is `processing`, users can’t take further action from the web UI. The web UI calls a Lambda function, which initiates the solution state machine to process the request. After the process completes, state machine updates the request status, and the web UI reflects the new status.

#### View history of a request
<a name="view-history-of-a-request"></a>

To view the history of a request, select the request from either the **Dashboard** or **Action Items** tab and then choose **View History**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Network Orchestration for AWS Transit Gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
