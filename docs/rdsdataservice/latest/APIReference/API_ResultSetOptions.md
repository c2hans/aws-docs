---
source_url: https://docs.aws.amazon.com/rdsdataservice/latest/APIReference/API_ResultSetOptions.html
---

# ResultSetOptions
<a name="API_ResultSetOptions"></a>

Options that control how the result set is returned.

## Contents
<a name="API_ResultSetOptions_Contents"></a>

 ** decimalReturnType **   <a name="rdsdtataservice-Type-ResultSetOptions-decimalReturnType"></a>
A value that indicates how a field of `DECIMAL` type is represented in the response. The value of `STRING`, the default, specifies that it is converted to a String value. The value of `DOUBLE_OR_LONG` specifies that it is converted to a Long value if its scale is 0, or to a Double value otherwise.
Conversion to Double or Long can result in roundoff errors due to precision loss. We recommend converting to String, especially when working with currency values.
Type: String
Valid Values: `STRING | DOUBLE_OR_LONG`
Required: No

 ** longReturnType **   <a name="rdsdtataservice-Type-ResultSetOptions-longReturnType"></a>
A value that indicates how a field of `LONG` type is represented. Allowed values are `LONG` and `STRING`. The default is `LONG`. Specify `STRING` if the length or precision of numeric values might cause truncation or rounding errors.
Type: String
Valid Values: `STRING | LONG`
Required: No

## See Also
<a name="API_ResultSetOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-data-2018-08-01/ResultSetOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-data-2018-08-01/ResultSetOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-data-2018-08-01/ResultSetOptions)
