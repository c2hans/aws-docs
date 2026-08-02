---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QuickResponseSearchExpression.html
---

# QuickResponseSearchExpression
<a name="API_amazon-q-connect_QuickResponseSearchExpression"></a>

Information about the import job.

## Contents
<a name="API_amazon-q-connect_QuickResponseSearchExpression_Contents"></a>

 ** filters **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchExpression-filters"></a>
The configuration of filtering rules applied to quick response query results.
Type: Array of [QuickResponseFilterField](API_amazon-q-connect_QuickResponseFilterField.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** orderOnField **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchExpression-orderOnField"></a>
The quick response attribute fields on which the query results are ordered.
Type: [QuickResponseOrderField](API_amazon-q-connect_QuickResponseOrderField.md) object
Required: No

 ** queries **   <a name="connect-Type-amazon-q-connect_QuickResponseSearchExpression-queries"></a>
The quick response query expressions.
Type: Array of [QuickResponseQueryField](API_amazon-q-connect_QuickResponseQueryField.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

## See Also
<a name="API_amazon-q-connect_QuickResponseSearchExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QuickResponseSearchExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QuickResponseSearchExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QuickResponseSearchExpression)
