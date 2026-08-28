---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/use-the-solution.html
---

# Using the web UI
<a name="use-the-solution"></a>

This section provides detailed instructions on how to log into the web UI, and use the web UI as an administrator, manager, or a user.

 **Administrator Guide**
+  [Adding new accounts to the account pool](administrator-guide.md#new-accounts)
+  [Managing existing accounts](administrator-guide.md#manage-accounts)
+  [Registering and managing blueprints](administrator-guide.md#registering-managing-blueprints)
+  [Viewing or modifying Innovation Sandbox settings](administrator-guide.md#manage-settings)

 **Manager Guide**
+  [Creating and managing lease templates](manager-guide.md#creating-lease-templates)
+  [Assigning leases to users](manager-guide.md#assigning-leases)
+  [Sharing a lease with additional users and groups](manager-guide.md#lease-sharing)
+  [Approving and rejecting leases](manager-guide.md#approve-reject-account-lease)
+  [Choosing the right budget and duration configuration](manager-guide.md#choosing-thresholds)
+  [Managing leases](manager-guide.md#manage-leases)
+  [Viewing your lease costs](manager-guide.md#lease-costs)
+  [Accessing user accounts for troubleshooting](manager-guide.md#troubleshoot)
+  [Viewing Innovation Sandbox settings](administrator-guide.md#manage-settings) (read-only)

 **User Guide**
+  [Requesting a new account lease](user-section.md#request-new-account-lease)
+  [Logging in to an account](user-section.md#account-log-in)
+  [Terminating your lease](user-section.md#terminate-your-lease)
+  [Viewing leases shared with you](user-section.md#shared-leases)
+  [Requesting a lease extension](user-section.md#lease-extension)

The following table summarizes the actions that can be performed by each Innovation Sandbox role.

 **Accounts**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| View all accounts \+ cost/usage | Yes | No | No |
| Add new AWS accounts to the account pool | Yes | No | No |
| Eject accounts from the account pool | Yes | No | No |
| Retry cleanup process on accounts | Yes | No | No |
| Quarantine accounts | Yes | No | No |
| Login to sandbox accounts at any point to troubleshoot or audit | Yes | No | No |

 **Blueprints**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| View all blueprints | Yes | Yes | No |
| View blueprint details | Yes | Yes | No |
| Register blueprint | Yes | No | No |
| Update blueprint metadata | Yes | No | No |
| Unregister blueprint | Yes | No | No |

 **Lease Templates**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| View all lease templates | Yes | Yes | Yes (public only) |
| View private lease templates | Yes | Yes | No |
| Create lease template (public or private) | Yes | Yes | No |
| Delete lease template | Yes | Yes | No |
| Update lease template (including visibility) | Yes | Yes | No |

 **Leases**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| Request lease (from public templates) | Yes | Yes | Yes |
| Request lease (from private templates) | Yes | Yes | No |
| Assign lease to another user | Yes | Yes | No |
| Share a lease with additional users or groups | Yes | Yes | Owner (if enabled) |
| View assignments on any lease | Yes | Yes | No |
| View assignments on own lease | Yes | Yes | Owner |
| View leases shared with self | Yes | Yes | Yes |
| View all leases | Yes | Yes | No |
| View leases belonging to self | Yes | Yes | Yes |
| Approve lease requests | Yes | Yes | No |
| Manually freeze lease | Yes | Yes | No |
| Terminate any lease | Yes | Yes | No |
| Terminate own lease (Active leases only) | Yes | Yes | Yes |
| Manually unfreeze lease | Yes | Yes | No |
| Manually extend lease budget/duration or lease | Yes | Yes | No |
| Login to active or frozen sandbox account as manager | Yes | Yes | No |
| Login to active sandbox account as user | Yes | Yes | Yes |

**Note**
Users can terminate only their own leases, only while the lease is in the Active state, and only when the **Allow user lease termination** setting is enabled. For more information, refer to [Terminating your lease](user-section.md#terminate-your-lease).

 **Settings**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| View settings page | Yes | Yes | No |
| Edit settings | Yes | No | No |

 **Operational**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| Create managers | Yes | No | No |
| Configure guardrails (such as Service Control Policies) | Yes | No | No |
| Manage Terms and Conditions content | Yes | No | No |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Innovation Sandbox on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
