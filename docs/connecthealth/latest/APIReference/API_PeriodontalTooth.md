---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_PeriodontalTooth.html
---

# PeriodontalTooth
<a name="API_PeriodontalTooth"></a>

The chart for one tooth.

## Contents
<a name="API_PeriodontalTooth_Contents"></a>

 ** missing **   <a name="connecthealth-Type-PeriodontalTooth-missing"></a>
Specifies whether the tooth is missing.
Type: Boolean
Required: Yes

 ** toothNumber **   <a name="connecthealth-Type-PeriodontalTooth-toothNumber"></a>
The tooth number in the Universal Numbering System. The value ranges from 1 to 32.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 32.
Required: Yes

 ** furcation **   <a name="connecthealth-Type-PeriodontalTooth-furcation"></a>
The furcation involvement class. The value ranges from 0 to 3.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3.
Required: No

 ** mobility **   <a name="connecthealth-Type-PeriodontalTooth-mobility"></a>
The tooth mobility grade. The value ranges from 0 to 3.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 3.
Required: No

 ** sites **   <a name="connecthealth-Type-PeriodontalTooth-sites"></a>
The probing sites that have a recorded measurement, in the order `MB`, `B`, `DB`, `ML`, `L`, `DL`.
Type: Array of [PeriodontalSite](API_PeriodontalSite.md) objects
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Required: No

## See Also
<a name="API_PeriodontalTooth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/PeriodontalTooth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/PeriodontalTooth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/PeriodontalTooth)
