---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QuickResponseQueryField.html
---

# QuickResponseQueryField
<a name="API_amazon-q-connect_QuickResponseQueryField"></a>

The quick response fields to query quick responses by.

The following is the list of supported field names.
+ content
+ name
+ description
+ shortcutKey

## Contents
<a name="API_amazon-q-connect_QuickResponseQueryField_Contents"></a>

 ** name **   <a name="connect-Type-amazon-q-connect_QuickResponseQueryField-name"></a>
The name of the attribute to query the quick responses by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** operator **   <a name="connect-Type-amazon-q-connect_QuickResponseQueryField-operator"></a>
The operator to use for matching attribute field values in the query.
Type: String
Valid Values: `CONTAINS | CONTAINS_AND_PREFIX`
Required: Yes

 ** values **   <a name="connect-Type-amazon-q-connect_QuickResponseQueryField-values"></a>
The values of the attribute to query the quick responses by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** allowFuzziness **   <a name="connect-Type-amazon-q-connect_QuickResponseQueryField-allowFuzziness"></a>
Whether the query expects only exact matches on the attribute field values. The results of the query will only include exact matches if this parameter is set to false.
Type: Boolean
Required: No

 ** priority **   <a name="connect-Type-amazon-q-connect_QuickResponseQueryField-priority"></a>
The importance of the attribute field when calculating query result relevancy scores. The value set for this parameter affects the ordering of search results.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

## See Also
<a name="API_amazon-q-connect_QuickResponseQueryField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QuickResponseQueryField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QuickResponseQueryField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QuickResponseQueryField)
