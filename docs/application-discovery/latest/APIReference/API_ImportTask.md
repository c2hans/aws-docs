---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_ImportTask.html
---

# ImportTask
<a name="API_ImportTask"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

An array of information related to the import task request that includes status information, times, IDs, the Amazon S3 Object URL for the import file, and more.

## Contents
<a name="API_ImportTask_Contents"></a>

 ** applicationImportFailure **   <a name="DiscServ-Type-ImportTask-applicationImportFailure"></a>
The total number of application records in the import file that failed to be imported.
Type: Integer
Required: No

 ** applicationImportSuccess **   <a name="DiscServ-Type-ImportTask-applicationImportSuccess"></a>
The total number of application records in the import file that were successfully imported.
Type: Integer
Required: No

 ** clientRequestToken **   <a name="DiscServ-Type-ImportTask-clientRequestToken"></a>
A unique token used to prevent the same import request from occurring more than once. If you didn't provide a token, a token was automatically generated when the import task request was sent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** errorsAndFailedEntriesZip **   <a name="DiscServ-Type-ImportTask-errorsAndFailedEntriesZip"></a>
A link to a compressed archive folder (in the ZIP format) that contains an error log and a file of failed records. You can use these two files to quickly identify records that failed, why they failed, and correct those records. Afterward, you can upload the corrected file to your Amazon S3 bucket and create another import task request.
This field also includes authorization information so you can confirm the authenticity of the compressed archive before you download it.
If some records failed to be imported we recommend that you correct the records in the failed entries file and then imports that failed entries file. This prevents you from having to correct and update the larger original file and attempt importing it again.
Type: String
Required: No

 ** fileClassification **   <a name="DiscServ-Type-ImportTask-fileClassification"></a>
The type of file detected by the import task.
Type: String
Valid Values: `MODELIZEIT_EXPORT | RVTOOLS_EXPORT | VMWARE_NSX_EXPORT | IMPORT_TEMPLATE`
Required: No

 ** importCompletionTime **   <a name="DiscServ-Type-ImportTask-importCompletionTime"></a>
The time that the import task request finished, presented in the Unix time stamp format.
Type: Timestamp
Required: No

 ** importDeletedTime **   <a name="DiscServ-Type-ImportTask-importDeletedTime"></a>
The time that the import task request was deleted, presented in the Unix time stamp format.
Type: Timestamp
Required: No

 ** importRequestTime **   <a name="DiscServ-Type-ImportTask-importRequestTime"></a>
The time that the import task request was made, presented in the Unix time stamp format.
Type: Timestamp
Required: No

 ** importTaskId **   <a name="DiscServ-Type-ImportTask-importTaskId"></a>
The unique ID for a specific import task. These IDs aren't globally unique, but they are unique within an AWS account.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^import-task-[a-fA-F0-9]{32}$`
Required: No

 ** importUrl **   <a name="DiscServ-Type-ImportTask-importUrl"></a>
The URL for your import file that you've uploaded to Amazon S3.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4000.
Pattern: `\S+://\S+/[\s\S]*\S[\s\S]*`
Required: No

 ** name **   <a name="DiscServ-Type-ImportTask-name"></a>
A descriptive name for an import task. You can use this name to filter future requests related to this import task, such as identifying applications and servers that were included in this import task. We recommend that you use a meaningful name for each import task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** serverImportFailure **   <a name="DiscServ-Type-ImportTask-serverImportFailure"></a>
The total number of server records in the import file that failed to be imported.
Type: Integer
Required: No

 ** serverImportSuccess **   <a name="DiscServ-Type-ImportTask-serverImportSuccess"></a>
The total number of server records in the import file that were successfully imported.
Type: Integer
Required: No

 ** status **   <a name="DiscServ-Type-ImportTask-status"></a>
The status of the import task. An import can have the status of `IMPORT_COMPLETE` and still have some records fail to import from the overall request. More information can be found in the downloadable archive defined in the `errorsAndFailedEntriesZip` field, or in the Migration Hub management console.
Type: String
Valid Values: `IMPORT_IN_PROGRESS | IMPORT_COMPLETE | IMPORT_COMPLETE_WITH_ERRORS | IMPORT_FAILED | IMPORT_FAILED_SERVER_LIMIT_EXCEEDED | IMPORT_FAILED_RECORD_LIMIT_EXCEEDED | IMPORT_FAILED_UNSUPPORTED_FILE_TYPE | DELETE_IN_PROGRESS | DELETE_COMPLETE | DELETE_FAILED | DELETE_FAILED_LIMIT_EXCEEDED | INTERNAL_ERROR`
Required: No

## See Also
<a name="API_ImportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/ImportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/ImportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/ImportTask)
