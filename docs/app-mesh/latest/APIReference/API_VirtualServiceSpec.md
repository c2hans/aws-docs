---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualServiceSpec.html
---

# VirtualServiceSpec
<a name="API_VirtualServiceSpec"></a>

An object that represents the specification of a virtual service.

## Contents
<a name="API_VirtualServiceSpec_Contents"></a>

 ** provider **   <a name="appmesh-Type-VirtualServiceSpec-provider"></a>
The App Mesh object that is acting as the provider for a virtual service. You can specify a single virtual node or virtual router.
Type: [VirtualServiceProvider](API_VirtualServiceProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_VirtualServiceSpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualServiceSpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualServiceSpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualServiceSpec)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
