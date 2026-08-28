---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_MicrovmHooks.html
---

# MicrovmHooks
<a name="API_MicrovmHooks"></a>

Configuration for lifecycle hooks invoked during MicroVM events such as run, resume, suspend, and terminate.

## Contents
<a name="API_MicrovmHooks_Contents"></a>

 ** resume **   <a name="lambdamicrovm-Type-MicrovmHooks-resume"></a>
The path of the hook invoked when the MicroVM resumes from a suspended state.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** resumeTimeoutInSeconds **   <a name="lambdamicrovm-Type-MicrovmHooks-resumeTimeoutInSeconds"></a>
The maximum time in seconds for the resume hook to complete.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

 ** run **   <a name="lambdamicrovm-Type-MicrovmHooks-run"></a>
The path of the hook invoked when the MicroVM starts running.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** runTimeoutInSeconds **   <a name="lambdamicrovm-Type-MicrovmHooks-runTimeoutInSeconds"></a>
The maximum time in seconds for the run hook to complete.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

 ** suspend **   <a name="lambdamicrovm-Type-MicrovmHooks-suspend"></a>
The path of the hook invoked when the MicroVM is suspended.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** suspendTimeoutInSeconds **   <a name="lambdamicrovm-Type-MicrovmHooks-suspendTimeoutInSeconds"></a>
The maximum time in seconds for the suspend hook to complete.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

 ** terminate **   <a name="lambdamicrovm-Type-MicrovmHooks-terminate"></a>
The path of the hook invoked when the MicroVM is terminated.
Type: String
Valid Values: `DISABLED | ENABLED`
Required: No

 ** terminateTimeoutInSeconds **   <a name="lambdamicrovm-Type-MicrovmHooks-terminateTimeoutInSeconds"></a>
The maximum time in seconds for the terminate hook to complete.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60.
Required: No

## See Also
<a name="API_MicrovmHooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/MicrovmHooks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/MicrovmHooks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/MicrovmHooks)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
