---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_GrpcRoute.html
---

# GrpcRoute
<a name="API_GrpcRoute"></a>

An object that represents a gRPC route type.

## Contents
<a name="API_GrpcRoute_Contents"></a>

 ** action **   <a name="appmesh-Type-GrpcRoute-action"></a>
An object that represents the action to take if a match is determined.
Type: [GrpcRouteAction](API_GrpcRouteAction.md) object
Required: Yes

 ** match **   <a name="appmesh-Type-GrpcRoute-match"></a>
An object that represents the criteria for determining a request match.
Type: [GrpcRouteMatch](API_GrpcRouteMatch.md) object
Required: Yes

 ** retryPolicy **   <a name="appmesh-Type-GrpcRoute-retryPolicy"></a>
An object that represents a retry policy.
Type: [GrpcRetryPolicy](API_GrpcRetryPolicy.md) object
Required: No

 ** timeout **   <a name="appmesh-Type-GrpcRoute-timeout"></a>
An object that represents types of timeouts.
Type: [GrpcTimeout](API_GrpcTimeout.md) object
Required: No

## See Also
<a name="API_GrpcRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
