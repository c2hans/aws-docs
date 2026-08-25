---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_IpamRouteOriginAuthorization.html
---

# IpamRouteOriginAuthorization
<a name="API_IpamRouteOriginAuthorization"></a>

Contains information about a Route Origin Authorization (ROA) published in the RPKI. A ROA cryptographically attests that a specific ASN is authorized to originate a specific IP address prefix.

## Contents
<a name="API_IpamRouteOriginAuthorization_Contents"></a>

 ** asn **
The Autonomous System Number (ASN) authorized by the ROA.
Type: String
Required: No

 ** expiration **
The expiration date of the ROA.
Type: Timestamp
Required: No

 ** match **
Specifies whether the ROA matches the route announcement.
Type: Boolean
Required: No

 ** maxLength **
The maximum prefix length that the ASN is authorized to announce.
Type: Integer
Required: No

 ** prefix **
The IP address prefix authorized by the ROA in CIDR notation.
Type: String
Required: No

## See Also
<a name="API_IpamRouteOriginAuthorization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/IpamRouteOriginAuthorization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/IpamRouteOriginAuthorization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/IpamRouteOriginAuthorization)
