---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedUser.html
---

# DescribedUser
<a name="API_DescribedUser"></a>

Describes the properties of a user that was specified.

## Contents
<a name="API_DescribedUser_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-DescribedUser-Arn"></a>
Specifies the unique Amazon Resource Name (ARN) for the user that was requested to be described.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** HomeDirectory **   <a name="TransferFamily-Type-DescribedUser-HomeDirectory"></a>
The landing directory (folder) for a user when they log in to the server using the client.
A `HomeDirectory` example is `/bucket_name/home/mydirectory`.
You can use the `HomeDirectory` parameter for `HomeDirectoryType` when it is set to either `PATH` or `LOGICAL`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: No

 ** HomeDirectoryMappings **   <a name="TransferFamily-Type-DescribedUser-HomeDirectoryMappings"></a>
Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the `Entry` and `Target` pair, where `Entry` shows how the path is made visible and `Target` is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your AWS Identity and Access Management (IAM) role provides access to paths in `Target`. This value can be set only when `HomeDirectoryType` is set to *LOGICAL*.
In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory ("`chroot`"). To do this, you can set `Entry` to '/' and set `Target` to the HomeDirectory parameter value.
Type: Array of [HomeDirectoryMapEntry](API_HomeDirectoryMapEntry.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50000 items.
Required: No

 ** HomeDirectoryType **   <a name="TransferFamily-Type-DescribedUser-HomeDirectoryType"></a>
The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to `PATH`, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to `LOGICAL`, you need to provide mappings in the `HomeDirectoryMappings` for how you want to make Amazon S3 or Amazon EFS paths visible to your users.
If `HomeDirectoryType` is `LOGICAL`, you must provide mappings, using the `HomeDirectoryMappings` parameter. If, on the other hand, `HomeDirectoryType` is `PATH`, you provide an absolute path using the `HomeDirectory` parameter. You cannot have both `HomeDirectory` and `HomeDirectoryMappings` in your template.
Type: String
Valid Values: `PATH | LOGICAL`
Required: No

 ** Policy **   <a name="TransferFamily-Type-DescribedUser-Policy"></a>
A session policy for your user so that you can use the same AWS Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include `${Transfer:UserName}`, `${Transfer:HomeDirectory}`, and `${Transfer:HomeBucket}`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** PosixProfile **   <a name="TransferFamily-Type-DescribedUser-PosixProfile"></a>
Specifies the full POSIX identity, including user ID (`Uid`), group ID (`Gid`), and any secondary groups IDs (`SecondaryGids`), that controls your users' access to your Amazon Elastic File System (Amazon EFS) file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.
Type: [PosixProfile](API_PosixProfile.md) object
Required: No

 ** Role **   <a name="TransferFamily-Type-DescribedUser-Role"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

 ** SshPublicKeys **   <a name="TransferFamily-Type-DescribedUser-SshPublicKeys"></a>
Specifies the public key portion of the Secure Shell (SSH) keys stored for the described user.
To delete the public key body, set its value to zero keys, as shown here:
 `SshPublicKeys: []`
Type: Array of [SshPublicKey](API_SshPublicKey.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** Tags **   <a name="TransferFamily-Type-DescribedUser-Tags"></a>
Specifies the key-value pairs for the user requested. Tag can be used to search for and group users for a variety of purposes.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** UserName **   <a name="TransferFamily-Type-DescribedUser-UserName"></a>
Specifies the name of the user that was requested to be described. User names are used for authentication purposes. This is the string that will be used by your user when they log in to your server.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 100.
Pattern: `[\w][\w@.-]{2,99}`
Required: No

## See Also
<a name="API_DescribedUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
