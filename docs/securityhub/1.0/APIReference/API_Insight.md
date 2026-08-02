---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Insight.html
---

# Insight
<a name="API_Insight"></a>

Contains information about a Security Hub CSPM insight.

## Contents
<a name="API_Insight_Contents"></a>

 ** Filters **   <a name="securityhub-Type-Insight-Filters"></a>
One or more attributes used to filter the findings included in the insight. You can filter by up to ten finding attributes. For each attribute, you can provide up to 20 filter values. The insight only includes findings that match the criteria defined in the filters.
Type: [AwsSecurityFindingFilters](API_AwsSecurityFindingFilters.md) object
Required: Yes

 ** GroupByAttribute **   <a name="securityhub-Type-Insight-GroupByAttribute"></a>
The grouping attribute for the insight's findings. Indicates how to group the matching findings, and identifies the type of item that the insight applies to. For example, if an insight is grouped by resource identifier, then the insight produces a list of resource identifiers.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** InsightArn **   <a name="securityhub-Type-Insight-InsightArn"></a>
The ARN of a Security Hub CSPM insight.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Name **   <a name="securityhub-Type-Insight-Name"></a>
The name of a Security Hub CSPM insight.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_Insight_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Insight)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Insight)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Insight)
