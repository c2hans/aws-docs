---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_BatchDeleteImportDataError.html
---

# BatchDeleteImportDataError
<a name="API_BatchDeleteImportDataError"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Error messages returned for each import task that you deleted as a response for this command.

## Contents
<a name="API_BatchDeleteImportDataError_Contents"></a>

 ** errorCode **   <a name="DiscServ-Type-BatchDeleteImportDataError-errorCode"></a>
The type of error that occurred for a specific import task.
Type: String
Valid Values: `NOT_FOUND | INTERNAL_SERVER_ERROR | OVER_LIMIT`
Required: No

 ** errorDescription **   <a name="DiscServ-Type-BatchDeleteImportDataError-errorDescription"></a>
The description of the error that occurred for a specific import task.
Type: String
Required: No

 ** importTaskId **   <a name="DiscServ-Type-BatchDeleteImportDataError-importTaskId"></a>
The unique import ID associated with the error that occurred.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `^import-task-[a-fA-F0-9]{32}$`
Required: No

## See Also
<a name="API_BatchDeleteImportDataError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/BatchDeleteImportDataError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/BatchDeleteImportDataError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/BatchDeleteImportDataError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
