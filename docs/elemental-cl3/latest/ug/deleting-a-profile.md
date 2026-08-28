---
source_url: https://docs.aws.amazon.com/elemental-cl3/latest/ug/deleting-a-profile.html
---

# Deleting a profile
<a name="deleting-a-profile"></a>

**To delete a profile**

1. Verify that the profile is not being used:
   + On the AWS Elemental Conductor Live main menu, choose **Profiles**. Look at the **Channels** column for this profile.
   + If it specifies a number, display the **Channels** page and filter the list (if necessary) to show only channels that use this profile.
   + Modify the channels to use a different profile.

1. Go back to the **Profiles** page and choose **Delete** next to the profile name. Then choose **OK**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Conductor Live 3. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-cl3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
