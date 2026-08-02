---
source_url: https://docs.aws.amazon.com/workspaces-instances/latest/api/API_ConnectionTrackingSpecificationRequest.html
---

# ConnectionTrackingSpecificationRequest
<a name="API_ConnectionTrackingSpecificationRequest"></a>

Defines connection tracking parameters for network interfaces.

## Contents
<a name="API_ConnectionTrackingSpecificationRequest_Contents"></a>

 ** TcpEstablishedTimeout **   <a name="workspacesinstances-Type-ConnectionTrackingSpecificationRequest-TcpEstablishedTimeout"></a>
Timeout for established TCP connections.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** UdpStreamTimeout **   <a name="workspacesinstances-Type-ConnectionTrackingSpecificationRequest-UdpStreamTimeout"></a>
Timeout for UDP stream connections.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** UdpTimeout **   <a name="workspacesinstances-Type-ConnectionTrackingSpecificationRequest-UdpTimeout"></a>
General timeout for UDP connections.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ConnectionTrackingSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-instances-2022-07-26/ConnectionTrackingSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-instances-2022-07-26/ConnectionTrackingSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-instances-2022-07-26/ConnectionTrackingSpecificationRequest)
