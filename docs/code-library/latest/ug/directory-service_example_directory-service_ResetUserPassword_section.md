---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/directory-service_example_directory-service_ResetUserPassword_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ResetUserPassword` with a CLI
<a name="directory-service_example_directory-service_ResetUserPassword_section"></a>

The following code examples show how to use `ResetUserPassword`.

------
#### [ CLI ]

**AWS CLI**
**To reset a user password in a directory**
The following `reset-user-password` example resets and enables the specified user in the specified directory.

```
aws ds reset-user-password \
    --directory-id {{d-1234567890}} \
    --user-name '{{john.doe}}' \
    --new-{{password}} 'password'
```
This command produces no output.
For more information, see [Resetting and enabling an AWS Managed Microsoft AD user's password](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_reset_user_pswd.html) in the *AWS Directory Service Administration Guide*.
+  For API details, see [ResetUserPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/reset-user-password.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example resets the password of Active Direcotry user named ADUser in AWS Managed microsoft AD or Simple AD Directory**

```
Reset-DSUserPassword -UserName ADuser -DirectoryId d-123456ijkl -NewPassword $Password
```
+  For API details, see [ResetUserPassword](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example resets the password of Active Direcotry user named ADUser in AWS Managed microsoft AD or Simple AD Directory**

```
Reset-DSUserPassword -UserName ADuser -DirectoryId d-123456ijkl -NewPassword $Password
```
+  For API details, see [ResetUserPassword](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
