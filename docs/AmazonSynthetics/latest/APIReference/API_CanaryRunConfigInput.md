---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunConfigInput.html
---

# CanaryRunConfigInput
<a name="API_CanaryRunConfigInput"></a>

A structure that contains input information for a canary run.

## Contents
<a name="API_CanaryRunConfigInput_Contents"></a>

 ** ActiveTracing **   <a name="synthetics-Type-CanaryRunConfigInput-ActiveTracing"></a>
Specifies whether this canary is to use active AWS X-Ray tracing when it runs. Active tracing enables this canary run to be displayed in the ServiceLens and X-Ray service maps even if the canary does not hit an endpoint that has X-Ray tracing enabled. Using X-Ray tracing incurs charges. For more information, see [ Canaries and X-Ray tracing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_tracing.html).
You can enable active tracing only for canaries that use version `syn-nodejs-2.0` or later for their canary runtime.
Type: Boolean
Required: No

 ** EnvironmentVariables **   <a name="synthetics-Type-CanaryRunConfigInput-EnvironmentVariables"></a>
Specifies the keys and values to use for any environment variables used in the canary script. Use the following format:
{ "key1" : "value1", "key2" : "value2", ...}
Keys must start with a letter and be at least two characters. The total size of your environment variables cannot exceed 4 KB. You can't specify any Lambda reserved environment variables as the keys for your environment variables. For more information about reserved keys, see [ Runtime environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html#configuration-envvars-runtime).
Environment variable keys and values are encrypted at rest using AWS owned AWS KMS keys. However, the environment variables are not encrypted on the client side. Do not store sensitive information in them.
Type: String to string map
Key Pattern: `[a-zA-Z]([a-zA-Z0-9_])+`
Required: No

 ** EphemeralStorage **   <a name="synthetics-Type-CanaryRunConfigInput-EphemeralStorage"></a>
Specifies the amount of ephemeral storage (in MB) to allocate for the canary run during execution. This temporary storage is used for storing canary run artifacts (which are uploaded to an Amazon S3 bucket at the end of the run), and any canary browser operations. This temporary storage is cleared after the run is completed. Default storage value is 1024 MB.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 10240.
Required: No

 ** MemoryInMB **   <a name="synthetics-Type-CanaryRunConfigInput-MemoryInMB"></a>
The maximum amount of memory available to the canary while it is running, in MB. This value must be a multiple of 64.
Type: Integer
Valid Range: Minimum value of 960. Maximum value of 3008.
Required: No

 ** TimeoutInSeconds **   <a name="synthetics-Type-CanaryRunConfigInput-TimeoutInSeconds"></a>
How long the canary is allowed to run before it must stop. You can't set this time to be longer than the frequency of the runs of this canary.
If you omit this field, the frequency of the canary is used as this value, up to a maximum of 14 minutes.
Type: Integer
Valid Range: Minimum value of 3. Maximum value of 840.
Required: No

## See Also
<a name="API_CanaryRunConfigInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/CanaryRunConfigInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/CanaryRunConfigInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/CanaryRunConfigInput)
