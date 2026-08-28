---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_IndexStatus.html
---

# IndexStatus
<a name="API_IndexStatus"></a>

Contains information about the status of a Resource Explorer index operation in a specific Region.

## Contents
<a name="API_IndexStatus_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ErrorDetails **   <a name="resourceexplorer-Type-IndexStatus-ErrorDetails"></a>
Details about any error that occurred during the index operation.
Type: [ErrorDetails](API_ErrorDetails.md) object
Required: No

 ** Index **   <a name="resourceexplorer-Type-IndexStatus-Index"></a>
An index is the data store used by AWS Resource Explorer to hold information about your AWS resources that the service discovers. Creating an index in an AWS Region turns on Resource Explorer and lets it discover your resources.
By default, an index is *local*, meaning that it contains information about resources in only the same Region as the index. However, you can promote the index of one Region in the account by calling [UpdateIndexType](API_UpdateIndexType.md) to convert it into an aggregator index. The aggregator index receives a replicated copy of the index information from all other Regions where Resource Explorer is turned on. This allows search operations in that Region to return results from all Regions in the account.
Type: [Index](API_Index.md) object
Required: No

 ** Status **   <a name="resourceexplorer-Type-IndexStatus-Status"></a>
The current status of the index operation. Valid values are `SUCCEEDED`, `FAILED`, `IN_PROGRESS`, or `SKIPPED`.
Type: String
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS | SKIPPED`
Required: No

## See Also
<a name="API_IndexStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/IndexStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/IndexStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/IndexStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
