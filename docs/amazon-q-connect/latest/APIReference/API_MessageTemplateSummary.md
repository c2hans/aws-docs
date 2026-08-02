---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_MessageTemplateSummary.html
---

# MessageTemplateSummary
<a name="API_amazon-q-connect_MessageTemplateSummary"></a>

The summary of the message template.

## Contents
<a name="API_amazon-q-connect_MessageTemplateSummary_Contents"></a>

 ** channelSubtype **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-channelSubtype"></a>
The channel subtype this message template applies to.
Type: String
Valid Values: `EMAIL | SMS | WHATSAPP | PUSH`
Required: Yes

 ** createdTime **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-createdTime"></a>
The timestamp when the message template was created.
Type: Timestamp
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedBy **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-lastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the message template data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: Yes

 ** lastModifiedTime **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-lastModifiedTime"></a>
The timestamp when the message template data was last modified.
Type: Timestamp
Required: Yes

 ** messageTemplateArn **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-messageTemplateArn"></a>
The Amazon Resource Name (ARN) of the message template.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** messageTemplateId **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-messageTemplateId"></a>
The identifier of the message template.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-name"></a>
The name of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** activeVersionNumber **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-activeVersionNumber"></a>
The version number of the message template version that is activated.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** channel **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-channel"></a>
The channel this message template applies to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-description"></a>
The description of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** sourceConfiguration **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-sourceConfiguration"></a>
The container of message template source configuration.
Type: [MessageTemplateSourceConfiguration](API_amazon-q-connect_MessageTemplateSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_MessageTemplateSummary-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_MessageTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateSummary)
