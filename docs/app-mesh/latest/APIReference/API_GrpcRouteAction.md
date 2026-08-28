---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_GrpcRouteAction.html
---

# GrpcRouteAction
<a name="API_GrpcRouteAction"></a>

An object that represents the action to take if a match is determined.

## Contents
<a name="API_GrpcRouteAction_Contents"></a>

 ** weightedTargets **   <a name="appmesh-Type-GrpcRouteAction-weightedTargets"></a>
An object that represents the targets that traffic is routed to when a request matches the route.
Type: Array of [WeightedTarget](API_WeightedTarget.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

## See Also
<a name="API_GrpcRouteAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcRouteAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcRouteAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcRouteAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
