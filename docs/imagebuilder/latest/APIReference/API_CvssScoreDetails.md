---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CvssScoreDetails.html
---

# CvssScoreDetails
<a name="API_CvssScoreDetails"></a>

Details about the source of the score, and the factors that determined the adjustments to create the final score.

## Contents
<a name="API_CvssScoreDetails_Contents"></a>

 ** adjustments **   <a name="imagebuilder-Type-CvssScoreDetails-adjustments"></a>
The adjustments that Amazon Inspector applied to the base CVSS score to produce its own score for the finding. The list is empty when Amazon Inspector made no adjustments.
Type: Array of [CvssScoreAdjustment](API_CvssScoreAdjustment.md) objects
Required: No

 ** cvssSource **   <a name="imagebuilder-Type-CvssScoreDetails-cvssSource"></a>
The source of the CVSS data that the Amazon Inspector score for the finding is based on, for example NVD or a vendor security feed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** score **   <a name="imagebuilder-Type-CvssScoreDetails-score"></a>
The CVSS score.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** scoreSource **   <a name="imagebuilder-Type-CvssScoreDetails-scoreSource"></a>
The source for the CVSS score.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** scoringVector **   <a name="imagebuilder-Type-CvssScoreDetails-scoringVector"></a>
A vector that measures the severity of the vulnerability.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** version **   <a name="imagebuilder-Type-CvssScoreDetails-version"></a>
The CVSS version that generated the score.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_CvssScoreDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CvssScoreDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CvssScoreDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CvssScoreDetails)
