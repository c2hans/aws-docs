---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_RecipeStep.html
---

# RecipeStep
<a name="API_RecipeStep"></a>

Represents a single step from a DataBrew recipe to be performed.

## Contents
<a name="API_RecipeStep_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **   <a name="databrew-Type-RecipeStep-Action"></a>
The particular action to be performed in the recipe step.
Type: [RecipeAction](API_RecipeAction.md) object
Required: Yes

 ** ConditionExpressions **   <a name="databrew-Type-RecipeStep-ConditionExpressions"></a>
One or more conditions that must be met for the recipe step to succeed.
All of the conditions in the array must be met. In other words, all of the conditions must be combined using a logical AND operation.
Type: Array of [ConditionExpression](API_ConditionExpression.md) objects
Required: No

## See Also
<a name="API_RecipeStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/RecipeStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/RecipeStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/RecipeStep)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue DataBrew. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query databrew` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
