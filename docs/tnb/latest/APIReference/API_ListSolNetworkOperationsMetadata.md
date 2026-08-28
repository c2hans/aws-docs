---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ListSolNetworkOperationsMetadata.html
---

# ListSolNetworkOperationsMetadata
<a name="API_ListSolNetworkOperationsMetadata"></a>

Metadata related to a network operation.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

## Contents
<a name="API_ListSolNetworkOperationsMetadata_Contents"></a>

 ** createdAt **   <a name="TNB-Type-ListSolNetworkOperationsMetadata-createdAt"></a>
The date that the resource was created.
Type: Timestamp
Required: Yes

 ** lastModified **   <a name="TNB-Type-ListSolNetworkOperationsMetadata-lastModified"></a>
The date that the resource was last modified.
Type: Timestamp
Required: Yes

 ** nsdInfoId **   <a name="TNB-Type-ListSolNetworkOperationsMetadata-nsdInfoId"></a>
The network service descriptor id used for the operation.
Only present if the updateType is `UPDATE_NS`.
Type: String
Pattern: `np-[a-f0-9]{17}`
Required: No

 ** vnfInstanceId **   <a name="TNB-Type-ListSolNetworkOperationsMetadata-vnfInstanceId"></a>
The network function id used for the operation.
Only present if the updateType is `MODIFY_VNF_INFO`.
Type: String
Pattern: `fi-[a-f0-9]{17}`
Required: No

## See Also
<a name="API_ListSolNetworkOperationsMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ListSolNetworkOperationsMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ListSolNetworkOperationsMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ListSolNetworkOperationsMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
