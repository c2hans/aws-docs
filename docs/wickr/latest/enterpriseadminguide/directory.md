---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/directory.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Team directory
<a name="directory"></a>

If SSO is not enabled on the network, network admins can create individual users. With SSO enabled, users are provisioned in the SSO provider.

Complete the following procedure to create a new user.

1. In the navigation pane of the Wickr Admin Console, choose **Team Directory**.

1. On the **Team Directory** page, choose **Create New User**.

1. In the **Create New User** dialog box that appears, do the following:

   1. For **First Name** and **Last Name**, enter the name of the user.

   1. For **Username**, enter the username of the user.

   1. For **Password**, enter the password for the user.

   1. (Optional) Select the security group for the user.

   1. Choose **Create**.

User statuses can be:
+ **Pending:** The user has not registered.
+ **Active:** The user has registered and is able to receive messages.
+ **Suspended:** The user is unable to sign in to their account, but still active.
+ **Restricted:** This notes that the user cannot use Global Federation or is strictly an administrator.
**Note**
If there is a requirement to restrict the types of devices your users can use with Wickr Enterprise, we recommend using a Mobile Device Management (MDM) solution.

User types are:
+ **User:** This user can login to the Wickr Enterprise apps.
+ **Web Admin:** This user can only log into the Network Dashboard.

Additionally, an administrator can set a visible first and last name. This will be shared with any contact across any internal network.
+ First Name
+ Last Name

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
