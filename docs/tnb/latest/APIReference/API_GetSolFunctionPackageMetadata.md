---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_GetSolFunctionPackageMetadata.html
---

# GetSolFunctionPackageMetadata
<a name="API_GetSolFunctionPackageMetadata"></a>

Metadata related to the function package.

A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.

## Contents
<a name="API_GetSolFunctionPackageMetadata_Contents"></a>

 ** createdAt **   <a name="TNB-Type-GetSolFunctionPackageMetadata-createdAt"></a>
The date that the resource was created.
Type: Timestamp
Required: Yes

 ** lastModified **   <a name="TNB-Type-GetSolFunctionPackageMetadata-lastModified"></a>
The date that the resource was last modified.
Type: Timestamp
Required: Yes

 ** vnfd **   <a name="TNB-Type-GetSolFunctionPackageMetadata-vnfd"></a>
Metadata related to the function package descriptor of the function package.
Type: [FunctionArtifactMeta](API_FunctionArtifactMeta.md) object
Required: No

## See Also
<a name="API_GetSolFunctionPackageMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/GetSolFunctionPackageMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/GetSolFunctionPackageMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/GetSolFunctionPackageMetadata)
