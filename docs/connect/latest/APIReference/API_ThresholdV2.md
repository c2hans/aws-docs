---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ThresholdV2.html
---

# ThresholdV2
<a name="API_ThresholdV2"></a>

Contains information about the threshold for service level metrics.

## Contents
<a name="API_ThresholdV2_Contents"></a>

 ** Comparison **   <a name="connect-Type-ThresholdV2-Comparison"></a>
The type of comparison. Currently, "less than" (LT), "less than equal" (LTE), and "greater than" (GT) comparisons are supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Required: No

 ** ThresholdValue **   <a name="connect-Type-ThresholdV2-ThresholdValue"></a>
The threshold value to compare.
Type: Double
Required: No

## See Also
<a name="API_ThresholdV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ThresholdV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ThresholdV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ThresholdV2)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
