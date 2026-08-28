---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualServiceData.html
---

# VirtualServiceData
<a name="API_VirtualServiceData"></a>

An object that represents a virtual service returned by a describe operation.

## Contents
<a name="API_VirtualServiceData_Contents"></a>

 ** meshName **   <a name="appmesh-Type-VirtualServiceData-meshName"></a>
The name of the service mesh that the virtual service resides in.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** metadata **   <a name="appmesh-Type-VirtualServiceData-metadata"></a>
An object that represents metadata for a resource.
Type: [ResourceMetadata](API_ResourceMetadata.md) object
Required: Yes

 ** spec **   <a name="appmesh-Type-VirtualServiceData-spec"></a>
The specifications of the virtual service.
Type: [VirtualServiceSpec](API_VirtualServiceSpec.md) object
Required: Yes

 ** status **   <a name="appmesh-Type-VirtualServiceData-status"></a>
The current status of the virtual service.
Type: [VirtualServiceStatus](API_VirtualServiceStatus.md) object
Required: Yes

 ** virtualServiceName **   <a name="appmesh-Type-VirtualServiceData-virtualServiceName"></a>
The name of the virtual service.
Type: String
Required: Yes

## See Also
<a name="API_VirtualServiceData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualServiceData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualServiceData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualServiceData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
