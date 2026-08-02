---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_Value.html
---

# Value
<a name="API_Value"></a>

Contains the value of a column.

**Note**
This data structure is only used with the deprecated `ExecuteSql` operation. Use the `BatchExecuteStatement` or `ExecuteStatement` operation instead.

## Contents
<a name="API_Value_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arrayValues **   <a name="rdsdtataservice-Type-Value-arrayValues"></a>
An array of column values.
Type: Array of [Value](#API_Value) objects
Required: No

 ** bigIntValue **   <a name="rdsdtataservice-Type-Value-bigIntValue"></a>
A value for a column of big integer data type.
Type: Long
Required: No

 ** bitValue **   <a name="rdsdtataservice-Type-Value-bitValue"></a>
A value for a column of BIT data type.
Type: Boolean
Required: No

 ** blobValue **   <a name="rdsdtataservice-Type-Value-blobValue"></a>
A value for a column of BLOB data type.
Type: Base64-encoded binary data object
Required: No

 ** doubleValue **   <a name="rdsdtataservice-Type-Value-doubleValue"></a>
A value for a column of double data type.
Type: Double
Required: No

 ** intValue **   <a name="rdsdtataservice-Type-Value-intValue"></a>
A value for a column of integer data type.
Type: Integer
Required: No

 ** isNull **   <a name="rdsdtataservice-Type-Value-isNull"></a>
A NULL value.
Type: Boolean
Required: No

 ** realValue **   <a name="rdsdtataservice-Type-Value-realValue"></a>
A value for a column of real data type.
Type: Float
Required: No

 ** stringValue **   <a name="rdsdtataservice-Type-Value-stringValue"></a>
A value for a column of string data type.
Type: String
Required: No

 ** structValue **   <a name="rdsdtataservice-Type-Value-structValue"></a>
A value for a column of STRUCT data type.
Type: [StructValue](API_StructValue.md) object
Required: No

## See Also
<a name="API_Value_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/Value)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/Value)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/Value)
