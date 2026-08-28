---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_FsxUpdateProtocol.html
---

# FsxUpdateProtocol
<a name="API_FsxUpdateProtocol"></a>

Specifies the data transfer protocol that AWS DataSync uses to access your Amazon FSx file system.

**Note**
You can't update the Network File System (NFS) protocol configuration for FSx for ONTAP locations. DataSync currently only supports NFS version 3 with this location type.

## Contents
<a name="API_FsxUpdateProtocol_Contents"></a>

 ** NFS **   <a name="DataSync-Type-FsxUpdateProtocol-NFS"></a>
Specifies the Network File System (NFS) protocol configuration that DataSync uses to access your FSx for OpenZFS file system or FSx for ONTAP file system's storage virtual machine (SVM).
Type: [FsxProtocolNfs](API_FsxProtocolNfs.md) object
Required: No

 ** SMB **   <a name="DataSync-Type-FsxUpdateProtocol-SMB"></a>
Specifies the Server Message Block (SMB) protocol configuration that DataSync uses to access your FSx for ONTAP file system's storage virtual machine (SVM).
Type: [FsxUpdateProtocolSmb](API_FsxUpdateProtocolSmb.md) object
Required: No

## See Also
<a name="API_FsxUpdateProtocol_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/FsxUpdateProtocol)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/FsxUpdateProtocol)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/FsxUpdateProtocol)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
