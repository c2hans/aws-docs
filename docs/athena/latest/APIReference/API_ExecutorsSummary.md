---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_ExecutorsSummary.html
---

# ExecutorsSummary
<a name="API_ExecutorsSummary"></a>

Contains summary information about an executor.

## Contents
<a name="API_ExecutorsSummary_Contents"></a>

 ** ExecutorId **   <a name="athena-Type-ExecutorsSummary-ExecutorId"></a>
The UUID of the executor.
Type: String
Length Constraints: Maximum length of 100000.
Pattern: `.*`
Required: Yes

 ** ExecutorSize **   <a name="athena-Type-ExecutorsSummary-ExecutorSize"></a>
The smallest unit of compute that a session can request from Athena. Size is measured in data processing unit (DPU) values, a relative measure of processing power.
Type: Long
Required: No

 ** ExecutorState **   <a name="athena-Type-ExecutorsSummary-ExecutorState"></a>
The processing state of the executor. A description of each state follows.
 `CREATING` - The executor is being started, including acquiring resources.
 `CREATED` - The executor has been started.
 `REGISTERED` - The executor has been registered.
 `TERMINATING` - The executor is in the process of shutting down.
 `TERMINATED` - The executor is no longer running.
 `FAILED` - Due to a failure, the executor is no longer running.
Type: String
Valid Values: `CREATING | CREATED | REGISTERED | TERMINATING | TERMINATED | FAILED`
Required: No

 ** ExecutorType **   <a name="athena-Type-ExecutorsSummary-ExecutorType"></a>
The type of executor used for the application (`COORDINATOR`, `GATEWAY`, or `WORKER`).
Type: String
Valid Values: `COORDINATOR | GATEWAY | WORKER`
Required: No

 ** StartDateTime **   <a name="athena-Type-ExecutorsSummary-StartDateTime"></a>
The date and time that the executor started.
Type: Long
Required: No

 ** TerminationDateTime **   <a name="athena-Type-ExecutorsSummary-TerminationDateTime"></a>
The date and time that the executor was terminated.
Type: Long
Required: No

## See Also
<a name="API_ExecutorsSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/ExecutorsSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/ExecutorsSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/ExecutorsSummary)
