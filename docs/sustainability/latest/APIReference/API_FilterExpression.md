---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_FilterExpression.html
---

# FilterExpression
<a name="API_FilterExpression"></a>

Filters environmental impact values by specific dimension values.

## Contents
<a name="API_FilterExpression_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Dimensions **   <a name="sustainability-Type-FilterExpression-Dimensions"></a>
Filters environmental impact values by specific dimension values. An empty values list means no filter is applied for that dimension. Multiple values within a dimension are combined with OR. Multiple dimensions are combined with AND.
Type: String to array of strings map
Valid Keys: `USAGE_ACCOUNT_ID | REGION | SERVICE`
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_FilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/FilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/FilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/FilterExpression)
