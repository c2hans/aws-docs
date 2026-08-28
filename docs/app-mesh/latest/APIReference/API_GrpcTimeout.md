---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_GrpcTimeout.html
---

# GrpcTimeout
<a name="API_GrpcTimeout"></a>

An object that represents types of timeouts.

## Contents
<a name="API_GrpcTimeout_Contents"></a>

 ** idle **   <a name="appmesh-Type-GrpcTimeout-idle"></a>
An object that represents an idle timeout. An idle timeout bounds the amount of time that a connection may be idle. The default value is none.
Type: [Duration](API_Duration.md) object
Required: No

 ** perRequest **   <a name="appmesh-Type-GrpcTimeout-perRequest"></a>
An object that represents a per request timeout. The default value is 15 seconds. If you set a higher timeout, then make sure that the higher value is set for each App Mesh resource in a conversation. For example, if a virtual node backend uses a virtual router provider to route to another virtual node, then the timeout should be greater than 15 seconds for the source and destination virtual node and the route.
Type: [Duration](API_Duration.md) object
Required: No

## See Also
<a name="API_GrpcTimeout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcTimeout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcTimeout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcTimeout)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
