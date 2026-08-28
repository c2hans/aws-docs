---
source_url: https://docs.aws.amazon.com/chime/latest/ag/manage-users.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# Managing users
<a name="manage-users"></a>

**Note**
The steps in this section assume that you have a set of user email addresses, or that you've connected your administrator account to Active Directory. For more information, refer to [Connecting to your Active Directory](active_directory.md), in this guide.

You use the Amazon Chime console to add and manage users. You add users by inviting them. As they accept your invitations, they appear under **Users**, which lists all the users in your account and their user details. For more information, see [Viewing user details](user-details.md).

Administrators of accounts using **Login with Amazon** (LWA) also see options to manage permission tiers and remove users from an account. These actions are managed through Active Directory or Okta, depending on which one of those you configure an account to use. For more information, see [Managing user permissions and access](manage-access.md).

**Topics**
+ [Adding users](adding-users.md)
+ [Viewing user details](user-details.md)
+ [Managing user permissions and access](manage-access.md)
+ [Changing personal meeting PINs](change-PINs.md)
+ [Managing Pro trials](manage-protrials.md)
+ [Requesting user attachments](request-attachments.md)
+ [How Amazon Chime manages automatic updates](managing-auto-update.md)
+ [Migrating users to another Team account](migrate-users.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
