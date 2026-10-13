---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_NfsMountOptions.html
---

# NfsMountOptions
<a name="API_NfsMountOptions"></a>

Specifies how DataSync can access a location using the NFS protocol.

## Contents
<a name="API_NfsMountOptions_Contents"></a>

 ** Version **   <a name="DataSync-Type-NfsMountOptions-Version"></a>
Specifies the NFS version that you want DataSync to use when mounting your NFS share. If the server refuses to use the version specified, the task fails.
You can specify the following options:
+  `AUTOMATIC` (default): DataSync chooses NFS version 4.1. For Amazon FSx for OpenZFS locations, DataSync first attempts to use NFS version 4.2, then falls back to version 4.1, and then to earlier versions if needed.
+  `NFS3`: Stateless protocol version that allows for asynchronous writes on the server.
+  `NFSv4_0`: Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems.
+  `NFSv4_1`: Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0.
+  `NFSv4_2`: Stateful protocol version that supports sparse file operations, space reservation, and server-side copy operations, in addition to all features available in version 4.1. Selecting NFS version 4.2 requires an Enhanced mode task.
DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.
Type: String
Valid Values: `AUTOMATIC | NFS3 | NFS4_0 | NFS4_1 | NFS4_2`
Required: No

## See Also
<a name="API_NfsMountOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/NfsMountOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/NfsMountOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/NfsMountOptions)
