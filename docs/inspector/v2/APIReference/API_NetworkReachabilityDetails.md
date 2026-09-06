---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_NetworkReachabilityDetails.html
---

# NetworkReachabilityDetails
<a name="API_NetworkReachabilityDetails"></a>

Contains the details of a network reachability finding.

## Contents
<a name="API_NetworkReachabilityDetails_Contents"></a>

 ** networkPath **   <a name="inspector2-Type-NetworkReachabilityDetails-networkPath"></a>
An object that contains details about a network path associated with a finding.
Type: [NetworkPath](API_NetworkPath.md) object
Required: Yes

 ** openPortRange **   <a name="inspector2-Type-NetworkReachabilityDetails-openPortRange"></a>
An object that contains details about the open port range associated with a finding.
Type: [PortRange](API_PortRange.md) object
Required: Yes

 ** protocol **   <a name="inspector2-Type-NetworkReachabilityDetails-protocol"></a>
The protocol associated with a finding.
Type: String
Valid Values: `TCP | UDP`
Required: Yes

## See Also
<a name="API_NetworkReachabilityDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/NetworkReachabilityDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/NetworkReachabilityDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/NetworkReachabilityDetails)
