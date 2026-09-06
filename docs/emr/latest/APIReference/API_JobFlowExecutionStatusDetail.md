---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_JobFlowExecutionStatusDetail.html
---

# JobFlowExecutionStatusDetail
<a name="API_JobFlowExecutionStatusDetail"></a>

Describes the status of the cluster (job flow).

## Contents
<a name="API_JobFlowExecutionStatusDetail_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-JobFlowExecutionStatusDetail-CreationDateTime"></a>
The creation date and time of the job flow.
Type: Timestamp
Required: Yes

 ** State **   <a name="EMR-Type-JobFlowExecutionStatusDetail-State"></a>
The state of the job flow.
Type: String
Valid Values: `STARTING | BOOTSTRAPPING | RUNNING | WAITING | SHUTTING_DOWN | TERMINATED | COMPLETED | FAILED`
Required: Yes

 ** EndDateTime **   <a name="EMR-Type-JobFlowExecutionStatusDetail-EndDateTime"></a>
The completion date and time of the job flow.
Type: Timestamp
Required: No

 ** LastStateChangeReason **   <a name="EMR-Type-JobFlowExecutionStatusDetail-LastStateChangeReason"></a>
Description of the job flow last changed state.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10280.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-JobFlowExecutionStatusDetail-ReadyDateTime"></a>
The date and time when the job flow was ready to start running bootstrap actions.
Type: Timestamp
Required: No

 ** StartDateTime **   <a name="EMR-Type-JobFlowExecutionStatusDetail-StartDateTime"></a>
The start date and time of the job flow.
Type: Timestamp
Required: No

## See Also
<a name="API_JobFlowExecutionStatusDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/JobFlowExecutionStatusDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/JobFlowExecutionStatusDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/JobFlowExecutionStatusDetail)
