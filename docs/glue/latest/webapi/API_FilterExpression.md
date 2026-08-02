---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_FilterExpression.html
---

# FilterExpression
<a name="API_FilterExpression"></a>

Specifies a filter expression.

## Contents
<a name="API_FilterExpression_Contents"></a>

 ** Operation **   <a name="Glue-Type-FilterExpression-Operation"></a>
The type of operation to perform in the expression.
Type: String
Valid Values: `EQ | LT | GT | LTE | GTE | REGEX | ISNULL`
Required: Yes

 ** Values **   <a name="Glue-Type-FilterExpression-Values"></a>
A list of filter values.
Type: Array of [FilterValue](API_FilterValue.md) objects
Required: Yes

 ** Negated **   <a name="Glue-Type-FilterExpression-Negated"></a>
Whether the expression is to be negated.
Type: Boolean
Required: No

## See Also
<a name="API_FilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/FilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/FilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/FilterExpression)
