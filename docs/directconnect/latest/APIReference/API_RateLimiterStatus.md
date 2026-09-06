---
source_url: https://docs.aws.amazon.com/directconnect/latest/APIReference/API_RateLimiterStatus.html
---

# RateLimiterStatus
<a name="API_RateLimiterStatus"></a>

Contains information about the rate limiter status for a connection, including the maximum number of rate limiters allowed, the number currently in use, and the remaining capacity.

## Contents
<a name="API_RateLimiterStatus_Contents"></a>

 ** inUse **   <a name="DX-Type-RateLimiterStatus-inUse"></a>
The number of rate limiters currently in use on the connection.
Type: Integer
Required: No

 ** maxAllowed **   <a name="DX-Type-RateLimiterStatus-maxAllowed"></a>
The maximum number of rate limiters allowed on the connection.
Type: Integer
Required: No

 ** remaining **   <a name="DX-Type-RateLimiterStatus-remaining"></a>
The number of rate limiters remaining (available) on the connection.
Type: Integer
Required: No

 ** totalBandwidth **   <a name="DX-Type-RateLimiterStatus-totalBandwidth"></a>
The total bandwidth allocated across all rate limiters on the connection.
Type: String
Required: No

## See Also
<a name="API_RateLimiterStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/directconnect-2012-10-25/RateLimiterStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/directconnect-2012-10-25/RateLimiterStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/directconnect-2012-10-25/RateLimiterStatus)
