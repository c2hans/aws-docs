---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_DataSetExportTask.html
---

# DataSetExportTask
<a name="API_DataSetExportTask"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Contains information about a data set export task.

## Contents
<a name="API_DataSetExportTask_Contents"></a>

 ** status **   <a name="m2-Type-DataSetExportTask-status"></a>
The status of the data set export task.
Type: String
Valid Values: `Creating | Running | Completed | Failed`
Required: Yes

 ** summary **   <a name="m2-Type-DataSetExportTask-summary"></a>
A summary of the data set export task.
Type: [DataSetExportSummary](API_DataSetExportSummary.md) object
Required: Yes

 ** taskId **   <a name="m2-Type-DataSetExportTask-taskId"></a>
The identifier of the data set export task.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** statusReason **   <a name="m2-Type-DataSetExportTask-statusReason"></a>
If dataset exports failed, the failure reason will show here.
Type: String
Required: No

## See Also
<a name="API_DataSetExportTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/DataSetExportTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/DataSetExportTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/DataSetExportTask)
