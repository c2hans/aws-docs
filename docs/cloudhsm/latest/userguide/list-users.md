---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/list-users.html
---

# List all HSM users in the cluster using AWS CloudHSM Management Utility
<a name="list-users"></a>

 Use **listUsers** command in the AWS CloudHSM Management Utility (CMU) to list all the users in the AWS CloudHSM cluster. You do not have to log in to run **listUsers** and all user types can list users.

**To list all users on the cluster**

1. Use the configure tool to update the CMU configuration.

------
#### [ Linux ]

   ```
   $ sudo /opt/cloudhsm/bin/configure --cmu {{<IP address>}}
   ```

------
#### [ Windows ]

   ```
   PS C:\> & "C:\Program Files\Amazon\CloudHSM\configure.exe" --cmu {{<IP address>}}
   ```

------

1. Start CMU.

------
#### [ Linux ]

   ```
   $ /opt/cloudhsm/bin/cloudhsm_mgmt_util /opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg
   ```

------
#### [ Windows ]

   ```
   PS C:\> & "C:\Program Files\Amazon\CloudHSM\cloudhsm_mgmt_util.exe" C:\ProgramData\Amazon\CloudHSM\data\cloudhsm_mgmt_util.cfg
   ```

------

1.  Use **listUsers** to list all the users on the cluster.

   ```
   aws-cloudhsm > listUsers
   ```

   CMU lists all the users on the cluster.

   ```
   Users on server 0(10.0.2.9):
   Number of users found:4

       User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
            1              AU              app_user                                 NO               0               NO
            2              CO              example_officer                          NO               0               NO
            3              CU              example_user                             NO               0               NO
   Users on server 1(10.0.3.11):
   Number of users found:4

       User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
            1              AU              app_user                                 NO               0               NO
            2              CO              example_officer                          NO               0               NO
            3              CU              example_user                             NO               0               NO
   Users on server 2(10.0.1.12):
   Number of users found:4

       User Id             User Type       User Name                          MofnPubKey    LoginFailureCnt         2FA
            1              AU              app_user                                 NO               0               NO
            2              CO              example_officer                          NO               0               NO
            3              CU              example_user                             NO               0               NO
   ```

For more information about **listUsers**, see [listUsers](cloudhsm_mgmt_util-listUsers.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
