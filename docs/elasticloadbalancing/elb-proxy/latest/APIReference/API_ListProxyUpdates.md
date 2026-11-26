---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/elb-proxy/latest/APIReference/API_ListProxyUpdates.html
---

# ListProxyUpdates

Lists the updates for the specified proxy, most recently submitted first.

## Request Parameters
<a name="API_ListProxyUpdates_RequestParameters"></a>

 ** maxResults **
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** nextToken **
A pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** proxyIdentifier **
The Amazon Resource Name (ARN) of the proxy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+:elasticloadbalancing:[a-z0-9-]+:[0-9]{12}:proxy/[a-zA-Z0-9-]+:[a-zA-Z0-9]+`
Required: Yes

## Response Elements
<a name="API_ListProxyUpdates_ResponseElements"></a>

The following elements are returned by the service.

 ** items **
Information about the updates for the proxy.
Type: Array of [ProxyUpdateSummary](API_ProxyUpdateSummary.md) objects

 ** nextToken **
If there are additional results, a pagination token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListProxyUpdates_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
 ** message **
The error message.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred while processing the request.
 ** message **
The error message.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** message **
The error message.
HTTP Status Code: 404

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** message **
The error message.
HTTP Status Code: 429

 ** ValidationError **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListProxyUpdates_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elb-proxy-2026-11-20/ListProxyUpdates)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elb-proxy-2026-11-20/ListProxyUpdates)
