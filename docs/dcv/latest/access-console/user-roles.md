---
source_url: https://docs.aws.amazon.com/dcv/latest/access-console/user-roles.html
---

# User roles
<a name="user-roles"></a>

There are two roles a user can have with the Amazon DCV Access Console: admin and user. Both of these user roles can create and connect to their own sessions.

**Admin role**
+ Create sessions
+ View and connect to all sessions
+ View, create, assign and modify session templates
+ View hosts
+ View and import users
+ View, import and modify user groups

**User role**
+ Create sessions
+ View and connect to all sessions

## Changing a user's role
<a name="change-user-role"></a>

To change a user’s role, you must edit the user directly from your configured datastore. You cannot change a user's role from the Access Console.

**DynamoDB**

1. Navigate to the users table in the DynamoDB console.

1. Select **Explore Table Items**.

1. Select the entry that corresponds to the user you want to be an admin.

1. Select **Actions** then **Edit item**.

1. Modify the role to be **Admin** or **User**.

1. Select **Save and close**.

1. Connect to the Handler host.

1. Restart the Handler.

   ```
   $ sudo systemctl restart dcv-access-console-handler
   ```

**MariaDB**

1. Connect to the Handler host.

1. Enter the username of the user you want to be an admin:

   ```
   ADMIN_USER={{replace with username}}
   ```

1. Enter the database name you chose during setup. If you left it as the default, the name is `dcv_access_console`.

   ```
   DATABASE_NAME={{replace with database name}}
   ```

1. Retrieve the name of the users table.

   ```
   $ sudo mysql -e "show tables like '%User';" --database=$DATABASE_NAME
   ```

   It is the table ending in User, not `SessionTemplatePublishedToUser`.

1. Update the user role.

   ```
   USER_TABLE={{user table name}}
   ```

   ```
   $ sudo mysql -e "UPDATE $DATABASE_NAME.$USER_TABLE SET role = 'Admin' WHERE userId='$ADMIN_USER';"
   ```

1. Restart the Handler.

   ```
   $ sudo systemctl restart dcv-access-console-handler
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
