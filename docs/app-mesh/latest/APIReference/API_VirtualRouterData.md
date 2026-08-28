---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualRouterData.html
---

# VirtualRouterData
<a name="API_VirtualRouterData"></a>

An object that represents a virtual router returned by a describe operation.

## Contents
<a name="API_VirtualRouterData_Contents"></a>

 ** meshName **   <a name="appmesh-Type-VirtualRouterData-meshName"></a>
The name of the service mesh that the virtual router resides in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** metadata **   <a name="appmesh-Type-VirtualRouterData-metadata"></a>
The associated metadata for the virtual router.
Type: [ResourceMetadata](API_ResourceMetadata.md) object
Required: Yes

 ** spec **   <a name="appmesh-Type-VirtualRouterData-spec"></a>
The specifications of the virtual router.
Type: [VirtualRouterSpec](API_VirtualRouterSpec.md) object
Required: Yes

 ** status **   <a name="appmesh-Type-VirtualRouterData-status"></a>
The current status of the virtual router.
Type: [VirtualRouterStatus](API_VirtualRouterStatus.md) object
Required: Yes

 ** virtualRouterName **   <a name="appmesh-Type-VirtualRouterData-virtualRouterName"></a>
The name of the virtual router.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_VirtualRouterData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualRouterData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualRouterData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualRouterData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
