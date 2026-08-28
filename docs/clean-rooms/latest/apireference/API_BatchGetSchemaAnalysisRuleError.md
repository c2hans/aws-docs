---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_BatchGetSchemaAnalysisRuleError.html
---

# BatchGetSchemaAnalysisRuleError
<a name="API_BatchGetSchemaAnalysisRuleError"></a>

An error that describes why a schema could not be fetched.

## Contents
<a name="API_BatchGetSchemaAnalysisRuleError_Contents"></a>

 ** code **   <a name="API-Type-BatchGetSchemaAnalysisRuleError-code"></a>
An error code for the error.
Type: String
Required: Yes

 ** message **   <a name="API-Type-BatchGetSchemaAnalysisRuleError-message"></a>
A description of why the call failed.
Type: String
Required: Yes

 ** name **   <a name="API-Type-BatchGetSchemaAnalysisRuleError-name"></a>
An error name for the error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** type **   <a name="API-Type-BatchGetSchemaAnalysisRuleError-type"></a>
The analysis rule type.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM | ID_MAPPING_TABLE`
Required: Yes

## See Also
<a name="API_BatchGetSchemaAnalysisRuleError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/BatchGetSchemaAnalysisRuleError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/BatchGetSchemaAnalysisRuleError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/BatchGetSchemaAnalysisRuleError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
