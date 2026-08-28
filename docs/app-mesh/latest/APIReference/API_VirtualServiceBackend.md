---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualServiceBackend.html
---

# VirtualServiceBackend
<a name="API_VirtualServiceBackend"></a>

An object that represents a virtual service backend for a virtual node.

## Contents
<a name="API_VirtualServiceBackend_Contents"></a>

 ** virtualServiceName **   <a name="appmesh-Type-VirtualServiceBackend-virtualServiceName"></a>
The name of the virtual service that is acting as a virtual node backend.
App Mesh doesn't validate the existence of those virtual services specified in backends. This is to prevent a cyclic dependency between virtual nodes and virtual services creation. Make sure the virtual service name is correct. The virtual service can be created afterwards if it doesn't already exist.
Type: String
Required: Yes

 ** clientPolicy **   <a name="appmesh-Type-VirtualServiceBackend-clientPolicy"></a>
A reference to an object that represents the client policy for a backend.
Type: [ClientPolicy](API_ClientPolicy.md) object
Required: No

## See Also
<a name="API_VirtualServiceBackend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualServiceBackend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualServiceBackend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualServiceBackend)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
