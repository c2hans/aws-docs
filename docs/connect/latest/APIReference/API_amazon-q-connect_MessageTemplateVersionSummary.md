---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_MessageTemplateVersionSummary.html
---

# MessageTemplateVersionSummary
<a name="API_amazon-q-connect_MessageTemplateVersionSummary"></a>

The summary of the message template version.

## Contents
<a name="API_amazon-q-connect_MessageTemplateVersionSummary_Contents"></a>

 ** channelSubtype **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-channelSubtype"></a>
The channel subtype this message template applies to.
Type: String
Valid Values: `EMAIL | SMS | WHATSAPP | PUSH`
Required: Yes

 ** isActive **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-isActive"></a>
Whether the version of the message template is activated.
Type: Boolean
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** messageTemplateArn **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-messageTemplateArn"></a>
The Amazon Resource Name (ARN) of the message template.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** messageTemplateId **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-messageTemplateId"></a>
The identifier of the message template.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-name"></a>
The name of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** versionNumber **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-versionNumber"></a>
The version number of the message template version.
Type: Long
Valid Range: Minimum value of 1.
Required: Yes

 ** channel **   <a name="connect-Type-amazon-q-connect_MessageTemplateVersionSummary-channel"></a>
The channel of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

## See Also
<a name="API_amazon-q-connect_MessageTemplateVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
