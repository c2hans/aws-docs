---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunConfigOutput.html
---

# CanaryRunConfigOutput
<a name="API_CanaryRunConfigOutput"></a>

A structure that contains information about a canary run.

## Contents
<a name="API_CanaryRunConfigOutput_Contents"></a>

 ** ActiveTracing **   <a name="synthetics-Type-CanaryRunConfigOutput-ActiveTracing"></a>
Displays whether this canary run used active X-Ray tracing.
Type: Boolean
Required: No

 ** EphemeralStorage **   <a name="synthetics-Type-CanaryRunConfigOutput-EphemeralStorage"></a>
Specifies the amount of ephemeral storage (in MB) to allocate for the canary run during execution. This temporary storage is used for storing canary run artifacts (which are uploaded to an Amazon S3 bucket at the end of the run), and any canary browser operations. This temporary storage is cleared after the run is completed. Default storage value is 1024 MB.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 10240.
Required: No

 ** MemoryInMB **   <a name="synthetics-Type-CanaryRunConfigOutput-MemoryInMB"></a>
The maximum amount of memory available to the canary while it is running, in MB. This value must be a multiple of 64.
Type: Integer
Valid Range: Minimum value of 960. Maximum value of 3008.
Required: No

 ** TimeoutInSeconds **   <a name="synthetics-Type-CanaryRunConfigOutput-TimeoutInSeconds"></a>
How long the canary is allowed to run before it must stop.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 840.
Required: No

## See Also
<a name="API_CanaryRunConfigOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryRunConfigOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryRunConfigOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryRunConfigOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Synthetics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonSynthetics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
