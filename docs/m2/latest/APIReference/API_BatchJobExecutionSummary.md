---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_BatchJobExecutionSummary.html
---

# BatchJobExecutionSummary
<a name="API_BatchJobExecutionSummary"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

A subset of the possible batch job attributes. Used in the batch job list.

## Contents
<a name="API_BatchJobExecutionSummary_Contents"></a>

 ** applicationId **   <a name="m2-Type-BatchJobExecutionSummary-applicationId"></a>
The unique identifier of the application that hosts this batch job.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** executionId **   <a name="m2-Type-BatchJobExecutionSummary-executionId"></a>
The unique identifier of this execution of the batch job.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** startTime **   <a name="m2-Type-BatchJobExecutionSummary-startTime"></a>
The timestamp when a particular batch job execution started.
Type: Timestamp
Required: Yes

 ** status **   <a name="m2-Type-BatchJobExecutionSummary-status"></a>
The status of a particular batch job execution.
Type: String
Valid Values: `Submitting | Holding | Dispatching | Running | Cancelling | Cancelled | Succeeded | Failed | Purged | Succeeded With Warning`
Required: Yes

 ** batchJobIdentifier **   <a name="m2-Type-BatchJobExecutionSummary-batchJobIdentifier"></a>
The unique identifier of this batch job.
Type: [BatchJobIdentifier](API_BatchJobIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** endTime **   <a name="m2-Type-BatchJobExecutionSummary-endTime"></a>
The timestamp when this batch job execution ended.
Type: Timestamp
Required: No

 ** jobId **   <a name="m2-Type-BatchJobExecutionSummary-jobId"></a>
The unique identifier of a particular batch job.
Type: String
Pattern: `\S{1,100}`
Required: No

 ** jobName **   <a name="m2-Type-BatchJobExecutionSummary-jobName"></a>
The name of a particular batch job.
Type: String
Pattern: `\S{1,100}`
Required: No

 ** jobType **   <a name="m2-Type-BatchJobExecutionSummary-jobType"></a>
The type of a particular batch job execution.
Type: String
Valid Values: `VSE | JES2 | JES3`
Required: No

 ** returnCode **   <a name="m2-Type-BatchJobExecutionSummary-returnCode"></a>
The batch job return code from either the Blu Age or Micro Focus runtime engines. For more information, see [Batch return codes](https://www.ibm.com/docs/en/was/8.5.5?topic=model-batch-return-codes) in the *IBM WebSphere Application Server* documentation.
Type: String
Required: No

## See Also
<a name="API_BatchJobExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/BatchJobExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/BatchJobExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/BatchJobExecutionSummary)
