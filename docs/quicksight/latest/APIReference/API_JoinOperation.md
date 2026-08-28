---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_JoinOperation.html
---

# JoinOperation
<a name="API_JoinOperation"></a>

A transform operation that combines data from two sources based on specified join conditions.

## Contents
<a name="API_JoinOperation_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Alias **   <a name="QS-Type-JoinOperation-Alias"></a>
Alias for this operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** LeftOperand **   <a name="QS-Type-JoinOperation-LeftOperand"></a>
The left operand for the join operation.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: Yes

 ** OnClause **   <a name="QS-Type-JoinOperation-OnClause"></a>
The join condition that specifies how to match rows between the left and right operands.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: Yes

 ** RightOperand **   <a name="QS-Type-JoinOperation-RightOperand"></a>
The right operand for the join operation.
Type: [TransformOperationSource](API_TransformOperationSource.md) object
Required: Yes

 ** Type **   <a name="QS-Type-JoinOperation-Type"></a>
The type of join to perform, such as `INNER`, `LEFT`, `RIGHT`, or `OUTER`.
Type: String
Valid Values: `INNER | OUTER | LEFT | RIGHT`
Required: Yes

 ** LeftOperandProperties **   <a name="QS-Type-JoinOperation-LeftOperandProperties"></a>
Properties that control how the left operand's columns are handled in the join result.
Type: [JoinOperandProperties](API_JoinOperandProperties.md) object
Required: No

 ** RightOperandProperties **   <a name="QS-Type-JoinOperation-RightOperandProperties"></a>
Properties that control how the right operand's columns are handled in the join result.
Type: [JoinOperandProperties](API_JoinOperandProperties.md) object
Required: No

## See Also
<a name="API_JoinOperation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/JoinOperation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/JoinOperation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/JoinOperation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
