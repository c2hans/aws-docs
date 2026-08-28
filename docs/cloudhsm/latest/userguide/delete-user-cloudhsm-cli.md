---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete-user-cloudhsm-cli.html
---

# Delete HSM users using CloudHSM CLI
<a name="delete-user-cloudhsm-cli"></a>

Use **user delete** in the CloudHSM CLI to delete a hardware security module (HSM) user. You must log in as an admin to delete another user.

**Tip**
 You can't delete crypto users (CU) that own keys.

**To delete a user**

1. Use the following command to start CloudHSM CLI interactive mode.

------
#### [ Linux ]

   ```
   $ /opt/cloudhsm/bin/cloudhsm-cli interactive
   ```

------
#### [ Windows ]

   ```
   PS C:\> & "C:\Program Files\Amazon\CloudHSM\bin\cloudhsm-cli.exe" interactive
   ```

------

1. Use the **login** command and log in to the cluster as the admin.

   ```
   aws-cloudhsm > login --username {{<username>}} --role admin
   ```

1. The system prompts you for your password. Enter the password, and the output shows that the command was successful.

   ```
   Enter password:
   {
     "error_code": 0,
     "data": {
       "username": "{{<username>}}",
       "role": "admin"
     }
   }
   ```

1. Use the **user delete** command to delete the user.

   ```
   aws-cloudhsm > user delete --username {{<username>}} --role {{<role>}}
   ```

For more information about **user delete**, see [deleteUser](cloudhsm_cli-user-delete.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
