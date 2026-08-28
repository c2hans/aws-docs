---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/userguide/delete-user.html
---

# Delete HSM users using AWS CloudHSM Management Utility
<a name="delete-user"></a>

Use **deleteUser** in the AWS CloudHSM Management Utility (CMU) to delete a hardware security module (HSM) user. You must log in as a CO to delete another user.

**Tip**
 You can't delete crypto users (CU) that own keys.

**To delete a user**

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

1. Log in to the HSM as a CO user.

   ```
   aws-cloudhsm > loginHSM CO admin co12345
   ```

   Make sure the number of connections CMU lists match the number of HSMs in the cluster. If not, log out and start over.

1.  Use **deleteUser** to delete a user.

   ```
   aws-cloudhsm > deleteUser CO example_officer
   ```

   CMU deletes the user.

   ```
   Deleting user example_officer(CO) on 3 nodes
   deleteUser success on server 0(10.0.2.9)
   deleteUser success on server 1(10.0.3.11)
   deleteUser success on server 2(10.0.1.12)
   ```

For more information about **deleteUser**, see [deleteUser](cloudhsm_mgmt_util-deleteUser.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudHSM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudhsm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
