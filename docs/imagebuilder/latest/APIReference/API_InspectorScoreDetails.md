---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InspectorScoreDetails.html
---

# InspectorScoreDetails
<a name="API_InspectorScoreDetails"></a>

Information about the factors that influenced the score that Amazon Inspector assigned for a finding.

## Contents
<a name="API_InspectorScoreDetails_Contents"></a>

 ** adjustedCvss **   <a name="imagebuilder-Type-InspectorScoreDetails-adjustedCvss"></a>
The CVSS score that Amazon Inspector assigned to the finding after applying its adjustments. It includes the score source, CVSS version, scoring vector, and the adjustments applied.
Type: [CvssScoreDetails](API_CvssScoreDetails.md) object
Required: No

## See Also
<a name="API_InspectorScoreDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/InspectorScoreDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/InspectorScoreDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/InspectorScoreDetails)
