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
+  `AUTOMATIC` (default): DataSync chooses NFS version 4.1.
+  `NFS3`: Stateless protocol version that allows for asynchronous writes on the server.
+  `NFSv4_0`: Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems.
+  `NFSv4_1`: Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0.
DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.
Type: String
Valid Values: `AUTOMATIC | NFS3 | NFS4_0 | NFS4_1`
Required: No

## See Also
<a name="API_NfsMountOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/NfsMountOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/NfsMountOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/NfsMountOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
