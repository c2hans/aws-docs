---
source_url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/API_HttpRetryPolicy.html
---

# HttpRetryPolicy
<a name="API_HttpRetryPolicy"></a>

An object that represents a retry policy. Specify at least one value for at least one of the types of `RetryEvents`, a value for `maxRetries`, and a value for `perRetryTimeout`. Both `server-error` and `gateway-error` under `httpRetryEvents` include the Envoy `reset` policy. For more information on the `reset` policy, see the [Envoy documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/router_filter#x-envoy-retry-on).

## Contents
<a name="API_HttpRetryPolicy_Contents"></a>

 ** maxRetries **   <a name="appmesh-Type-HttpRetryPolicy-maxRetries"></a>
The maximum number of retry attempts.
Type: Long
Valid Range: Minimum value of 0.
Required: Yes

 ** perRetryTimeout **   <a name="appmesh-Type-HttpRetryPolicy-perRetryTimeout"></a>
The timeout for each retry attempt.
Type: [Duration](API_Duration.md) object
Required: Yes

 ** httpRetryEvents **   <a name="appmesh-Type-HttpRetryPolicy-httpRetryEvents"></a>
Specify at least one of the following values.
+  **server-error** – HTTP status codes 500, 501, 502, 503, 504, 505, 506, 507, 508, 510, and 511
+  **gateway-error** – HTTP status codes 502, 503, and 504
+  **client-error** – HTTP status code 409
+  **stream-error** – Retry on refused stream
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 25.
Required: No

 ** tcpRetryEvents **   <a name="appmesh-Type-HttpRetryPolicy-tcpRetryEvents"></a>
Specify a valid value. The event occurs before any processing of a request has started and is encountered when the upstream is temporarily or permanently unavailable.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `connection-error`
Required: No

## See Also
<a name="API_HttpRetryPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appmesh-2019-01-25/HttpRetryPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appmesh-2019-01-25/HttpRetryPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appmesh-2019-01-25/HttpRetryPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Mesh. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query app-mesh` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
