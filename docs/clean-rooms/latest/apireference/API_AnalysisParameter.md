---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_AnalysisParameter.html
---

# AnalysisParameter
<a name="API_AnalysisParameter"></a>

Optional. The member who can query can provide this placeholder for a literal data value in an analysis template.

## Contents
<a name="API_AnalysisParameter_Contents"></a>

 ** name **   <a name="API-Type-AnalysisParameter-name"></a>
The name of the parameter. The name must use only alphanumeric or underscore (\_) characters.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9a-zA-Z_]+`
Required: Yes

 ** type **   <a name="API-Type-AnalysisParameter-type"></a>
The type of parameter.
Type: String
Valid Values: `SMALLINT | INTEGER | BIGINT | DECIMAL | REAL | DOUBLE_PRECISION | BOOLEAN | CHAR | VARCHAR | DATE | TIMESTAMP | TIMESTAMPTZ | TIME | TIMETZ | VARBYTE | BINARY | BYTE | CHARACTER | DOUBLE | FLOAT | INT | LONG | NUMERIC | SHORT | STRING | TIMESTAMP_LTZ | TIMESTAMP_NTZ | TINYINT`
Required: Yes

 ** defaultValue **   <a name="API-Type-AnalysisParameter-defaultValue"></a>
Optional. The default value that is applied in the analysis template. The member who can query can override this value in the query editor.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

## See Also
<a name="API_AnalysisParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/AnalysisParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/AnalysisParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/AnalysisParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
