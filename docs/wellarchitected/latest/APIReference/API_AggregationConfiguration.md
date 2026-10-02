---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_AggregationConfiguration.html
---

# AggregationConfiguration
<a name="API_AggregationConfiguration"></a>

Configuration settings that define the scope of AWS resources to analyze for optimization recommendations.

## Contents
<a name="API_AggregationConfiguration_Contents"></a>

 ** accessRoleArn **   <a name="wellarchitected-Type-AggregationConfiguration-accessRoleArn"></a>
The ARN of an IAM role to assume for resource analysis in this account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:([a-z\-]+):iam::\d{12}:role/(service-role/)?[a-zA-Z0-9+=,.@\-_]+`
Required: Yes

 ** accountId **   <a name="wellarchitected-Type-AggregationConfiguration-accountId"></a>
The AWS account ID to analyze.
Type: String
Pattern: `\d{12}`
Required: Yes

 ** regions **   <a name="wellarchitected-Type-AggregationConfiguration-regions"></a>
A list of AWS Regions to include in the analysis.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[a-z]{2}-[a-z]+-\d{1}`
Required: Yes

## See Also
<a name="API_AggregationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/AggregationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/AggregationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/AggregationConfiguration)
