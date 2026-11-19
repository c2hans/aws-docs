---
source_url: https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_PeriodontalReview.html
---

# PeriodontalReview

An item of the periodontal chart that needs the clinician's confirmation.

## Contents
<a name="API_PeriodontalReview_Contents"></a>

 ** reason **   <a name="connecthealth-Type-PeriodontalReview-reason"></a>
The reason for review. The following values are valid:
+  `SITE_NOT_CHARTED`: One or more sites have no reading.
+  `VALUE_NOT_CHARTED`: A dictated value or charting instruction was not charted, for example because the value was out of range or not valid at its position.
+  `READING_COUNT_MISMATCH`: The number of dictated values did not match the number of open sites. The values were charted as dictated.
+  `LINE_UNCLEAR`: A line of dictation could not be interpreted and was not charted.
+  `TOOTH_UNCLEAR`: A line of dictation did not identify the tooth and was not charted.
+  `MISSING_TOOTH_CONFLICT`: The dictation conflicts with a tooth marked as missing.
+  `MEASUREMENT_NOT_CHARTED`: The dictation included a measurement that the chart does not record, such as plaque, calculus, or the mucogingival junction.
+  `SESSION_ISSUE`: The exam setup could not be used and all teeth were assumed to be present, or the earlier chart could not be restored and charting restarted.
Type: String
Valid Values: `SITE_NOT_CHARTED | VALUE_NOT_CHARTED | READING_COUNT_MISMATCH | LINE_UNCLEAR | TOOTH_UNCLEAR | MISSING_TOOTH_CONFLICT | MEASUREMENT_NOT_CHARTED | SESSION_ISSUE`
Required: Yes

 ** sites **   <a name="connecthealth-Type-PeriodontalReview-sites"></a>
The probing sites of that tooth that the item refers to.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 6 items.
Valid Values: `DB | B | MB | DL | L | ML`
Required: No

 ** toothNumber **   <a name="connecthealth-Type-PeriodontalReview-toothNumber"></a>
The tooth that the item refers to.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 32.
Required: No

## See Also
<a name="API_PeriodontalReview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connecthealth-2025-01-29/PeriodontalReview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connecthealth-2025-01-29/PeriodontalReview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connecthealth-2025-01-29/PeriodontalReview)
