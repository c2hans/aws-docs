---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_SmbMountOptions.html
---

# SmbMountOptions
<a name="API_SmbMountOptions"></a>

Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.

## Contents
<a name="API_SmbMountOptions_Contents"></a>

 ** Version **   <a name="DataSync-Type-SmbMountOptions-Version"></a>
By default, DataSync automatically chooses an SMB protocol version based on negotiation with your SMB file server. You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically.
These are the following options for configuring the SMB version:
+  `AUTOMATIC` (default): DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1.

  This is the recommended option. If you instead choose a specific version that your file server doesn't support, you may get an `Operation Not Supported` error.
+  `SMB3`: Restricts the protocol negotiation to only SMB version 3.0.2.
+  `SMB2`: Restricts the protocol negotiation to only SMB version 2.1.
+  `SMB2_0`: Restricts the protocol negotiation to only SMB version 2.0.
+  `SMB1`: Restricts the protocol negotiation to only SMB version 1.0.
**Note**
The `SMB1` option isn't available when [creating an Amazon FSx for NetApp ONTAP location](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html).
Type: String
Valid Values: `AUTOMATIC | SMB2 | SMB3 | SMB1 | SMB2_0`
Required: No

## See Also
<a name="API_SmbMountOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/SmbMountOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/SmbMountOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/SmbMountOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
