---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ContentReference.html
---

# ContentReference
<a name="API_amazon-q-connect_ContentReference"></a>

Reference information about the content.

## Contents
<a name="API_amazon-q-connect_ContentReference_Contents"></a>

 ** contentArn **   <a name="connect-Type-amazon-q-connect_ContentReference-contentArn"></a>
The Amazon Resource Name (ARN) of the content.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: No

 ** contentId **   <a name="connect-Type-amazon-q-connect_ContentReference-contentId"></a>
The identifier of the content.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_ContentReference-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: No

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_ContentReference-knowledgeBaseId"></a>
The identifier of the knowledge base. This should not be a QUICK\_RESPONSES type knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: No

 ** referenceType **   <a name="connect-Type-amazon-q-connect_ContentReference-referenceType"></a>
The type of reference content.
Type: String
Valid Values: `WEB_CRAWLER | KNOWLEDGE_BASE | BEDROCK_KB_S3 | BEDROCK_KB_WEB | BEDROCK_KB_CONFLUENCE | BEDROCK_KB_SALESFORCE | BEDROCK_KB_SHAREPOINT | BEDROCK_KB_KENDRA | BEDROCK_KB_CUSTOM_DOCUMENT | BEDROCK_KB_SQL`
Required: No

 ** sourceURL **   <a name="connect-Type-amazon-q-connect_ContentReference-sourceURL"></a>
The web URL of the source content.
Type: String
Required: No

## See Also
<a name="API_amazon-q-connect_ContentReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ContentReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ContentReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ContentReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
