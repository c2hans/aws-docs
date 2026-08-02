---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_KnowledgeBaseData.html
---

# KnowledgeBaseData
<a name="API_amazon-q-connect_KnowledgeBaseData"></a>

Information about the knowledge base.

## Contents
<a name="API_amazon-q-connect_KnowledgeBaseData_Contents"></a>

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** knowledgeBaseType **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-knowledgeBaseType"></a>
The type of knowledge base.
Type: String
Valid Values: `EXTERNAL | CUSTOM | QUICK_RESPONSES | MESSAGE_TEMPLATES | MANAGED`
Required: Yes

 ** name **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-name"></a>
The name of the knowledge base.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-status"></a>
The status of the knowledge base.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_FAILED | ACTIVE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: Yes

 ** description **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-description"></a>
The description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\s_.,-]+.*`
Required: No

 ** ingestionFailureReasons **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-ingestionFailureReasons"></a>
List of failure reasons on ingestion per file.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** ingestionStatus **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-ingestionStatus"></a>
Status of ingestion on data source.
Type: String
Valid Values: `SYNC_FAILED | SYNCING_IN_PROGRESS | SYNC_SUCCESS | CREATE_IN_PROGRESS`
Required: No

 ** lastContentModificationTime **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-lastContentModificationTime"></a>
An epoch timestamp indicating the most recent content modification inside the knowledge base. If no content exists in a knowledge base, this value is unset.
Type: Timestamp
Required: No

 ** renderingConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-renderingConfiguration"></a>
Information about how to render the content.
Type: [RenderingConfiguration](API_amazon-q-connect_RenderingConfiguration.md) object
Required: No

 ** serverSideEncryptionConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-serverSideEncryptionConfiguration"></a>
The configuration information for the customer managed key used for encryption.
This KMS key must have a policy that allows `kms:CreateGrant`, `kms:DescribeKey`, `kms:Decrypt`, and `kms:GenerateDataKey*` permissions to the IAM identity using the key to invoke Amazon Q in Connect.
For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html).
Type: [ServerSideEncryptionConfiguration](API_amazon-q-connect_ServerSideEncryptionConfiguration.md) object
Required: No

 ** sourceConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-sourceConfiguration"></a>
Source configuration information about the knowledge base.
Type: [SourceConfiguration](API_amazon-q-connect_SourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** vectorIngestionConfiguration **   <a name="connect-Type-amazon-q-connect_KnowledgeBaseData-vectorIngestionConfiguration"></a>
Contains details about how to ingest the documents in a data source.
Type: [VectorIngestionConfiguration](API_amazon-q-connect_VectorIngestionConfiguration.md) object
Required: No

## See Also
<a name="API_amazon-q-connect_KnowledgeBaseData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/KnowledgeBaseData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/KnowledgeBaseData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/KnowledgeBaseData)
