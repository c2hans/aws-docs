---
source_url: https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-sync-pause-resume-sync-configurable-ADsync.html
---

# Pause and resume your sync
<a name="manage-sync-pause-resume-sync-configurable-ADsync"></a>

Pausing your sync pauses all future sync cycles and prevents any changes that you make to users and groups in Active Directory from being reflected in IAM Identity Center. After you resume the sync, the sync cycle picks up these changes from the next scheduled sync.

**To pause your sync**

1. Open the [IAM Identity Center console.](https://console.aws.amazon.com/singlesignon)

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab, choose **Actions**, and then choose **Manage Sync**.

1. Under **Manage Sync**, choose **Pause sync**.

**To resume your sync**

1. Open the [IAM Identity Center console.](https://console.aws.amazon.com/singlesignon)

1. Choose **Settings**.

1. On the **Settings** page, choose the **Identity source** tab, choose **Actions**, and then choose **Manage Sync**.

1. Under **Manage Sync**, choose **Resume sync**.
**Note**
If you see **Pause sync** instead of **Resume sync**, the sync from Active Directory to IAM Identity Center has already resumed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IAM Identity Center. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query singlesignon` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
