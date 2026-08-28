---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CvssScoreDetails.html
---

# CvssScoreDetails
<a name="API_CvssScoreDetails"></a>

Information about the CVSS score.

## Contents
<a name="API_CvssScoreDetails_Contents"></a>

 ** score **   <a name="inspector2-Type-CvssScoreDetails-score"></a>
The CVSS score.
Type: Double
Required: Yes

 ** scoreSource **   <a name="inspector2-Type-CvssScoreDetails-scoreSource"></a>
The source for the CVSS score.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** scoringVector **   <a name="inspector2-Type-CvssScoreDetails-scoringVector"></a>
The vector for the CVSS score.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** version **   <a name="inspector2-Type-CvssScoreDetails-version"></a>
The CVSS version used in scoring.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** adjustments **   <a name="inspector2-Type-CvssScoreDetails-adjustments"></a>
An object that contains details about adjustment Amazon Inspector made to the CVSS score.
Type: Array of [CvssScoreAdjustment](API_CvssScoreAdjustment.md) objects
Required: No

 ** cvssSource **   <a name="inspector2-Type-CvssScoreDetails-cvssSource"></a>
The source of the CVSS data.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_CvssScoreDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CvssScoreDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CvssScoreDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CvssScoreDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
