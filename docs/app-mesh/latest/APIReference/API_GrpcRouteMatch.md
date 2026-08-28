---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_GrpcRouteMatch.html
---

# GrpcRouteMatch
<a name="API_GrpcRouteMatch"></a>

An object that represents the criteria for determining a request match.

## Contents
<a name="API_GrpcRouteMatch_Contents"></a>

 ** metadata **   <a name="appmesh-Type-GrpcRouteMatch-metadata"></a>
An object that represents the data to match from the request.
Type: Array of [GrpcRouteMetadata](API_GrpcRouteMetadata.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** methodName **   <a name="appmesh-Type-GrpcRouteMatch-methodName"></a>
The method name to match from the request. If you specify a name, you must also specify a `serviceName`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Required: No

 ** port **   <a name="appmesh-Type-GrpcRouteMatch-port"></a>
The port number to match on.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** serviceName **   <a name="appmesh-Type-GrpcRouteMatch-serviceName"></a>
The fully qualified domain name for the service to match from the request.
Type: String
Required: No

## See Also
<a name="API_GrpcRouteMatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/GrpcRouteMatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/GrpcRouteMatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/GrpcRouteMatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
