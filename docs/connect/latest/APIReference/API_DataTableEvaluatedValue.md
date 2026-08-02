---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DataTableEvaluatedValue.html
---

# DataTableEvaluatedValue
<a name="API_DataTableEvaluatedValue"></a>

A data table evaluated value.

## Contents
<a name="API_DataTableEvaluatedValue_Contents"></a>

 ** AttributeName **   <a name="connect-Type-DataTableEvaluatedValue-AttributeName"></a>
The value's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** Error **   <a name="connect-Type-DataTableEvaluatedValue-Error"></a>
The value's error.
Type: Boolean
Required: Yes

 ** EvaluatedValue **   <a name="connect-Type-DataTableEvaluatedValue-EvaluatedValue"></a>
The value's evaluated value.
Type: String
Required: Yes

 ** Found **   <a name="connect-Type-DataTableEvaluatedValue-Found"></a>
The value's found.
Type: Boolean
Required: Yes

 ** PrimaryValues **   <a name="connect-Type-DataTableEvaluatedValue-PrimaryValues"></a>
The value's primary values.
Type: Array of [PrimaryValue](API_PrimaryValue.md) objects
Required: Yes

 ** RecordId **   <a name="connect-Type-DataTableEvaluatedValue-RecordId"></a>
The value's record ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** ValueType **   <a name="connect-Type-DataTableEvaluatedValue-ValueType"></a>
The value's value type.
Type: String
Valid Values: `TEXT | NUMBER | BOOLEAN | TEXT_LIST | NUMBER_LIST`
Required: Yes

## See Also
<a name="API_DataTableEvaluatedValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DataTableEvaluatedValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DataTableEvaluatedValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DataTableEvaluatedValue)
