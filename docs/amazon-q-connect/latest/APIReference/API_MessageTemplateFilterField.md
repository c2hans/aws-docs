---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_MessageTemplateFilterField.html
---

# MessageTemplateFilterField
<a name="API_amazon-q-connect_MessageTemplateFilterField"></a>

The message template fields to filter the message template query results by. The following is the list of supported field names:
+ name
+ description
+ channel
+ channelSubtype
+ language
+ qualifier
+ createdTime
+ lastModifiedTime
+ lastModifiedBy
+ groupingConfiguration.criteria
+ groupingConfiguration.values

## Contents
<a name="API_amazon-q-connect_MessageTemplateFilterField_Contents"></a>

 ** name **   <a name="connect-Type-amazon-q-connect_MessageTemplateFilterField-name"></a>
The name of the attribute field to filter the message templates by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** operator **   <a name="connect-Type-amazon-q-connect_MessageTemplateFilterField-operator"></a>
The operator to use for filtering.
Type: String
Valid Values: `EQUALS | PREFIX`
Required: Yes

 ** includeNoExistence **   <a name="connect-Type-amazon-q-connect_MessageTemplateFilterField-includeNoExistence"></a>
Whether to treat null value as a match for the attribute field.
Type: Boolean
Required: No

 ** values **   <a name="connect-Type-amazon-q-connect_MessageTemplateFilterField-values"></a>
The values of attribute field to filter the message template by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## See Also
<a name="API_amazon-q-connect_MessageTemplateFilterField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateFilterField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateFilterField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateFilterField)
