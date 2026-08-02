---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ArrayValue.html
---

# ArrayValue
<a name="API_ArrayValue"></a>

Contains an array.

## Contents
<a name="API_ArrayValue_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** arrayValues **   <a name="rdsdtataservice-Type-ArrayValue-arrayValues"></a>
An array of arrays.
Type: Array of [ArrayValue](#API_ArrayValue) objects
Required: No

 ** booleanValues **   <a name="rdsdtataservice-Type-ArrayValue-booleanValues"></a>
An array of Boolean values.
Type: Array of booleans
Required: No

 ** doubleValues **   <a name="rdsdtataservice-Type-ArrayValue-doubleValues"></a>
An array of floating-point numbers.
Type: Array of doubles
Required: No

 ** longValues **   <a name="rdsdtataservice-Type-ArrayValue-longValues"></a>
An array of integers.
Type: Array of longs
Required: No

 ** stringValues **   <a name="rdsdtataservice-Type-ArrayValue-stringValues"></a>
An array of strings.
Type: Array of strings
Required: No

## See Also
<a name="API_ArrayValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/ArrayValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/ArrayValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/ArrayValue)
