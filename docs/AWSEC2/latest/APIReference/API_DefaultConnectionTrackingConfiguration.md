---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DefaultConnectionTrackingConfiguration.html
---

# DefaultConnectionTrackingConfiguration
<a name="API_DefaultConnectionTrackingConfiguration"></a>

Indicates default conntrack information for the instance type. For more information, see [ Connection tracking timeouts ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#connection-tracking-timeouts) in the Amazon EC2 User Guide.

## Contents
<a name="API_DefaultConnectionTrackingConfiguration_Contents"></a>

 ** defaultTcpEstablishedTimeout **
Default timeout (in seconds) for idle TCP connections in an established state.
Type: Integer
Required: No

 ** defaultUdpStreamTimeout **
Default timeout (in seconds) for idle UDP flows classified as streams which have seen more than one request-response transaction.
Type: Integer
Required: No

 ** defaultUdpTimeout **
Default timeout (in seconds) for idle UDP flows that have seen traffic only in a single direction or a single request-response transaction.
Type: Integer
Required: No

## See Also
<a name="API_DefaultConnectionTrackingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DefaultConnectionTrackingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DefaultConnectionTrackingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DefaultConnectionTrackingConfiguration)
