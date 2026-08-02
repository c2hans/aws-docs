---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_CvssScoreDetails.html
---

# CvssScoreDetails
<a name="API_CvssScoreDetails"></a>

Information about the CVSS score.

## Contents
<a name="API_CvssScoreDetails_Contents"></a>

 ** adjustments **   <a name="ECR-Type-CvssScoreDetails-adjustments"></a>
An object that contains details about adjustment Amazon Inspector made to the CVSS score.
Type: Array of [CvssScoreAdjustment](API_CvssScoreAdjustment.md) objects
Required: No

 ** score **   <a name="ECR-Type-CvssScoreDetails-score"></a>
The CVSS score.
Type: Double
Required: No

 ** scoreSource **   <a name="ECR-Type-CvssScoreDetails-scoreSource"></a>
The source for the CVSS score.
Type: String
Required: No

 ** scoringVector **   <a name="ECR-Type-CvssScoreDetails-scoringVector"></a>
The vector for the CVSS score.
Type: String
Required: No

 ** version **   <a name="ECR-Type-CvssScoreDetails-version"></a>
The CVSS version used in scoring.
Type: String
Required: No

## See Also
<a name="API_CvssScoreDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/CvssScoreDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/CvssScoreDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/CvssScoreDetails)
