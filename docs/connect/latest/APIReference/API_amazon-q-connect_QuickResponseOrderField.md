---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QuickResponseOrderField.html
---

# QuickResponseOrderField
<a name="API_amazon-q-connect_QuickResponseOrderField"></a>

The quick response fields to order the quick response query results by.

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
<a name="API_amazon-q-connect_QuickResponseOrderField_Contents"></a>

 ** name **   <a name="connect-Type-amazon-q-connect_QuickResponseOrderField-name"></a>
The name of the attribute to order the quick response query results by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** order **   <a name="connect-Type-amazon-q-connect_QuickResponseOrderField-order"></a>
The order at which the quick responses are sorted by.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_amazon-q-connect_QuickResponseOrderField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QuickResponseOrderField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QuickResponseOrderField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QuickResponseOrderField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
