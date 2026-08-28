---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_FsxUpdateProtocolSmb.html
---

# FsxUpdateProtocolSmb
<a name="API_FsxUpdateProtocolSmb"></a>

Specifies the Server Message Block (SMB) protocol configuration that AWS DataSync uses to access your Amazon FSx for NetApp ONTAP file system's storage virtual machine (SVM). For more information, see [Providing DataSync access to FSx for ONTAP file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access).

## Contents
<a name="API_FsxUpdateProtocolSmb_Contents"></a>

 ** CmkSecretConfig **   <a name="DataSync-Type-FsxUpdateProtocolSmb-CmkSecretConfig"></a>
Specifies configuration information for a DataSync-managed secret, such as a `Password` or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed AWS KMS key.
Type: [CmkSecretConfig](API_CmkSecretConfig.md) object
Required: No

 ** CustomSecretConfig **   <a name="DataSync-Type-FsxUpdateProtocolSmb-CustomSecretConfig"></a>
Specifies configuration information for a customer-managed secret, such as a `Password` or set of credentials that DataSync uses to access a specific transfer location. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.
Type: [CustomSecretConfig](API_CustomSecretConfig.md) object
Required: No

 ** Domain **   <a name="DataSync-Type-FsxUpdateProtocolSmb-Domain"></a>
Specifies the name of the Windows domain that your storage virtual machine (SVM) belongs to.
If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right SVM.
Type: String
Length Constraints: Maximum length of 253.
Pattern: `^([A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252})?$`
Required: No

 ** MountOptions **   <a name="DataSync-Type-FsxUpdateProtocolSmb-MountOptions"></a>
Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.
Type: [SmbMountOptions](API_SmbMountOptions.md) object
Required: No

 ** Password **   <a name="DataSync-Type-FsxUpdateProtocolSmb-Password"></a>
Specifies the password of a user who has permission to access your SVM.
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^.{0,104}$`
Required: No

 ** User **   <a name="DataSync-Type-FsxUpdateProtocolSmb-User"></a>
Specifies a user that can mount and access the files, folders, and metadata in your SVM.
For information about choosing a user with the right level of access for your transfer, see [Using the SMB protocol](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-smb).
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`
Required: No

## See Also
<a name="API_FsxUpdateProtocolSmb_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/FsxUpdateProtocolSmb)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/FsxUpdateProtocolSmb)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/FsxUpdateProtocolSmb)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
