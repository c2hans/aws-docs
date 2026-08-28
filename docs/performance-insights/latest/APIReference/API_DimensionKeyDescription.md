---
source_url: https://docs.aws.amazon.com/performance-insights/latest/APIReference/API_DimensionKeyDescription.html
---

# DimensionKeyDescription
<a name="API_DimensionKeyDescription"></a>

An object that includes the requested dimension key values and aggregated metric values within a dimension group.

## Contents
<a name="API_DimensionKeyDescription_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AdditionalMetrics **   <a name="performanceinsights-Type-DimensionKeyDescription-AdditionalMetrics"></a>
A map that contains the value for each additional metric.
Type: String to double map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*\S.*`
Required: No

 ** Dimensions **   <a name="performanceinsights-Type-DimensionKeyDescription-Dimensions"></a>
A map of name-value pairs for the dimensions in the group.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Key Pattern: `.*\S.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*\S.*`
Required: No

 ** Partitions **   <a name="performanceinsights-Type-DimensionKeyDescription-Partitions"></a>
If `PartitionBy` was specified, `PartitionKeys` contains the dimensions that were.
Type: Array of doubles
Required: No

 ** Total **   <a name="performanceinsights-Type-DimensionKeyDescription-Total"></a>
The aggregated metric value for the dimensions, over the requested time range.
Type: Double
Required: No

## See Also
<a name="API_DimensionKeyDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pi-2018-02-27/DimensionKeyDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pi-2018-02-27/DimensionKeyDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pi-2018-02-27/DimensionKeyDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS Performance Insights. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query performance-insights` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
