---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_LastExecutionStatus.html
---

# LastExecutionStatus
<a name="API_connect-app-integrations_LastExecutionStatus"></a>

The execution status of the last job.

## Contents
<a name="API_connect-app-integrations_LastExecutionStatus_Contents"></a>

 ** ExecutionStatus **   <a name="connect-Type-connect-app-integrations_LastExecutionStatus-ExecutionStatus"></a>
The job status enum string.
Type: String
Valid Values: `COMPLETED | IN_PROGRESS | FAILED`
Required: No

 ** StatusMessage **   <a name="connect-Type-connect-app-integrations_LastExecutionStatus-StatusMessage"></a>
The status message of a job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_connect-app-integrations_LastExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/LastExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/LastExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/LastExecutionStatus)
