---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_ImportJobSummary.html
---

# ImportJobSummary
<a name="API_amazon-q-connect_ImportJobSummary"></a>

Summary information about the import job.

## Contents
<a name="API_amazon-q-connect_ImportJobSummary_Contents"></a>

 ** createdTime **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-createdTime"></a>
The timestamp when the import job was created.
Type: Timestamp
Required: Yes

 ** importJobId **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-importJobId"></a>
The identifier of the import job.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** importJobType **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-importJobType"></a>
The type of import job.
Type: String
Valid Values: `QUICK_RESPONSES`
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedTime **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-lastModifiedTime"></a>
The timestamp when the import job was last modified.
Type: Timestamp
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-status"></a>
The status of the import job.
Type: String
Valid Values: `START_IN_PROGRESS | FAILED | COMPLETE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: Yes

 ** uploadId **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-uploadId"></a>
A pointer to the uploaded asset. This value is returned by [StartContentUpload](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1200.
Required: Yes

 ** externalSourceConfiguration **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-externalSourceConfiguration"></a>
The configuration information of the external source that the resource data are imported from.
Type: [ExternalSourceConfiguration](API_amazon-q-connect_ExternalSourceConfiguration.md) object
Required: No

 ** metadata **   <a name="connect-Type-amazon-q-connect_ImportJobSummary-metadata"></a>
The metadata fields of the imported Amazon Q in Connect resources.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_ImportJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ImportJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ImportJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ImportJobSummary)
