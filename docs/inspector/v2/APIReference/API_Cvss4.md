---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Cvss4.html
---

# Cvss4
<a name="API_Cvss4"></a>

The Common Vulnerability Scoring System (CVSS) version 4 details for the vulnerability.

## Contents
<a name="API_Cvss4_Contents"></a>

 ** baseScore **   <a name="inspector2-Type-Cvss4-baseScore"></a>
The base CVSS v4 score for the vulnerability finding, which rates the severity of the vulnerability on a scale from 0 to 10.
Type: Double
Required: No

 ** scoringVector **   <a name="inspector2-Type-Cvss4-scoringVector"></a>
The CVSS v4 scoring vector, which contains the metrics and measurements that were used to calculate the base score.
Type: String
Length Constraints: Minimum length of 0.
Required: No

## See Also
<a name="API_Cvss4_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Cvss4)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Cvss4)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Cvss4)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
