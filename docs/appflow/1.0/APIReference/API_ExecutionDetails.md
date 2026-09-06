---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ExecutionDetails.html
---

# ExecutionDetails
<a name="API_ExecutionDetails"></a>

 Describes the details of the flow run, including the timestamp, status, and message.

## Contents
<a name="API_ExecutionDetails_Contents"></a>

 ** mostRecentExecutionMessage **   <a name="appflow-Type-ExecutionDetails-mostRecentExecutionMessage"></a>
 Describes the details of the most recent flow run.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `[\w!@#\-.?,\s]*`
Required: No

 ** mostRecentExecutionStatus **   <a name="appflow-Type-ExecutionDetails-mostRecentExecutionStatus"></a>
 Specifies the status of the most recent flow run.
Type: String
Valid Values: `InProgress | Successful | Error | CancelStarted | Canceled`
Required: No

 ** mostRecentExecutionTime **   <a name="appflow-Type-ExecutionDetails-mostRecentExecutionTime"></a>
 Specifies the time of the most recent flow run.
Type: Timestamp
Required: No

## See Also
<a name="API_ExecutionDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ExecutionDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ExecutionDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ExecutionDetails)
