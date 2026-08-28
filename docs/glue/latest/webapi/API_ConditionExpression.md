---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_ConditionExpression.html
---

# ConditionExpression
<a name="API_ConditionExpression"></a>

Condition expression defined in the AWS Glue Studio data preparation recipe node.

## Contents
<a name="API_ConditionExpression_Contents"></a>

 ** Condition **   <a name="Glue-Type-ConditionExpression-Condition"></a>
The condition of the condition expression.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z\_]+$`
Required: Yes

 ** TargetColumn **   <a name="Glue-Type-ConditionExpression-TargetColumn"></a>
The target column of the condition expressions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Value **   <a name="Glue-Type-ConditionExpression-Value"></a>
The value of the condition expression.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_ConditionExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/ConditionExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/ConditionExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/ConditionExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
