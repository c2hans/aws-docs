---
source_url: https://docs.aws.amazon.com/efs/latest/APIReference/API_PosixUser.html
---

# PosixUser
<a name="API_PosixUser"></a>

The full POSIX identity, including the user ID, group ID, and any secondary group IDs, on the access point that is used for all file system operations performed by NFS clients using the access point.

## Contents
<a name="API_PosixUser_Contents"></a>

 ** Gid **   <a name="efs-Type-PosixUser-Gid"></a>
The POSIX group ID used for all file system operations using this access point.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** Uid **   <a name="efs-Type-PosixUser-Uid"></a>
The POSIX user ID used for all file system operations using this access point.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: Yes

 ** SecondaryGids **   <a name="efs-Type-PosixUser-SecondaryGids"></a>
Secondary POSIX group IDs used for all file system operations using this access point.
Type: Array of longs
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_PosixUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticfilesystem-2015-02-01/PosixUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PosixUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PosixUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic File System (EFS). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query efs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
