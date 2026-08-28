---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ImportJobData.html
---

# ImportJobData
<a name="API_amazon-q-connect_ImportJobData"></a>

Summary information about the import job.

## Contents
<a name="API_amazon-q-connect_ImportJobData_Contents"></a>

 ** createdTime **   <a name="connect-Type-amazon-q-connect_ImportJobData-createdTime"></a>
The timestamp when the import job was created.
Type: Timestamp
Required: Yes

 ** importJobId **   <a name="connect-Type-amazon-q-connect_ImportJobData-importJobId"></a>
The identifier of the import job.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** importJobType **   <a name="connect-Type-amazon-q-connect_ImportJobData-importJobType"></a>
The type of the import job.
Type: String
Valid Values: `QUICK_RESPONSES`
Required: Yes

 ** knowledgeBaseArn **   <a name="connect-Type-amazon-q-connect_ImportJobData-knowledgeBaseArn"></a>
The Amazon Resource Name (ARN) of the knowledge base.
Type: String
Pattern: `arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** knowledgeBaseId **   <a name="connect-Type-amazon-q-connect_ImportJobData-knowledgeBaseId"></a>
The identifier of the knowledge base.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** lastModifiedTime **   <a name="connect-Type-amazon-q-connect_ImportJobData-lastModifiedTime"></a>
The timestamp when the import job data was last modified.
Type: Timestamp
Required: Yes

 ** status **   <a name="connect-Type-amazon-q-connect_ImportJobData-status"></a>
The status of the import job.
Type: String
Valid Values: `START_IN_PROGRESS | FAILED | COMPLETE | DELETE_IN_PROGRESS | DELETE_FAILED | DELETED`
Required: Yes

 ** uploadId **   <a name="connect-Type-amazon-q-connect_ImportJobData-uploadId"></a>
A pointer to the uploaded asset. This value is returned by [StartContentUpload](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1200.
Required: Yes

 ** url **   <a name="connect-Type-amazon-q-connect_ImportJobData-url"></a>
The download link to the resource file that is uploaded to the import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** urlExpiry **   <a name="connect-Type-amazon-q-connect_ImportJobData-urlExpiry"></a>
The expiration time of the URL as an epoch timestamp.
Type: Timestamp
Required: Yes

 ** externalSourceConfiguration **   <a name="connect-Type-amazon-q-connect_ImportJobData-externalSourceConfiguration"></a>
The configuration information of the external data source.
Type: [ExternalSourceConfiguration](API_amazon-q-connect_ExternalSourceConfiguration.md) object
Required: No

 ** failedRecordReport **   <a name="connect-Type-amazon-q-connect_ImportJobData-failedRecordReport"></a>
The link to download the information of resource data that failed to be imported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** metadata **   <a name="connect-Type-amazon-q-connect_ImportJobData-metadata"></a>
The metadata fields of the imported Amazon Q in Connect resources.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 10 items.
Key Length Constraints: Minimum length of 1. Maximum length of 4096.
Value Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_amazon-q-connect_ImportJobData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ImportJobData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ImportJobData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ImportJobData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
