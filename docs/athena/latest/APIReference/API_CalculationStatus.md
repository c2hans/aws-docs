---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_CalculationStatus.html
---

# CalculationStatus
<a name="API_CalculationStatus"></a>

Contains information about the status of a notebook calculation.

## Contents
<a name="API_CalculationStatus_Contents"></a>

 ** CompletionDateTime **   <a name="athena-Type-CalculationStatus-CompletionDateTime"></a>
The date and time the calculation completed processing.
Type: Timestamp
Required: No

 ** State **   <a name="athena-Type-CalculationStatus-State"></a>
The state of the calculation execution. A description of each state follows.
 `CREATING` - The calculation is in the process of being created.
 `CREATED` - The calculation has been created and is ready to run.
 `QUEUED` - The calculation has been queued for processing.
 `RUNNING` - The calculation is running.
 `CANCELING` - A request to cancel the calculation has been received and the system is working to stop it.
 `CANCELED` - The calculation is no longer running as the result of a cancel request.
 `COMPLETED` - The calculation has completed without error.
 `FAILED` - The calculation failed and is no longer running.
Type: String
Valid Values: `CREATING | CREATED | QUEUED | RUNNING | CANCELING | CANCELED | COMPLETED | FAILED`
Required: No

 ** StateChangeReason **   <a name="athena-Type-CalculationStatus-StateChangeReason"></a>
The reason for the calculation state change (for example, the calculation was canceled because the session was terminated).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** SubmissionDateTime **   <a name="athena-Type-CalculationStatus-SubmissionDateTime"></a>
The date and time the calculation was submitted for processing.
Type: Timestamp
Required: No

## See Also
<a name="API_CalculationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/CalculationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/CalculationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/CalculationStatus)
