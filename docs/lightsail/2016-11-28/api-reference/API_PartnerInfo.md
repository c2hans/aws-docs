---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_PartnerInfo.html
---

# PartnerInfo
<a name="API_PartnerInfo"></a>

An object that contains information about the Lightsail partner program membership of an Amazon Lightsail account.

## Contents
<a name="API_PartnerInfo_Contents"></a>

 ** enrolledAt **   <a name="Lightsail-Type-PartnerInfo-enrolledAt"></a>
The timestamp when the account was enrolled in the Lightsail partner program.
Type: Timestamp
Required: Yes

 ** status **   <a name="Lightsail-Type-PartnerInfo-status"></a>
The status of the partner membership.
The following statuses are possible:
+  `Active` – The membership is active, and the benefits of the current tier are available to the account.
+  `Suspended` – The membership is suspended, and the benefits of the tier are not available to the account.
Type: String
Valid Values: `Active | Suspended`
Required: Yes

 ** tierName **   <a name="Lightsail-Type-PartnerInfo-tierName"></a>
The tier of the partner membership.
Type: String
Valid Values: `Essential | Growth | Accelerate | Premier`
Required: No

## See Also
<a name="API_PartnerInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/PartnerInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/PartnerInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/PartnerInfo)
