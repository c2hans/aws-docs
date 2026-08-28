---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/admin-functions.html
---

# Admin functions
<a name="admin-functions"></a>

**Note**
Only admins can perform the functions in this section, unless otherwise noted.

## Manage instance page
<a name="manage-instance-page"></a>

The Manage instance page provides a consolidated interface for managing the different facets of a DeepRacer on AWS deployment.

![Manage instance page](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_instance_management.png)

### Usage summary
<a name="usage-summary"></a>

![Usage summary](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_manage_instance_usage_summary_closeup.png)

The usage summary on the **Manage instance** page provides key metrics for your deployment at-a-glance. From this view, you can see:
+  **Training and evaluation hours used** - the number of hours that have been spent on training and evaluating machine learning users on your deployment.
+  **Models stored** - the total number of models currently stored on your deployment across all users.
+  **Storage used** - the total amount of storage space used by all models across all users on your deployment.
+  **Number of users** - the total number of users who are registered on your deployment.
+  **Registration mode** - how new users join your deployment. "Invite only" means users must be explicitly invited by an administrator.
+  **Global compute usage limit** - the maximum total compute hours that can be used across all users in your deployment for training and evaluation.
+  **Global model count limit** - the maximum total number of models that can be stored across all users in your deployment.
+  **New user compute usage limit** - the default compute usage limit that will be assigned to new users.
+  **New user model count limit** - the default model count limit that will be assigned to new users.

### Users table
<a name="users-table"></a>

![Users table](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_manage_instance_users_table_closeup.png)

The users table on the **Manage instance** page shows all of the users who are registered to your deployment. This table allows you to search by email address or alias. It also shows the following attributes for each user:
+  **Email address** - the email address that the user used when creating their account.
+  **Alias** - a custom alias selected by the user; used primarily for identifying models in races.
+  **Role** - the user’s role, either Admin, Race facilitator, or Racer.
+  **Current usage** - the number of compute hours used for training and evaluation jobs.
+  **Queued usage** - the number of compute hours that are expected to be used based on jobs that have been queued.
+  **Usage limit** - the individual compute usage limit, if any, that has been set.
+  **Model limit** - the individual model count limit, if any, that has been set.
+  **Model storage** - the amount of storage currently being used by models and artifacts.
+  **Date added** - the date when the user’s account was created.

The **Actions** menu features various user management actions that can be performed when either 0 or 1 users in the table are selected. The sections in User management expand on these actions further.

## User management
<a name="user-management"></a>

This section provides an overview of how to manage users in the DeepRacer on AWS solution.

### Invite a user
<a name="invite-a-user"></a>

![Invite a user](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_instance_manage_invite_user.png)

Admins can invite users to an instance via the Manage instance page by clicking **Actions > Invite user**. The **Actions** menu is in the upper-right corner of the Users section. Users are invited to the instance using their email address. Once you provide the email address of the user you’d like to invite, click **Invite**.

The invited user will receive an email with a temporary password which can be used to log in to the instance and set a preferred password. Once the preferred password is set, the temporary password will be invalidated and the preferred password can be used going forward.

Users who are invited to the instance are assigned to the **Racer** role by default.

### Change user permissions
<a name="change-user-permissions"></a>

![Change user role](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_manage_instance_change_role.png)

Admins can change the permission level that a given user has via the **Manage instance** page by selecting the user in the Users table, clicking **Actions > Change role**, and selecting the desired role from the list of options. Click **Change** to save your selection when ready.

If the user whose role you are updating is currently logged in, that user will need to log out and log back in for their role change to take effect. A successful role change will take 1-2 minutes to propagate and reflect in the Users table.

**Note**
For more information on each type of user and their permissions, see the Types of users section.

### Delete a user
<a name="delete-a-user"></a>

![Delete a user](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_manage_instance_delete_user.png)

Admins can delete a user from the instance via the **Manage instance** page by selecting the user in the Users table and clicking **Actions > Delete user**. Click **Delete** in the pop-up modal to confirm your choice.

**Note**
Deleting a user from the system permanently deletes their profile and all of their data. The action cannot be undone.

## Cost and usage management
<a name="cost-and-usage-management"></a>

DeepRacer on AWS provides a robust set of controls allowing admins to manage cost by setting limits on compute and storage resource utilization. Limits are effective from the time they are set, and will only allow or restrict actions that are performed after they are set.

### Global limits
<a name="global-limits"></a>

![Set global usage limit](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_manage_instance_set_global_quota.png)

Global limits allow compute and storage usage limits to be set at the instance level. These limits prevent the instance as a whole from exceeding a certain number of compute hours or storage capacity in a given month. This can help admins stay within a certain operating budget, mitigate against unexpected volume, and/or control variable costs.

 **Global compute usage limit** controls the number of compute hours that can be consumed by all users on a given instance in a given month through training and evaluating models. By default, this is set to **Unlimited**.
+ This can be viewed on the **Manage instance** page in the **Usage summary** section under **Global compute usage limit**.
+ This can be changed by clicking **Instance quotas** and either updating the value for **Global compute usage limit (hours),** or checking the box for **Unlimited**. Clicking **Confirm** will save your selection.

 **Global model count limit** controls the number of models that can be created, imported, and otherwise stored on a given instance. By default, this is set to **Unlimited**.
+ This can be viewed on the **Manage instance** page in the **Usage summary** section under **Global model count limit**.
+ This can be changed by clicking **Instance quotas** and either updating the value for **Global model count limit,** or checking the box for **Unlimited**. Clicking **Confirm** will save your selection.

### Individual limits
<a name="individual-limits"></a>

![Set individual usage limit](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_manage_instance_update_user_usage_quota.png)

Individual limits allow compute and storage usage limits to be set at the individual user level. These limits prevent a specific user from exceeding a certain number of compute hours or storage capacity in a given month.

The **individual usage limit** for a given user controls the number of compute hours that can be consumed by that users in a given month through training and evaluating models. By default, this is set to **Unlimited**.
+ This can be viewed on the **Manage instance** page in the **Users** table under the **Usage limit** column for a given user.
+ This can be changed by selecting a given user’s row in the table, clicking **Actions > Update usage quotas**, and setting the value for **Usage limit (hours)**. Clicking **Confirm** will save your selection.

The **individual model limit** for a given user controls the number of models that can be created, imported, and otherwise stored by that user on the instance. By default, this is set to **Unlimited**.

### New user limits
<a name="new-user-limits"></a>

![Set new user limit usage limit](http://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/images/deepracer_manage_instance_set_new_user_quota.png)

New user limits are default limits that are applied to any new users that are created after the limit is set.

The **new user compute usage limit** automatically sets a default limit on the number of compute hours for all accounts that are created after the limit is established or updated. By default, this is set to **Unlimited**.
+ This can be viewed on the **Manage instance** page in the **Users** table under the **New user compute usage limit** in the **Usage summary** section.
+ This can be changed by clicking **New user quotas** and either updating the value for **New user compute usage limit (hours),** or checking the box for **Unlimited**. Clicking **Confirm** will save your selection.

The **new user model count limit** automatically sets a default limit on the number of models that an accounts created after the limit is established or updated can have. By default, this is set to **Unlimited**.
+ This can be viewed on the **Manage instance** page in the **Users** table under the **New user model count limit** in the **Usage summary** section.
+ This can be changed by clicking **New user quotas** and either updating the value for **New user model count limit (hours),** or checking the box for **Unlimited**. Clicking **Confirm** will save your selection.

### Levels of precedence
<a name="levels-of-precedence"></a>

Global limits have the highest level of precedence in determining whether usage will be restricted. If the system is close to reaching a global limit, it will restrict jobs from being run even if a user has not neared or exceeded their individual limit. This is designed to help protect against cost overruns and unexpected resource utilization for the owner or operator of the solution.

Below are some examples of how levels of precedence work when it comes to limits in DeepRacer on AWS:
+ If global usage is *unlimited* and individual usage is *unlimited*, then usage will not be restricted.
+ If global usage is *limited* and individual usage is *unlimited*, then the global usage limit will control.
+ If global usage is *limited* and individual usage is *limited*, then the limit with the least capacity will control.
+ If global usage is *unlimited* and individual usage is *limited*, then the individual usage limit will control.

## Model management
<a name="model-management"></a>

**Note**
This feature is available to both admins and race facilitators.

The **Download physical car model** page allows admins and race facilitators to view all users on the instance, browse their trained models, and download physical car models (.tar.gz) for loading onto DeepRacer vehicles at physical race events.

To access the page, click **Download physical car model** under **Model Management** in the left sidebar. The page displays a table of all registered users that can be filtered by email address or racer alias. Expanding a user’s row reveals their trained models with name, status, and creation date. Click **Download** next to any model to download it in physical car format.

**Note**
Physical models are exported in .tar.gz format. If you are using Windows, you will need to install 7-Zip or another program that is capable of extracting this type of file.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
