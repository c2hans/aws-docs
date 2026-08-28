---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/account-lifecycle-in-isb.html
---

# Account lifecycle
<a name="account-lifecycle-in-isb"></a>

This section describes how an account statuses and OU location changes throughout its lifecycle. In the following diagram, green arrows represent asynchronous system events and red arrows represent user-initiated actions.

![Account lifecycle diagram showing the state transitions between the Entry](http://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/diagrams/sandbox-account-ou-lifecycle.drawio.png)

**Account lifecycle**

1. The account is onboarded into the solution from the **Entry** OU. This is a manual action performed by an administrator that sends the account to cleanup. This sanitizes the account so that no previously existing resources make it into the sandbox environment.

1. If the cleanup is successful, an event is produced detailing that the account has been successfully cleaned up. This moves the account to **Available** state.

1. After the account becomes available, the lease approval flow attempts to claim it. Lease approval is a manual API action. During this, the account will move to **Active** state, and a user will be granted access, and the lease’s incurred cost and duration will start being monitored.

1. (Optional) **Frozen** status: The account can be sent to a **Frozen** status either manually via an API request, or when the monitoring process detects that a configured threshold for the lease was breached. This revokes account access for the sandbox user and allows the Admin and Manager to review the contents of the account. From the Frozen state, administrators and managers can unfreeze the lease to restore user access, returning the account to **Active** status.

1. From **Frozen** or **Active** status, a lease can be terminated, which sends the account back to **CleanUp** to delete resources from the previous lease. Lease termination can occur in three ways: automatically, when the lease monitoring service detects that the lease has reached its configured budget or duration limits; manually, by an administrator or manager; or by the leaseholder terminating their own **Active** lease when the **Allow user lease termination** setting is enabled. When a leaseholder terminates their own lease, the status is recorded as **UserTerminated**. For more information, see [Terminating your lease](user-section.md#terminate-your-lease).

1. During cleanup, if deletion fails (resources were unable to be deleted or an unexpected failure occurs), the account is moved to **Quarantine**. Accounts in Quarantine require manual remediation from the administrator and can only return to the account pool by retrying cleanup and succeeding. Accounts can also be quarantined if drift between the expected account location and actual OU location is detected by the drift monitor Lambda. In this case the account will bypass cleanup, and move straight to Quarantine.

1. From any lifecycle status except accounts going through ongoing cleanup, the account can be **ejected** from the solution. During the ejection process, the solution relinquishes control over the account and places it in a boundary OU named **Exit** where an administrator can safely move it from the account pool. This is useful for preserving work in an account indefinitely, removing a problematic account from the solution, or downsizing the account pool.

**Note**
As accounts move between these states, the solution updates the `ISB-<namespace>:Status` account cost allocation tag to reflect the current state, and applies or removes the lease-level tags on lease approval, cleanup completion, and ejection. For more information, see the [Account cost allocation tagging](account-cost-allocation-tagging.md) section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
