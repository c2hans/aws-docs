---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_PeriodontalSite.html
---

# PeriodontalSite
<a name="API_PeriodontalSite"></a>

The measurements at one probing site of a tooth.

## Contents
<a name="API_PeriodontalSite_Contents"></a>

 ** site **   <a name="connecthealth-Type-PeriodontalSite-site"></a>
The probing site. The following values are valid:
+  `DB`: Distobuccal.
+  `B`: Buccal.
+  `MB`: Mesiobuccal.
+  `DL`: Distolingual.
+  `L`: Lingual.
+  `ML`: Mesiolingual.
Type: String
Valid Values: `DB | B | MB | DL | L | ML`
Required: Yes

 ** bleeding **   <a name="connecthealth-Type-PeriodontalSite-bleeding"></a>
Specifies whether the site bled during probing.
Type: Boolean
Required: No

 ** probingDepth **   <a name="connecthealth-Type-PeriodontalSite-probingDepth"></a>
The probing depth, in millimeters. The value ranges from 0 to 15.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 15.
Required: No

 ** recession **   <a name="connecthealth-Type-PeriodontalSite-recession"></a>
The gingival recession, in millimeters. The value ranges from -5 to 15. For example, `-1` represents "plus one."
Type: Integer
Valid Range: Minimum value of -5. Maximum value of 15.
Required: No

 ** suppuration **   <a name="connecthealth-Type-PeriodontalSite-suppuration"></a>
Specifies whether suppuration was present at the site.
Type: Boolean
Required: No

## See Also
<a name="API_PeriodontalSite_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/PeriodontalSite)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/PeriodontalSite)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/PeriodontalSite)
