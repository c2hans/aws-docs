---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ApplicationStatusReason.html
---

# ApplicationStatusReason
<a name="API_ApplicationStatusReason"></a>

Describes the reason for an application status check result.

## Contents
<a name="API_ApplicationStatusReason_Contents"></a>

 ** code **
The reason code for the application status check result. Possible values:
+  `ResponseCodeMatched` – The HTTP status code returned by the health check matched the configured `StatusCodeMatcher`.
+  `ResponseCodeMismatch` – The HTTP status code returned by the health check did not match the configured `StatusCodeMatcher`.
+  `ConnectionTimeout` – The connection to the target timed out.
+  `ResponseTimeout` – The health check timed out while waiting for a response from the target.
+  `ConnectionRefused` – The target refused the health check connection.
+  `ConnectionReset` – The target reset the health check connection before returning a response.
Current health check results use the values in the preceding list. Legacy results that do not contain structured reason metadata can instead contain a producer error type, such as `Http Status Code` or `HttpConnectTimeoutException`.
For `ResponseCodeMatched` and `ResponseCodeMismatch`, the `statusCode` field contains the returned HTTP status code. The `protocol` field contains the protocol used for the health check.
Type: String
Required: No

 ** protocol **
The protocol used for the health check. Possible values: `HTTP` and `HTTPS`.
Type: String
Required: No

 ** statusCode **
The HTTP status code returned by the health check.
Type: Integer
Required: No

## See Also
<a name="API_ApplicationStatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ApplicationStatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ApplicationStatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ApplicationStatusReason)
