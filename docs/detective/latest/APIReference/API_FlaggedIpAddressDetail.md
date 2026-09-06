---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_FlaggedIpAddressDetail.html
---

# FlaggedIpAddressDetail
<a name="API_FlaggedIpAddressDetail"></a>

Contains information on suspicious IP addresses identified as indicators of compromise. This indicator is derived from AWS threat intelligence.

## Contents
<a name="API_FlaggedIpAddressDetail_Contents"></a>

 ** IpAddress **   <a name="detective-Type-FlaggedIpAddressDetail-IpAddress"></a>
IP address of the suspicious entity.
Type: String
Required: No

 ** Reason **   <a name="detective-Type-FlaggedIpAddressDetail-Reason"></a>
Details the reason the IP address was flagged as suspicious.
Type: String
Valid Values: `AWS_THREAT_INTELLIGENCE`
Required: No

## See Also
<a name="API_FlaggedIpAddressDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/FlaggedIpAddressDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/FlaggedIpAddressDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/FlaggedIpAddressDetail)
