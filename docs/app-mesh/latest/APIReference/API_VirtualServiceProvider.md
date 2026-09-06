---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualServiceProvider.html
---

# VirtualServiceProvider
<a name="API_VirtualServiceProvider"></a>

An object that represents the provider for a virtual service.

## Contents
<a name="API_VirtualServiceProvider_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** virtualNode **   <a name="appmesh-Type-VirtualServiceProvider-virtualNode"></a>
The virtual node associated with a virtual service.
Type: [VirtualNodeServiceProvider](API_VirtualNodeServiceProvider.md) object
Required: No

 ** virtualRouter **   <a name="appmesh-Type-VirtualServiceProvider-virtualRouter"></a>
The virtual router associated with a virtual service.
Type: [VirtualRouterServiceProvider](API_VirtualRouterServiceProvider.md) object
Required: No

## See Also
<a name="API_VirtualServiceProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualServiceProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualServiceProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualServiceProvider)
