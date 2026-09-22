---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_CvssScore.html
---

# CvssScore
<a name="API_CvssScore"></a>

A CVSS score for the vulnerability, as published by the vulnerability source. Sources include the National Vulnerability Database (NVD) and the operating system vendor's security feed. A finding can include CVSS scores from multiple sources and CVSS versions.

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
