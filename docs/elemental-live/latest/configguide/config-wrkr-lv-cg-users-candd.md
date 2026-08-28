---
source_url: https://docs.aws.amazon.com/elemental-live/latest/configguide/config-wrkr-lv-cg-users-candd.html
---

# Change and delete users
<a name="config-wrkr-lv-cg-users-candd"></a>

Administrators can change and delete users of AWS Elemental Live.

**To change or delete a user**

1. Log in to the Elemental Live web interface using administrator credentials.

1. Hover over **Settings** and choose **Users**.

1. On the **Users** screen, perform the following actions as needed:
   + To change the existing information for a user, choose **Edit** (pencil icon).
   + To reset a forgotten password, edit the user and enter a new password.
   + To force a user to reset their password the next time they log in, edit the user, and select **Force Password Reset**.
   + To reactivate a deactivated user, edit the user by extending the length of time that user password is in effect. In **Password Expires**, change **Expired** to another option.
   + To reset the API key for a user, choose **Reset API Key **(key icon). A new key is created. The user can view this key in the User Profile screen (**Settings** > **User Profile**).
   + To deactivate a user, choose **Deactivate** (banned icon).
   + To delete a user, choose **Delete** (X icon).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
