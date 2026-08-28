---
source_url: https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/updating-admin-password.html
---

# Updating the `fsxadmin` account password fails
<a name="updating-admin-password"></a>

When you update the password for the `fsxadmin` user, you may receive an error if it doesn't meet the password requirements set on the file system. You can view the password requirements by using the `security login role config show` ONTAP CLI or REST API command.

**To view the password requirements for a file system or SVM role**

1. To access the ONTAP CLI, establish an SSH session on the management port of the Amazon FSx for NetApp ONTAP file system or SVM by running the following command. Replace `{{management_endpoint_ip}}` with the IP address of the file system's management port.

   ```
   [~]$ ssh fsxadmin@{{management_endpoint_ip}}
   ```

   For more information, see [Managing file systems with the ONTAP CLI](managing-resources-ontap-apps.md#fsxadmin-ontap-cli).

1. The `security login role config show` command returns the password requirements for a file system or SVM role.

   ```
   FsxId0123456::> security login role config show -role {{fsxadmin}} -fields {{password_requirement_fields}}
   ```

   For the `-fields` parameter, specify any or all of the following:
   + `passwd-minlength` – The minimum length of the password.
   + `passwd-min-special-chars` – The minimum number of special characters in the password.
   + `passwd-min-lowercase-chars` – The minimum number of lowercase characters in the password.
   + `passwd-min-uppercase-chars` – The minimum number of uppercase characters in the password.
   + `passwd-min-digits` – The minimum number of digits in the password.
   + `passwd-alphanum` – Information about the inclusion or exclusion of alphanumeric characters.
   + `passwd-expiry-time` – The password expiration time.
   + `passwd-expiry-warn-time` – The password expiration warning time.

1. Run the following command to see all password requirements:

   ```
   FsxId0123456::> security login role config show -role {{fsxadmin}} -fields {{passwd-minlength, passwd-min-special-chars, passwd-min-lowercase-chars, passwd-min-digits, passwd-alphanum, passwd-expiry-time, passwd-expiry-warn-time, passwd-min-uppercase-chars}}

   vserver                role     passwd-minlength passwd-alphanum passwd-min-special-chars passwd-expiry-time passwd-min-lowercase-chars passwd-min-uppercase-chars passwd-min-digits passwd-expiry-warn-time
   ---------------------- -------- ---------------- --------------- ------------------------ ------------------ -------------------------- -------------------------- ----------------- -----------------------
   FsxId0123456           fsxadmin 3                enabled         0                        unlimited          0                          0                          0                 unlimited
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
