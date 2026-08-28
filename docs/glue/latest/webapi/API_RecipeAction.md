---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_RecipeAction.html
---

# RecipeAction
<a name="API_RecipeAction"></a>

Actions defined in the AWS Glue Studio data preparation recipe node.

## Contents
<a name="API_RecipeAction_Contents"></a>

 ** Operation **   <a name="Glue-Type-RecipeAction-Operation"></a>
The operation of the recipe action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z\_]+$`
Required: Yes

 ** Parameters **   <a name="Glue-Type-RecipeAction-Parameters"></a>
The parameters of the recipe action.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^[A-Za-z0-9]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: No

## See Also
<a name="API_RecipeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/RecipeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/RecipeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/RecipeAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
