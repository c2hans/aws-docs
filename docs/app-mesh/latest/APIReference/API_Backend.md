---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_Backend.html
---

# Backend
<a name="API_Backend"></a>

An object that represents the backends that a virtual node is expected to send outbound traffic to.

## Contents
<a name="API_Backend_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** virtualService **   <a name="appmesh-Type-Backend-virtualService"></a>
Specifies a virtual service to use as a backend.
Type: [VirtualServiceBackend](API_VirtualServiceBackend.md) object
Required: No

## See Also
<a name="API_Backend_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/Backend)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/Backend)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/Backend)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
