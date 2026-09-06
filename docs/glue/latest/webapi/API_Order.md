---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_Order.html
---

# Order
<a name="API_Order"></a>

Specifies the sort order of a sorted column.

## Contents
<a name="API_Order_Contents"></a>

 ** Column **   <a name="Glue-Type-Order-Column"></a>
The name of the column.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** SortOrder **   <a name="Glue-Type-Order-SortOrder"></a>
Indicates that the column is sorted in ascending order (`== 1`), or in descending order (`==0`).
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1.
Required: Yes

## See Also
<a name="API_Order_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/Order)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/Order)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/Order)
