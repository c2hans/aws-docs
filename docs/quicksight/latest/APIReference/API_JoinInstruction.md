---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_JoinInstruction.html
---

# JoinInstruction
<a name="API_JoinInstruction"></a>

The instructions associated with a join.

## Contents
<a name="API_JoinInstruction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** LeftOperand **   <a name="QS-Type-JoinInstruction-LeftOperand"></a>
The operand on the left side of a join.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** OnClause **   <a name="QS-Type-JoinInstruction-OnClause"></a>
The join instructions provided in the `ON` clause of a join.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** RightOperand **   <a name="QS-Type-JoinInstruction-RightOperand"></a>
The operand on the right side of a join.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-zA-Z-]*`
Required: Yes

 ** Type **   <a name="QS-Type-JoinInstruction-Type"></a>
The type of join that it is.
Type: String
Valid Values: `INNER | OUTER | LEFT | RIGHT`
Required: Yes

 ** LeftJoinKeyProperties **   <a name="QS-Type-JoinInstruction-LeftJoinKeyProperties"></a>
Join key properties of the left operand.
Type: [JoinKeyProperties](API_JoinKeyProperties.md) object
Required: No

 ** RightJoinKeyProperties **   <a name="QS-Type-JoinInstruction-RightJoinKeyProperties"></a>
Join key properties of the right operand.
Type: [JoinKeyProperties](API_JoinKeyProperties.md) object
Required: No

## See Also
<a name="API_JoinInstruction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/JoinInstruction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/JoinInstruction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/JoinInstruction)
