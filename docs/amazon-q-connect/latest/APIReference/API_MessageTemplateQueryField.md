---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_MessageTemplateQueryField.html
---

# MessageTemplateQueryField
<a name="API_amazon-q-connect_MessageTemplateQueryField"></a>

The message template fields to query message templates by. The following is the list of supported field names:
+ name
+ description

## Contents
<a name="API_amazon-q-connect_MessageTemplateQueryField_Contents"></a>

 ** name **   <a name="connect-Type-amazon-q-connect_MessageTemplateQueryField-name"></a>
The name of the attribute to query the message templates by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** operator **   <a name="connect-Type-amazon-q-connect_MessageTemplateQueryField-operator"></a>
The operator to use for matching attribute field values in the query.
Type: String
Valid Values: `CONTAINS | CONTAINS_AND_PREFIX`
Required: Yes

 ** values **   <a name="connect-Type-amazon-q-connect_MessageTemplateQueryField-values"></a>
The values of the attribute to query the message templates by.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

 ** allowFuzziness **   <a name="connect-Type-amazon-q-connect_MessageTemplateQueryField-allowFuzziness"></a>
Whether the query expects only exact matches on the attribute field values. The results of the query will only include exact matches if this parameter is set to false.
Type: Boolean
Required: No

 ** priority **   <a name="connect-Type-amazon-q-connect_MessageTemplateQueryField-priority"></a>
The importance of the attribute field when calculating query result relevancy scores. The value set for this parameter affects the ordering of search results.
Type: String
Valid Values: `HIGH | MEDIUM | LOW`
Required: No

## See Also
<a name="API_amazon-q-connect_MessageTemplateQueryField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateQueryField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateQueryField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateQueryField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
