---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_ConditionExpression.html
---

# ConditionExpression
<a name="API_ConditionExpression"></a>

Represents an individual condition that evaluates to true or false.

Conditions are used with recipe actions. The action is only performed for column values where the condition evaluates to true.

If a recipe requires more than one condition, then the recipe must specify multiple `ConditionExpression` elements. Each condition is applied to the rows in a dataset first, before the recipe action is performed.

## Contents
<a name="API_ConditionExpression_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Condition **   <a name="databrew-Type-ConditionExpression-Condition"></a>
A specific condition to apply to a recipe action. For more information, see [Recipe structure](https://docs.aws.amazon.com/databrew/latest/dg/recipes.html#recipes.structure) in the * AWS Glue DataBrew Developer Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[A-Z\_]+$`
Required: Yes

 ** TargetColumn **   <a name="databrew-Type-ConditionExpression-TargetColumn"></a>
A column to apply this condition to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** Value **   <a name="databrew-Type-ConditionExpression-Value"></a>
A value that the condition must evaluate to for the condition to succeed.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

## See Also
<a name="API_ConditionExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/ConditionExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/ConditionExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/ConditionExpression)
