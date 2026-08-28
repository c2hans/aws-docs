---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_QuickResponseSummary.html
---

# QuickResponseSummary
<a name="API_amazon-q-connect_QuickResponseSummary"></a>

The summary information about the quick response.

## Contents
<a name="API_amazon-q-connect_QuickResponseSummary_Contents"></a>

 ** contentType **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-contentType"></a>
The media type of the quick response content.
+ Use `application/x.quickresponse;format=plain` for quick response written in plain text.
+ Use `application/x.quickresponse;format=markdown` for quick response written in richtext.
Type: String
Pattern: `(application/x\.quickresponse;format=(plain|markdown))`
Required: Yes

 ** createdTime **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-createdTime"></a>
The timestamp when the quick response was created.
Type: Timestamp
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedTime **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-lastModifiedTime"></a>
The timestamp when the quick response summary was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-name"></a>
The name of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** quickResponseArn **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-quickResponseArn"></a>
The Amazon Resource Name (ARN) of the quick response.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** quickResponseId **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-quickResponseId"></a>
The identifier of the quick response.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-status"></a>
The resource status of the quick response.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | CREATED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** channels **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-channels"></a>
The Connect Customer contact channels this quick response applies to. The supported contact channel types include `Chat`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-description"></a>
The description of the quick response.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** isActive **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-isActive"></a>
Whether the quick response is active.
Type: Boolean
Required: No

 ** lastModifiedBy **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-lastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the quick response data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_QuickResponseSummary-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_QuickResponseSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/QuickResponseSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/QuickResponseSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/QuickResponseSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
