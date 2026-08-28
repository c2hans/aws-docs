---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SchemaStatusReason.html
---

# SchemaStatusReason
<a name="API_SchemaStatusReason"></a>

A reason why the schema status is set to its current value.

## Contents
<a name="API_SchemaStatusReason_Contents"></a>

 ** code **   <a name="API-Type-SchemaStatusReason-code"></a>
The schema status reason code.
Type: String
Valid Values: `ANALYSIS_RULE_MISSING | ANALYSIS_TEMPLATES_NOT_CONFIGURED | ANALYSIS_PROVIDERS_NOT_CONFIGURED | DIFFERENTIAL_PRIVACY_POLICY_NOT_CONFIGURED | ID_MAPPING_TABLE_NOT_POPULATED | COLLABORATION_ANALYSIS_RULE_NOT_CONFIGURED | ADDITIONAL_ANALYSES_NOT_CONFIGURED | RESULT_RECEIVERS_NOT_CONFIGURED | ADDITIONAL_ANALYSES_NOT_ALLOWED | RESULT_RECEIVERS_NOT_ALLOWED | ANALYSIS_RULE_TYPES_NOT_COMPATIBLE | INTERMEDIATE_TABLE_NOT_POPULATED | INTERMEDIATE_TABLE_ANALYSIS_RULE_MISSING | INTERMEDIATE_TABLE_BASE_TABLE_REMOVED | INTERMEDIATE_TABLE_INHERITED_CONSTRAINTS_VIOLATED | INTERMEDIATE_TABLE_DISALLOWED_BY_DATA_PROVIDER | INTERMEDIATE_TABLE_RETENTION_PERIOD_EXPIRED`
Required: Yes

 ** message **   <a name="API-Type-SchemaStatusReason-message"></a>
An explanation of the schema status reason code.
Type: String
Required: Yes

## See Also
<a name="API_SchemaStatusReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SchemaStatusReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SchemaStatusReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SchemaStatusReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
