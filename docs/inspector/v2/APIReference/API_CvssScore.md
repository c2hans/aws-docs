---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CvssScore.html
---

# CvssScore
<a name="API_CvssScore"></a>

The CVSS score for a finding.

## Contents
<a name="API_CvssScore_Contents"></a>

 ** baseScore **   <a name="inspector2-Type-CvssScore-baseScore"></a>
The base CVSS score used for the finding.
Type: Double
Required: Yes

 ** scoringVector **   <a name="inspector2-Type-CvssScore-scoringVector"></a>
The vector string of the CVSS score.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** source **   <a name="inspector2-Type-CvssScore-source"></a>
The source of the CVSS score.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** version **   <a name="inspector2-Type-CvssScore-version"></a>
The version of CVSS used for the score.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_CvssScore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CvssScore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CvssScore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CvssScore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
