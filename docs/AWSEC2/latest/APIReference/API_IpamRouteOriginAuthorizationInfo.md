---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamRouteOriginAuthorizationInfo.html
---

# IpamRouteOriginAuthorizationInfo
<a name="API_IpamRouteOriginAuthorizationInfo"></a>

Contains information about a Route Origin Authorization (ROA) currently published in the RPKI.

## Contents
<a name="API_IpamRouteOriginAuthorizationInfo_Contents"></a>

 ** asn **
The Autonomous System Number (ASN) authorized to originate the prefix.
Type: String
Required: No

 ** cidr **
The IP address prefix in CIDR notation authorized by the ROA.
Type: String
Required: No

 ** maxLength **
The maximum prefix length that the ASN is authorized to announce.
Type: Integer
Required: No

## See Also
<a name="API_IpamRouteOriginAuthorizationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamRouteOriginAuthorizationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamRouteOriginAuthorizationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamRouteOriginAuthorizationInfo)
