---
source_url: https://docs.aws.amazon.com/wickr/latest/enterpriseadminguide/admin-provisioning.html
---

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Administrator provisioning
<a name="admin-provisioning"></a>

Once logged into the super administration panel, you can create network administrators. Network administrators will be able to configure their own networks, security groups, and manage end users.

**Important**
We recommend at least two administrators per network. Having multiple administrators ensures the maximum coverage in case of emergencies.

Complete the following procedure to create a network administrator.

1. In the navigation pane of the Wickr Super Administrator Console, choose **Admin Provisioning**.

1. On the **Admin Provisioning** page, choose **Create Admin**.

1. In the **Create Admin** dialog box that appears, do the following:

   1. (Optional) For **First Name** and **Last Name**, enter the name of the admin.

   1. For **Username**, enter the username of the admin.

   1. For **Password**, enter the password for the admin.

   1. Under **Network Membership**, select **Create new network**.

   1. Choose **Create**.
+ Network administrators can be added to an existing network using the network drop down or be assigned to a new network.
+ Network administrators’ passwords can be updated at any time.
+ Network administrators can be deleted.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
