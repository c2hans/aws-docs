---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Byoasn.html
---

# Byoasn
<a name="API_Byoasn"></a>

The Autonomous System Number (ASN) and BYOIP CIDR association.

## Contents
<a name="API_Byoasn_Contents"></a>

 ** asn **
A public 2-byte or 4-byte ASN.
Type: String
Required: No

 ** ipamId **
An IPAM ID.
Type: String
Required: No

 ** state **
The provisioning state of the BYOASN.
Type: String
Valid Values: `deprovisioned | failed-deprovision | failed-provision | pending-deprovision | pending-provision | provisioned`
Required: No

 ** statusMessage **
The status message.
Type: String
Required: No

## See Also
<a name="API_Byoasn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/Byoasn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/Byoasn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/Byoasn)
