---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/list-users-cloudhsm-cli.html
---

# List all HSM users in the cluster using CloudHSM CLI
<a name="list-users-cloudhsm-cli"></a>

 Use **user list** command in the CloudHSM CLI to list all the users in the AWS CloudHSM cluster. You do not have to log in to run **user list**. All user types can list users.

**Follow these steps to list all users in the cluster**

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

1. Enter the following command to list all the users in the cluster:

   ```
   aws-cloudhsm > user list
   ```

For more information about **user list**, see [user list](cloudhsm_cli-user-list.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
