---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SchemaAnalysisRuleRequest.html
---

# SchemaAnalysisRuleRequest
<a name="API_SchemaAnalysisRuleRequest"></a>

Defines the information that's necessary to retrieve an analysis rule schema. Schema analysis rules are uniquely identiﬁed by a combination of the schema name and the analysis rule type for a given collaboration.

## Contents
<a name="API_SchemaAnalysisRuleRequest_Contents"></a>

 ** name **   <a name="API-Type-SchemaAnalysisRuleRequest-name"></a>
The name of the analysis rule schema that you are requesting.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9_](([a-zA-Z0-9_ ]+-)*([a-zA-Z0-9_ ]+))?`
Required: Yes

 ** type **   <a name="API-Type-SchemaAnalysisRuleRequest-type"></a>
The type of analysis rule schema that you are requesting.
Type: String
Valid Values: `AGGREGATION | LIST | CUSTOM | ID_MAPPING_TABLE`
Required: Yes

## See Also
<a name="API_SchemaAnalysisRuleRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SchemaAnalysisRuleRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SchemaAnalysisRuleRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SchemaAnalysisRuleRequest)
