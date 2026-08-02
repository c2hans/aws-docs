---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.troubleshooting.html
---

# Troubleshooting Amazon EFS integration
<a name="oracle-efs-integration.troubleshooting"></a>

Your RDS for Oracle DB instance monitors the connectivity to an Amazon EFS file system. When monitoring detects an issue, it might try to correct the issue and publish an event in the RDS console. For more information, see [Viewing Amazon RDS events](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ListEvents.html).

Use the information in this section to help you diagnose and fix common issues when you work with Amazon EFS integration.

| Notification | Description | Action |
| --- | --- | --- |
| `The EFS for RDS Oracle instance {{instance_name}} isn't available on the primary host. NFS port 2049 of your EFS isn't reachable.` | The DB instance can't communicate with the EFS file system. | Make sure of the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.troubleshooting.html) |
| `The EFS isn't reachable.` | An error occurred during the installation of the `EFS_INTEGRATION` option. | Make sure of the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.troubleshooting.html) |
| `The associated role with your DB instance wasn't found.` | An error occurred during the installation of the `EFS_INTEGRATION` option. | Make sure that you associated an IAM role with your RDS for Oracle DB instance. |
| `The associated role with your DB instance wasn't found.` | An error occurred during the installation of the `EFS_INTEGRATION` option. RDS for Oracle was restored from a DB snapshot with the `USE_IAM_ROLE` option setting of `TRUE`. | Make sure that you associated an IAM role with your RDS for Oracle DB instance. |
| `The associated role with your DB instance wasn't found.` | An error occurred during the installation of the `EFS_INTEGRATION` option. RDS for Oracle was created from an all-in-one CloudFormation template with the `USE_IAM_ROLE` option setting of `TRUE`. | As a workaround, complete the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.troubleshooting.html) |
| `PLS-00302: component 'CREATE_DIRECTORY_EFS' must be declared` | This error can occur when you're using a version of RDS for Oracle that doesn't support Amazon EFS. | Make sure that you are using RDS for Oracle DB instance version 19.0.0.0.ru-2022-07.rur-2022-07.r1 or higher. |
| `Read access of your EFS is denied. Check your file system policy.` | Your DB instance can't read the EFS file system. | Make sure that your EFS file system allows read access through the IAM role or on the EFS file system level.  |
| N/A | Your DB instance can't write to the EFS file system. | Take the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/oracle-efs-integration.troubleshooting.html) |
