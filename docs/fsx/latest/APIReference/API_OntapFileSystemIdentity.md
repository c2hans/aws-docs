---
source_url: https://docs.aws.amazon.com/fsx/latest/APIReference/API_OntapFileSystemIdentity.html
---

# OntapFileSystemIdentity
<a name="API_OntapFileSystemIdentity"></a>

Specifies the file system user identity that will be used for authorizing all file access requests that are made using the S3 access point. The identity can be either a UNIX user or a Windows user.

## Contents
<a name="API_OntapFileSystemIdentity_Contents"></a>

 ** Type **   <a name="FSx-Type-OntapFileSystemIdentity-Type"></a>
Specifies the FSx for ONTAP user identity type. Valid values are `UNIX` and `WINDOWS`.
Type: String
Valid Values: `UNIX | WINDOWS`
Required: Yes

 ** UnixUser **   <a name="FSx-Type-OntapFileSystemIdentity-UnixUser"></a>
Specifies the UNIX user identity for file system operations.
Type: [OntapUnixFileSystemUser](API_OntapUnixFileSystemUser.md) object
Required: No

 ** WindowsUser **   <a name="FSx-Type-OntapFileSystemIdentity-WindowsUser"></a>
Specifies the Windows user identity for file system operations.
Type: [OntapWindowsFileSystemUser](API_OntapWindowsFileSystemUser.md) object
Required: No

## See Also
<a name="API_OntapFileSystemIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fsx-2018-03-01/OntapFileSystemIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fsx-2018-03-01/OntapFileSystemIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fsx-2018-03-01/OntapFileSystemIdentity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FSx. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fsx` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
