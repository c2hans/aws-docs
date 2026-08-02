---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ConnectionTrackingSpecificationResponse.html
---

# ConnectionTrackingSpecificationResponse
<a name="API_ConnectionTrackingSpecificationResponse"></a>

A security group connection tracking specification response that enables you to set the idle timeout for connection tracking on an Elastic network interface. For more information, see [Connection tracking timeouts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_ConnectionTrackingSpecificationResponse_Contents"></a>

 ** tcpEstablishedTimeout **
Timeout (in seconds) for idle TCP connections in an established state. Min: 60 seconds. Max: 432000 seconds (5 days). Default: 350 seconds for Nitro v6 instance types (excluding P6e-GB200); 432000 seconds for all other instance types (including P6e-GB200). Recommended: Less than 432000 seconds.
Type: Integer
Required: No

 ** udpStreamTimeout **
Timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction. Min: 60 seconds. Max: 180 seconds (3 minutes). Default: 180 seconds.
Type: Integer
Required: No

 ** udpTimeout **
Timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction. Min: 30 seconds. Max: 60 seconds. Default: 30 seconds.
Type: Integer
Required: No

## See Also
<a name="API_ConnectionTrackingSpecificationResponse_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ConnectionTrackingSpecificationResponse)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ConnectionTrackingSpecificationResponse)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ConnectionTrackingSpecificationResponse)
