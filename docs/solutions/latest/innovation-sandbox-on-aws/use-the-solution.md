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
+  [Approving and rejecting leases](manager-guide.md#approve-reject-account-lease)
+  [Choosing the right budget and duration configuration](manager-guide.md#choosing-thresholds)
+  [Managing leases](manager-guide.md#manage-leases)
+  [Viewing your lease costs](manager-guide.md#lease-costs)
+  [Accessing user accounts for troubleshooting](manager-guide.md#troubleshoot)

 **User Guide**
+  [Requesting a new account lease](user-section.md#request-new-account-lease)
+  [Logging in to an account](user-section.md#account-log-in)
+  [Requesting a lease extension](user-section.md#lease-extension)

The following table summarizes the actions that can be performed by each Innovation Sandbox role.

 **Accounts**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| View all accounts \+ cost/usage | Yes | No | No |
| Add new AWS accounts to the account pool | Yes | No | No |
| Eject accounts from the account pool | Yes | No | No |
| Retry cleanup process on accounts | Yes | No | No |
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
| View all leases | Yes | Yes | No |
| View leases belonging to self | Yes | Yes | Yes |
| Approve lease requests | Yes | Yes | No |
| Manually freeze lease | Yes | Yes | No |
| Manually terminate lease | Yes | Yes | No |
| Manually unfreeze lease | Yes | Yes | No |
| Manually extend lease budget/duration or lease | Yes | Yes | No |
| Login to active or frozen sandbox account as manager | Yes | Yes | No |
| Login to active sandbox account as user | Yes | Yes | Yes |

 **Settings**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| View settings page | Yes | No | No |

 **Operational**

| Action | Admin | Manager | User |
| --- | --- | --- | --- |
| Create managers | Yes | No | No |
| Configure guardrails (such as Service Control Policies) | Yes | No | No |
| Manage Terms and Conditions content | Yes | No | No |
