---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QuickResponseFilterField.html
---

# QuickResponseFilterField
<a name="API_amazon-q-connect_QuickResponseFilterField"></a>

The quick response fields to filter the quick response query results by.

The following is the list of supported field names.
+ name
+ description
+ shortcutKey
+ isActive
+ channels
+ language
+ contentType
+ createdTime
+ lastModifiedTime
+ lastModifiedBy
+ groupingConfiguration.criteria
+ groupingConfiguration.values

## Contents
<a name="API_amazon-q-connect_QuickResponseFilterField_Contents"></a>

 ** name **   <a name="connect-Type-amazon-q-connect_QuickResponseFilterField-name"></a>
The name of the attribute field to filter the quick responses by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** operator **   <a name="connect-Type-amazon-q-connect_QuickResponseFilterField-operator"></a>
The operator to use for filtering.
Type: String
Valid Values: `EQUALS | PREFIX`
Required: Yes

 ** includeNoExistence **   <a name="connect-Type-amazon-q-connect_QuickResponseFilterField-includeNoExistence"></a>
Whether to treat null value as a match for the attribute field.
Type: Boolean
Required: No

 ** values **   <a name="connect-Type-amazon-q-connect_QuickResponseFilterField-values"></a>
The values of attribute field to filter the quick response by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_amazon-q-connect_QuickResponseFilterField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QuickResponseFilterField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QuickResponseFilterField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QuickResponseFilterField)
