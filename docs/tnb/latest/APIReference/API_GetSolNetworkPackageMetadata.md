---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolNetworkPackageMetadata.html
---

# GetSolNetworkPackageMetadata
<a name="API_GetSolNetworkPackageMetadata"></a>

Metadata associated with a network package.

A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the AWS infrastructure you want to deploy them on.

## Contents
<a name="API_GetSolNetworkPackageMetadata_Contents"></a>

 ** createdAt **   <a name="TNB-Type-GetSolNetworkPackageMetadata-createdAt"></a>
The date that the resource was created.
Type: Timestamp
Required: Yes

 ** lastModified **   <a name="TNB-Type-GetSolNetworkPackageMetadata-lastModified"></a>
The date that the resource was last modified.
Type: Timestamp
Required: Yes

 ** nsd **   <a name="TNB-Type-GetSolNetworkPackageMetadata-nsd"></a>
Metadata related to the onboarded network service descriptor in the network package.
Type: [NetworkArtifactMeta](API_NetworkArtifactMeta.md) object
Required: No

## See Also
<a name="API_GetSolNetworkPackageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolNetworkPackageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolNetworkPackageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolNetworkPackageMetadata)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Telco Network Builder. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tnb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
