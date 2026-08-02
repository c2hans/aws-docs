---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_ConditionalSpecification.html
---

# ConditionalSpecification
<a name="API_ConditionalSpecification"></a>

Provides a list of conditional branches. Branches are evaluated in the order that they are entered in the list. The first branch with a condition that evaluates to true is executed. The last branch in the list is the default branch. The default branch should not have any condition expression. The default branch is executed if no other branch has a matching condition.

## Contents
<a name="API_ConditionalSpecification_Contents"></a>

 ** active **   <a name="lexv2-Type-ConditionalSpecification-active"></a>
Determines whether a conditional branch is active. When `active` is false, the conditions are not evaluated.
Type: Boolean
Required: Yes

 ** conditionalBranches **   <a name="lexv2-Type-ConditionalSpecification-conditionalBranches"></a>
A list of conditional branches. A conditional branch is made up of a condition, a response and a next step. The response and next step are executed when the condition is true.
Type: Array of [ConditionalBranch](API_ConditionalBranch.md) objects
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Required: Yes

 ** defaultBranch **   <a name="lexv2-Type-ConditionalSpecification-defaultBranch"></a>
The conditional branch that should be followed when the conditions for other branches are not satisfied. A conditional branch is made up of a condition, a response and a next step.
Type: [DefaultConditionalBranch](API_DefaultConditionalBranch.md) object
Required: Yes

## See Also
<a name="API_ConditionalSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/ConditionalSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/ConditionalSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/ConditionalSpecification)
