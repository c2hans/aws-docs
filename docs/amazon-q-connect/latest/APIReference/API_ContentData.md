---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ContentData.html
---

# ContentData
<a name="API_amazon-q-connect_ContentData"></a>

Information about the content.

## Contents
<a name="API_amazon-q-connect_ContentData_Contents"></a>

 ** contentArn **   <a name="connect-Type-amazon-q-connect_ContentData-contentArn"></a>
The Amazon Resource Name (ARN) of the content.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** contentId **   <a name="connect-Type-amazon-q-connect_ContentData-contentId"></a>
The identifier of the content.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** contentType **   <a name="connect-Type-amazon-q-connect_ContentData-contentType"></a>
The media type of the content.
Type: String
Pattern: `(text/(plain|html|csv))|(application/(pdf|vnd\.openxmlformats-officedocument\.wordprocessingml\.document))|(application/x\.wisdom-json;source=(salesforce|servicenow|zendesk))`
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_ContentData-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_ContentData-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** metadata **   <a name="connect-Type-amazon-q-connect_ContentData-metadata"></a>
A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_ContentData-name"></a>
The name of the content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** revisionId **   <a name="connect-Type-amazon-q-connect_ContentData-revisionId"></a>
The identifier of the content revision.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_ContentData-status"></a>
The status of the content.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED | UPDATE_FAILED`
Required: Yes

 ** title **   <a name="connect-Type-amazon-q-connect_ContentData-title"></a>
The title of the content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** url **   <a name="connect-Type-amazon-q-connect_ContentData-url"></a>
The URL of the content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** urlExpiry **   <a name="connect-Type-amazon-q-connect_ContentData-urlExpiry"></a>
The expiration time of the URL as an epoch timestamp.
Type: Timestamp
Required: Yes

 ** linkOutUri **   <a name="connect-Type-amazon-q-connect_ContentData-linkOutUri"></a>
The URI of the content.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_ContentData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_ContentData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ContentData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ContentData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ContentData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
