---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html
---

# Account lifecycle
<a name="account-lifecycle-in-isb"></a>

This section describes how an account statuses and OU location changes throughout its lifecycle.

![sandbox account ou lifecycle](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/sandbox-account-ou-lifecycle.png)

**Account lifecycle**

1. The account is onboarded into the solution from the **Entry** OU. This is a manual action performed by an administrator that sends the account to clean-up. This sanitizes the account to ensure no previously existing resources make it into the sandbox environment.

1. If the clean-up is successful, an event is produced detailing that the account has been successfully cleaned up. This moves the account to **Available** state.

1. Once available, the lease approval flow will attempt to claim an available sandbox account. Lease approval is a manual API action. During this, the account will move to **Active** state, and a user will be granted access, and the lease’s incurred cost and duration will start being monitored.

1. (Optional) **Frozen** status: The account can be sent to a **Frozen** status either manually via an API request, or when the monitoring process detects that a configured threshold for the lease was breached. This revokes account access for the sandbox user and allows the Admin and Manager to review the contents of the account. From the Frozen state, administrators and managers can unfreeze the lease to restore user access, returning the account to **Active** status.

1. From Frozen or Active status, the account can be manually cleaned up by an API request, or the lease monitoring service detecting that the account has reached the end of its configured lease terms. The account will be moved back to **CleanUp** to delete resources that were created under the previous lease so that the account can be used again.

1. During clean-up, if deletion fails (resources were unable to be deleted or an unexpected failure occurs), the account is moved to **Quarantine**. Accounts in Quarantine require manual remediation from the administrator and can only return to the account pool by retrying cleanup and succeeding. Accounts can also be quarantined if drift between the expected account location and actual OU location is detected by the drift monitor Lambda. In this case the account will bypass clean-up, and move straight to Quarantine.

1. From any lifecycle status except accounts going through ongoing clean-up, the account can be **ejected** from the solution. During the ejection process, the solution relinquishes control over the account and places it in a boundary OU named **Exit** where an administrator can safely move it from the account pool. This is useful for preserving work in an account indefinitely, removing a problematic account from the solution, or downsizing the account pool.
