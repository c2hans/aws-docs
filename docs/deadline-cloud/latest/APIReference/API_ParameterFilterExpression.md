---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ParameterFilterExpression.html
---

# ParameterFilterExpression
<a name="API_ParameterFilterExpression"></a>

The details of a filtered search for parameters.

## Contents
<a name="API_ParameterFilterExpression_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-ParameterFilterExpression-name"></a>
The name of the parameter to filter on.
Type: String
Required: Yes

 ** operator **   <a name="deadlinecloud-Type-ParameterFilterExpression-operator"></a>
The type of comparison to use to filter results.
Type: String
Valid Values: `EQUAL | NOT_EQUAL | GREATER_THAN_EQUAL_TO | GREATER_THAN | LESS_THAN_EQUAL_TO | LESS_THAN | ANY_EQUALS | ALL_NOT_EQUALS`
Required: Yes

 ** value **   <a name="deadlinecloud-Type-ParameterFilterExpression-value"></a>
The parameter's value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ParameterFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/ParameterFilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/ParameterFilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/ParameterFilterExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
