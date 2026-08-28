---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionGroupDetail.html
---

# DimensionGroupDetail
<a name="API_DimensionGroupDetail"></a>

Information about dimensions within a dimension group.

## Contents
<a name="API_DimensionGroupDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimensions **   <a name="performanceinsights-Type-DimensionGroupDetail-Dimensions"></a>
The dimensions within a dimension group.
Type: Array of [DimensionDetail](API_DimensionDetail.md) objects
Required: No

 ** Group **   <a name="performanceinsights-Type-DimensionGroupDetail-Group"></a>
The name of the dimension group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_DimensionGroupDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/DimensionGroupDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/DimensionGroupDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/DimensionGroupDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
