---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SchemaStatusDetail.html
---

# SchemaStatusDetail
<a name="API_SchemaStatusDetail"></a>

Information about the schema status.

A status of `READY` means that based on the schema analysis rule, queries of the given analysis rule type are properly configured to run queries on this schema.

## Contents
<a name="API_SchemaStatusDetail_Contents"></a>

 ** analysisType **   <a name="API-Type-SchemaStatusDetail-analysisType"></a>
The type of analysis that can be performed on the schema.
A schema can have an `analysisType` of `DIRECT_ANALYSIS`, `ADDITIONAL_ANALYSIS_FOR_AUDIENCE_GENERATION`, or both.
Type: String
Valid Values: `DIRECT_ANALYSIS | ADDITIONAL_ANALYSIS`
Required: Yes

 ** status **   <a name="API-Type-SchemaStatusDetail-status"></a>
The status of the schema, indicating if it is ready to query.
Type: String
Valid Values: `READY | NOT_READY`
Required: Yes

 ** analysisRuleType **   <a name="API-Type-SchemaStatusDetail-analysisRuleType"></a>
The analysis rule type for which the schema status has been evaluated.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM | ID_MAPPING_TABLE`
Required: No

 ** configurations **   <a name="API-Type-SchemaStatusDetail-configurations"></a>
The configuration details of the schema analysis rule for the given type.
Type: Array of strings
Valid Values: `DIFFERENTIAL_PRIVACY`
Required: No

 ** reasons **   <a name="API-Type-SchemaStatusDetail-reasons"></a>
The reasons why the schema status is set to its current state.
Type: Array of [SchemaStatusReason](API_SchemaStatusReason.md) objects
Required: No

## See Also
<a name="API_SchemaStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SchemaStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SchemaStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SchemaStatusDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
