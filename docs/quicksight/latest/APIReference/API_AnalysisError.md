---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AnalysisError.html
---

# AnalysisError
<a name="API_AnalysisError"></a>

Analysis error.

## Contents
<a name="API_AnalysisError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Message **   <a name="QS-Type-AnalysisError-Message"></a>
The message associated with the analysis error.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="QS-Type-AnalysisError-Type"></a>
The type of the analysis error.
Type: String
Valid Values: `ACCESS_DENIED | SOURCE_NOT_FOUND | DATA_SET_NOT_FOUND | INTERNAL_FAILURE | PARAMETER_VALUE_INCOMPATIBLE | PARAMETER_TYPE_INVALID | PARAMETER_NOT_FOUND | COLUMN_TYPE_MISMATCH | COLUMN_GEOGRAPHIC_ROLE_MISMATCH | COLUMN_REPLACEMENT_MISSING`
Required: No

 ** ViolatedEntities **   <a name="QS-Type-AnalysisError-ViolatedEntities"></a>
Lists the violated entities that caused the analysis error
Type: Array of [Entity](API_Entity.md) objects
Array Members: Maximum number of 200 items.
Required: No

## See Also
<a name="API_AnalysisError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AnalysisError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AnalysisError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AnalysisError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
