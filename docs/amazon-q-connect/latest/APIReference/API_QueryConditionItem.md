---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QueryConditionItem.html
---

# QueryConditionItem
<a name="API_amazon-q-connect_QueryConditionItem"></a>

The condition for the query.

## Contents
<a name="API_amazon-q-connect_QueryConditionItem_Contents"></a>

 ** comparator **   <a name="connect-Type-amazon-q-connect_QueryConditionItem-comparator"></a>
The comparison operator for query condition to query on.
Type: String
Valid Values: `EQUALS`
Required: Yes

 ** field **   <a name="connect-Type-amazon-q-connect_QueryConditionItem-field"></a>
 The name of the field for query condition to query on.
Type: String
Valid Values: `RESULT_TYPE`
Required: Yes

 ** value **   <a name="connect-Type-amazon-q-connect_QueryConditionItem-value"></a>
The value for the query condition to query on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## See Also
<a name="API_amazon-q-connect_QueryConditionItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QueryConditionItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QueryConditionItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QueryConditionItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
