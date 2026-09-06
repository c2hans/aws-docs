---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TopicConstantValue.html
---

# TopicConstantValue
<a name="API_TopicConstantValue"></a>

The definition for a `TopicConstantValue`.

## Contents
<a name="API_TopicConstantValue_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ConstantType **   <a name="QS-Type-TopicConstantValue-ConstantType"></a>
The constant type of a `TopicConstantValue`.
Type: String
Valid Values: `SINGULAR | RANGE | COLLECTIVE`
Required: No

 ** Maximum **   <a name="QS-Type-TopicConstantValue-Maximum"></a>
The maximum for the `TopicConstantValue`.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Minimum **   <a name="QS-Type-TopicConstantValue-Minimum"></a>
The minimum for the `TopicConstantValue`.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** Value **   <a name="QS-Type-TopicConstantValue-Value"></a>
The value of the `TopicConstantValue`.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** ValueList **   <a name="QS-Type-TopicConstantValue-ValueList"></a>
The value list of the `TopicConstantValue`.
Type: Array of [CollectiveConstantEntry](API_CollectiveConstantEntry.md) objects
Array Members: Maximum number of 2000 items.
Required: No

## See Also
<a name="API_TopicConstantValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TopicConstantValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TopicConstantValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TopicConstantValue)
