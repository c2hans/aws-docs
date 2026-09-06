---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CvssScore.html
---

# CvssScore
<a name="API_CvssScore"></a>

Amazon Inspector generates a risk score for each finding. This score helps you to prioritize findings, to focus on the most critical findings and the most vulnerable resources. The score uses the Common Vulnerability Scoring System (CVSS) format. This format is a modification of the base CVSS score that the National Vulnerability Database (NVD) provides. For more information about severity levels, see [Severity levels for Amazon Inspector findings](https://docs.aws.amazon.com/inspector/latest/user/findings-understanding-severity.html) in the *Amazon Inspector User Guide*.

## Contents
<a name="API_CvssScore_Contents"></a>

 ** baseScore **   <a name="imagebuilder-Type-CvssScore-baseScore"></a>
The CVSS base score.
Type: Double
Valid Range: Minimum value of 0.
Required: No

 ** scoringVector **   <a name="imagebuilder-Type-CvssScore-scoringVector"></a>
The vector string of the CVSS score.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** source **   <a name="imagebuilder-Type-CvssScore-source"></a>
The source of the CVSS score.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** version **   <a name="imagebuilder-Type-CvssScore-version"></a>
The CVSS version that generated the score.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## See Also
<a name="API_CvssScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/CvssScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/CvssScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/CvssScore)
