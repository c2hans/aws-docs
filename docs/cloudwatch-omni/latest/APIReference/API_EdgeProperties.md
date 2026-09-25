---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_EdgeProperties.html
---

# EdgeProperties
<a name="API_EdgeProperties"></a>

Edge attributes promoted out of the flat attribute map onto typed members. Which members are present depends entirely on what produced the edge, so most edges carry only a few of them.

## Contents
<a name="API_EdgeProperties_Contents"></a>

 ** blocked **   <a name="cloudwatchomni-Type-EdgeProperties-blocked"></a>
Whether the observed network flow was denied. Absent means the edge was not derived from network flow data, which is not the same as allowed.
Type: Boolean
Required: No

 ** destinationPort **   <a name="cloudwatchomni-Type-EdgeProperties-destinationPort"></a>
The destination port of the observed traffic. May be a placeholder when the port is unknown.
Type: String
Required: No

 ** errorCode **   <a name="cloudwatchomni-Type-EdgeProperties-errorCode"></a>
The error code returned when the call was attempted and refused. Its presence means the edge exists but the dependency is failing.
Type: String
Required: No

 ** httpMethod **   <a name="cloudwatchomni-Type-EdgeProperties-httpMethod"></a>
The HTTP method observed on the request.
Type: String
Required: No

 ** httpStatusCode **   <a name="cloudwatchomni-Type-EdgeProperties-httpStatusCode"></a>
The HTTP status code observed on the request. Distinct from errorCode.
Type: String
Required: No

 ** protocol **   <a name="cloudwatchomni-Type-EdgeProperties-protocol"></a>
The IANA protocol name for the observed network traffic, such as "tcp".
Type: String
Required: No

 ** serviceInitiated **   <a name="cloudwatchomni-Type-EdgeProperties-serviceInitiated"></a>
Whether the caller was an AWS service principal rather than a user or role. Absent means the edge was not derived from a source that reports it.
Type: Boolean
Required: No

 ** sourcePort **   <a name="cloudwatchomni-Type-EdgeProperties-sourcePort"></a>
The source port of the observed traffic. May be a placeholder when the port is unknown.
Type: String
Required: No

 ** trafficStats **   <a name="cloudwatchomni-Type-EdgeProperties-trafficStats"></a>
Traffic counters accumulated over the edge's observation window.
Type: [EdgeTrafficStats](API_EdgeTrafficStats.md) object
Required: No

## See Also
<a name="API_EdgeProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/EdgeProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/EdgeProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/EdgeProperties)
