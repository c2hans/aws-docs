---
source_url: https://docs.aws.amazon.com/tnb/latest/APIReference/API_ModifyVnfInfoMetadata.html
---

# ModifyVnfInfoMetadata
<a name="API_ModifyVnfInfoMetadata"></a>

Metadata related to the configuration properties used during update of a specific network function in a network instance.

## Contents
<a name="API_ModifyVnfInfoMetadata_Contents"></a>

 ** vnfConfigurableProperties **   <a name="TNB-Type-ModifyVnfInfoMetadata-vnfConfigurableProperties"></a>
The configurable properties used during update of the network function instance.
Type: JSON value
Required: Yes

 ** vnfInstanceId **   <a name="TNB-Type-ModifyVnfInfoMetadata-vnfInstanceId"></a>
The network function instance that was updated in the network instance.
Type: String
Pattern: `fi-[a-f0-9]{17}`
Required: Yes

## See Also
<a name="API_ModifyVnfInfoMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/tnb-2008-10-21/ModifyVnfInfoMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/tnb-2008-10-21/ModifyVnfInfoMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/tnb-2008-10-21/ModifyVnfInfoMetadata)
