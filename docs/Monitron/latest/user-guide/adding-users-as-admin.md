---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/adding-users-as-admin.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Adding users as an admin
<a name="adding-users-as-admin"></a>

As an admin, you can add other users (including other admin users) in the Amazon Monitron web app.

1. Navigate to the project or site that you want to add a user to, and then to the **Users** list.
![Users and Permissions page showing a table with 8 users, their roles, assigned locations, and project level access.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/user-10.png)

1. Enter a user name. Amazon Monitron searches the user directory for the user.

   Choose the user from the list and the role you want to assign to the user: **Admin**, **Technician**, or **Viewer**.

   Then, choose **Add user**.
![Add user dialog with Username search field and Role dropdown set to Choose a role.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/user-1.png)

1. The new user appears on the **Users** list.
![Users table showing User 10 added with Technician role and No inherited user status.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/user-3.png)

   Send the new user an email invitation with a link for accessing the project and downloading the Amazon Monitron mobile app. For more information, see [Sending an email invitation](resending-email.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
