---
source_url: https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_RealtimeEndpointInfo.html
---

# RealtimeEndpointInfo
<a name="API_RealtimeEndpointInfo"></a>

 Describes the real-time endpoint information for an `MLModel`.

## Contents
<a name="API_RealtimeEndpointInfo_Contents"></a>

 ** CreatedAt **   <a name="amazonml-Type-RealtimeEndpointInfo-CreatedAt"></a>
The time that the request to create the real-time endpoint for the `MLModel` was received. The time is expressed in epoch time.
Type: Timestamp
Required: No

 ** EndpointStatus **   <a name="amazonml-Type-RealtimeEndpointInfo-EndpointStatus"></a>
 The current status of the real-time endpoint for the `MLModel`. This element can have one of the following values:
+  `NONE` - Endpoint does not exist or was previously deleted.
+  `READY` - Endpoint is ready to be used for real-time predictions.
+  `UPDATING` - Updating/creating the endpoint.
Type: String
Valid Values: `NONE | READY | UPDATING | FAILED`
Required: No

 ** EndpointUrl **   <a name="amazonml-Type-RealtimeEndpointInfo-EndpointUrl"></a>
The URI that specifies where to send real-time prediction requests for the `MLModel`.
 **Note:** The application must wait until the real-time endpoint is ready before using this URI.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `https://[a-zA-Z0-9-.]*\.amazon(aws)?\.com[/]?`
Required: No

 ** PeakRequestsPerSecond **   <a name="amazonml-Type-RealtimeEndpointInfo-PeakRequestsPerSecond"></a>
 The maximum processing rate for the real-time endpoint for `MLModel`, measured in incoming requests per second.
Type: Integer
Required: No

## See Also
<a name="API_RealtimeEndpointInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/machinelearning-2014-12-12/RealtimeEndpointInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/machinelearning-2014-12-12/RealtimeEndpointInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/machinelearning-2014-12-12/RealtimeEndpointInfo)
