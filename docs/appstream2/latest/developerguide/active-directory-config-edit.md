---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-config-edit.html
---

# Editing the Directory Configuration
<a name="active-directory-config-edit"></a>

After a WorkSpaces Applications directory configuration has been created, you can edit it to add, remove, or modify organizational units, update the service account username, or update the service account password.

**To update a directory configuration**

1. Open the WorkSpaces Applications console at [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2).

1. In the left navigation pane, choose **Directory Configs** and select the directory configuration to edit.

1. Choose **Actions**, **Edit**.

1. Update the fields to be changed. To add additional OUs, select the plus sign (**\+**) next to the topmost OU field. To remove an OU field, select the **x** next to the field.
**Note**
At least one OU is required. OUs that are currently in use cannot be removed.

1. To save changes, choose **Update Directory Config**.

1. The information in the **Details** tab should now update to reflect the changes.

Changes to the service account sign-in credentials do not impact in-process streaming instance operations. New streaming instance operations use the updated credentials. For more information, see [Updating the Service Account Used for Joining the Domain](active-directory-service-acct.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
