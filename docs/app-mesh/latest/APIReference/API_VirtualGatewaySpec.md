---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_VirtualGatewaySpec.html
---

# VirtualGatewaySpec
<a name="API_VirtualGatewaySpec"></a>

An object that represents the specification of a service mesh resource.

## Contents
<a name="API_VirtualGatewaySpec_Contents"></a>

 ** listeners **   <a name="appmesh-Type-VirtualGatewaySpec-listeners"></a>
The listeners that the mesh endpoint is expected to receive inbound traffic from. You can specify one listener.
Type: Array of [VirtualGatewayListener](API_VirtualGatewayListener.md) objects
Required: Yes

 ** backendDefaults **   <a name="appmesh-Type-VirtualGatewaySpec-backendDefaults"></a>
A reference to an object that represents the defaults for backends.
Type: [VirtualGatewayBackendDefaults](API_VirtualGatewayBackendDefaults.md) object
Required: No

 ** logging **   <a name="appmesh-Type-VirtualGatewaySpec-logging"></a>
An object that represents logging information.
Type: [VirtualGatewayLogging](API_VirtualGatewayLogging.md) object
Required: No

## See Also
<a name="API_VirtualGatewaySpec_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/VirtualGatewaySpec)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/VirtualGatewaySpec)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/VirtualGatewaySpec)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
