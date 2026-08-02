---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-policy-statement.html
---

# Creating the delegated administrator policy in Security Hub
<a name="securityhub-v2-policy-statement"></a>

 The AWS organization management account can create a policy allowing the delegated administrator to configure Security Hub and perform specific actions in AWS Organizations. The procedure in this topic describes how to create the policy. When completing the procedure, you can allow Security Hub to create the policy for you or manually create the policy. We recommend allowing Security Hub to create the policy for you, unless you want to customize the policy for a particular use case. The AWS organization management account must complete this procedure only if it enabled Security Hub and designated a delegated administrator, but skipped creating the policy when completing the [enablement](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-enable.html#securityhub-v2-enable-management-account) workflow. For information about how to update this policy, see [Update a resource-based delegation policy with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs-policy-delegate-update.html) in the *AWS Organizations User Guide*.

**Note**
 After you complete this procedure, the delegated administrator can create a policy allowing it to manage member accounts in your organization. For more information, see [Creating a policy as the delegated administrator to manage member accounts](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-da-policy.html).

**To create the delegated administrator policy**

1.  Sign in to your AWS account with your organization management account credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home).

1.  From the navigation pane, choose **General**.

1.  For **Delegated administrator policy**, do one of the following:

   1.  (Option 1) Choose **Create policy**. Select the box under the policy statement to confirm Security Hub will automatically create a delegation policy granting all required permission to the delegated administrator.

   1.  (Option 2) Open the policy. Choose **Copy and attach**. In the AWS Organizations console, under **Delegated administrator for AWS Organizations**, choose **Delegate**, and paste the resource policy in the delegation policy editor. Choose **Create Policy**. Open the tab where you are in the Security Hub console, and choose **Configure**.
