---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_Sort.html
---

# Sort
<a name="API_Sort"></a>

A structure that defines the field name to sort by and a sort order.

## Contents
<a name="API_Sort_Contents"></a>

 ** FieldName **   <a name="connect-Type-Sort-FieldName"></a>
The name of the field on which to sort.
Type: String
Valid Values: `INITIATION_TIMESTAMP | SCHEDULED_TIMESTAMP | CONNECTED_TO_AGENT_TIMESTAMP | DISCONNECT_TIMESTAMP | INITIATION_METHOD | CHANNEL | EXPIRY_TIMESTAMP`
Required: Yes

 ** Order **   <a name="connect-Type-Sort-Order"></a>
An ascending or descending sort.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: Yes

## See Also
<a name="API_Sort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/Sort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/Sort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/Sort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
