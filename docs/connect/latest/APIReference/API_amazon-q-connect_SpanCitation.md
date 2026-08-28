---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SpanCitation.html
---

# SpanCitation
<a name="API_amazon-q-connect_SpanCitation"></a>

A citation that spans a specific range of text.

## Contents
<a name="API_amazon-q-connect_SpanCitation_Contents"></a>

 ** contentId **   <a name="connect-Type-amazon-q-connect_SpanCitation-contentId"></a>
The identifier of the content being cited in the span.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_SpanCitation-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base containing the cited content.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: No

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_SpanCitation-knowledgeBaseId"></a>
The identifier of the knowledge base containing the cited content.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** title **   <a name="connect-Type-amazon-q-connect_SpanCitation-title"></a>
The title of the content being cited in the span.
Type: String
Required: No

## See Also
<a name="API_amazon-q-connect_SpanCitation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SpanCitation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SpanCitation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SpanCitation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
