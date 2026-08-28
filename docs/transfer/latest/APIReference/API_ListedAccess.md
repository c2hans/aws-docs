---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_ListedAccess.html
---

# ListedAccess
<a name="API_ListedAccess"></a>

Lists the properties for one or more specified associated accesses.

## Contents
<a name="API_ListedAccess_Contents"></a>

 ** ExternalId **   <a name="TransferFamily-Type-ListedAccess-ExternalId"></a>
A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using AWS Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.
 `Get-ADGroup -Filter {samAccountName -like "YourGroupName*"} -Properties * | Select SamAccountName,ObjectSid`
In that command, replace *YourGroupName* with the name of your Active Directory group.
The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `S-1-[\d-]+`
Required: No

 ** HomeDirectory **   <a name="TransferFamily-Type-ListedAccess-HomeDirectory"></a>
The landing directory (folder) for a user when they log in to the server using the client.
A `HomeDirectory` example is `/bucket_name/home/mydirectory`.
You can use the `HomeDirectory` parameter for `HomeDirectoryType` when it is set to either `PATH` or `LOGICAL`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(|/.*)`
Required: No

 ** HomeDirectoryType **   <a name="TransferFamily-Type-ListedAccess-HomeDirectoryType"></a>
The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to `PATH`, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to `LOGICAL`, you need to provide mappings in the `HomeDirectoryMappings` for how you want to make Amazon S3 or Amazon EFS paths visible to your users.
If `HomeDirectoryType` is `LOGICAL`, you must provide mappings, using the `HomeDirectoryMappings` parameter. If, on the other hand, `HomeDirectoryType` is `PATH`, you provide an absolute path using the `HomeDirectory` parameter. You cannot have both `HomeDirectory` and `HomeDirectoryMappings` in your template.
Type: String
Valid Values: `PATH | LOGICAL`
Required: No

 ** Role **   <a name="TransferFamily-Type-ListedAccess-Role"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

## See Also
<a name="API_ListedAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/ListedAccess)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/ListedAccess)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/ListedAccess)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
