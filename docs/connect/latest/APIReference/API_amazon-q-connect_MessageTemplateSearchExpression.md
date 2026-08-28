---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_MessageTemplateSearchExpression.html
---

# MessageTemplateSearchExpression
<a name="API_amazon-q-connect_MessageTemplateSearchExpression"></a>

The search expression of the message template.

## Contents
<a name="API_amazon-q-connect_MessageTemplateSearchExpression_Contents"></a>

 ** filters **   <a name="connect-Type-amazon-q-connect_MessageTemplateSearchExpression-filters"></a>
The configuration of filtering rules applied to message template query results.
Type: Array of [MessageTemplateFilterField](API_amazon-q-connect_MessageTemplateFilterField.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** orderOnField **   <a name="connect-Type-amazon-q-connect_MessageTemplateSearchExpression-orderOnField"></a>
The message template attribute fields on which the query results are ordered.
Type: [MessageTemplateOrderField](API_amazon-q-connect_MessageTemplateOrderField.md) object
Required: No

 ** queries **   <a name="connect-Type-amazon-q-connect_MessageTemplateSearchExpression-queries"></a>
The message template query expressions.
Type: Array of [MessageTemplateQueryField](API_amazon-q-connect_MessageTemplateQueryField.md) objects
Array Members: Minimum number of 0 items. Maximum number of 4 items.
Required: No

## See Also
<a name="API_amazon-q-connect_MessageTemplateSearchExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateSearchExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateSearchExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateSearchExpression)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
