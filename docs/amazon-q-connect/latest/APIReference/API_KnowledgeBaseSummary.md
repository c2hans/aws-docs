---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_KnowledgeBaseSummary.html
---

# KnowledgeBaseSummary
<a name="API_amazon-q-connect_KnowledgeBaseSummary"></a>

Summary information about the knowledge base.

## Contents
<a name="API_amazon-q-connect_KnowledgeBaseSummary_Contents"></a>

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** knowledgeBaseType **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-knowledgeBaseType"></a>
The type of knowledge base.
Type: String
Valid Values: `EXTERNAL | CUSTOM | QUICK_RESPONSES | MESSAGE_TEMPLATES | MANAGED`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-name"></a>
The name of the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-status"></a>
The status of the knowledge base summary.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: Yes

 ** description **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-description"></a>
The description of the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** renderingConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-renderingConfiguration"></a>
Information about how to render the content.
Type: [RenderingConfiguration](API_amazon-q-connect_RenderingConfiguration.md) object
Required: No

 ** serverSideEncryptionConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-serverSideEncryptionConfiguration"></a>
The configuration information for the customer managed key used for encryption.
This KMS key must have a policy that allows `kms:CreateGrant`, `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey*` permissions to the IAM identity using the key to invoke Amazon Q in Connect.
For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html).
Type: [ServerSideEncryptionConfiguration](API_amazon-q-connect_ServerSideEncryptionConfiguration.md) object
Required: No

 ** sourceConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-sourceConfiguration"></a>
Configuration information about the external data source.
Type: [SourceConfiguration](API_amazon-q-connect_SourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** vectorIngestionConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseSummary-vectorIngestionConfiguration"></a>
Contains details about how to ingest the documents in a data source.
Type: [VectorIngestionConfiguration](API_amazon-q-connect_VectorIngestionConfiguration.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_KnowledgeBaseSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/KnowledgeBaseSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/KnowledgeBaseSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/KnowledgeBaseSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
