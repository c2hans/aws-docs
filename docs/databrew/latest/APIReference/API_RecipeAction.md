---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_RecipeAction.html
---

# RecipeAction
<a name="API_RecipeAction"></a>

Represents a transformation and associated parameters that are used to apply a change to a DataBrew dataset. For more information, see [Recipe actions reference](https://docs.aws.amazon.com/databrew/latest/dg/recipe-actions-reference.html).

## Contents
<a name="API_RecipeAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Operation **   <a name="databrew-Type-RecipeAction-Operation"></a>
The name of a valid DataBrew transformation to be performed on the data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z\_]+$`
Required: Yes

 ** Parameters **   <a name="databrew-Type-RecipeAction-Parameters"></a>
Contextual parameters for the transformation.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^[A-Za-z0-9]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 32768.
Required: No

## See Also
<a name="API_RecipeAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/RecipeAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/RecipeAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/RecipeAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
