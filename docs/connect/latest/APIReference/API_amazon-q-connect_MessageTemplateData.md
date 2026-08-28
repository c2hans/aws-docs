---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_MessageTemplateData.html
---

# MessageTemplateData
<a name="API_amazon-q-connect_MessageTemplateData"></a>

The data of a message template.

## Contents
<a name="API_amazon-q-connect_MessageTemplateData_Contents"></a>

 ** channelSubtype **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-channelSubtype"></a>
The channel subtype this message template applies to.
Type: String
Valid Values: `EMAIL | SMS | WHATSAPP | PUSH`
Required: Yes

 ** createdTime **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-createdTime"></a>
The timestamp when the message template was created.
Type: Timestamp
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedBy **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-lastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the message template data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[a-z-]+?:[a-z-]+?:[a-z0-9-]*?:([0-9]{12})?:[a-zA-Z0-9-:/]+`
Required: Yes

 ** lastModifiedTime **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-lastModifiedTime"></a>
The timestamp when the message template data was last modified.
Type: Timestamp
Required: Yes

 ** messageTemplateArn **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-messageTemplateArn"></a>
The Amazon Resource Name (ARN) of the message template.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** messageTemplateContentSha256 **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-messageTemplateContentSha256"></a>
The checksum value of the message template content that is referenced by the `$LATEST` qualifier. It can be returned in `MessageTemplateData` or `ExtendedMessageTemplateData`. It’s calculated by content, language, `defaultAttributes` and `Attachments` of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** messageTemplateId **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-messageTemplateId"></a>
The identifier of the message template.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-name"></a>
The name of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** attributeTypes **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-attributeTypes"></a>
The types of attributes that the message template contains.
Type: Array of strings
Valid Values: `SYSTEM | AGENT | CUSTOMER_PROFILE | CUSTOM`
Required: No

 ** channel **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-channel"></a>
The channel of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Required: No

 ** content **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-content"></a>
The content of the message template.
Type: [MessageTemplateContentProvider](API_amazon-q-connect_MessageTemplateContentProvider.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** defaultAttributes **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-defaultAttributes"></a>
An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.
Type: [MessageTemplateAttributes](API_amazon-q-connect_MessageTemplateAttributes.md) object
Required: No

 ** description **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-description"></a>
The description of the message template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** groupingConfiguration **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-groupingConfiguration"></a>
The configuration information of the grouping of Amazon Q in Connect users.
Type: [GroupingConfiguration](API_amazon-q-connect_GroupingConfiguration.md) object
Required: No

 ** language **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-language"></a>
The language code value for the language in which the quick response is written. The supported language codes include `de_DE`, `en_US`, `es_ES`, `fr_FR`, `id_ID`, `it_IT`, `ja_JP`, `ko_KR`, `pt_BR`, `zh_CN`, `zh_TW`
Type: String
Length Constraints: Minimum length of 2. Maximum length of 5.
Required: No

 ** sourceConfigurationSummary **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-sourceConfigurationSummary"></a>
The source configuration summary of the message template.
Type: [MessageTemplateSourceConfigurationSummary](API_amazon-q-connect_MessageTemplateSourceConfigurationSummary.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_MessageTemplateData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_amazon-q-connect_MessageTemplateData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/MessageTemplateData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/MessageTemplateData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/MessageTemplateData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
