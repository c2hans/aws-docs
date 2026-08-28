---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_OpenZFSFileSystemIdentity.html
---

# OpenZFSFileSystemIdentity
<a name="API_OpenZFSFileSystemIdentity"></a>

Specifies the file system user identity that will be used for authorizing all file access requests that are made using the S3 access point.

## Contents
<a name="API_OpenZFSFileSystemIdentity_Contents"></a>

 ** Type **   <a name="FSx-Type-OpenZFSFileSystemIdentity-Type"></a>
Specifies the FSx for OpenZFS user identity type, accepts only `POSIX`.
Type: String
Valid Values: `POSIX`
Required: Yes

 ** PosixUser **   <a name="FSx-Type-OpenZFSFileSystemIdentity-PosixUser"></a>
Specifies the UID and GIDs of the file system POSIX user.
Type: [OpenZFSPosixFileSystemUser](API_OpenZFSPosixFileSystemUser.md) object
Required: No

## See Also
<a name="API_OpenZFSFileSystemIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OpenZFSFileSystemIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OpenZFSFileSystemIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OpenZFSFileSystemIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
