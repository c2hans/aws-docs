---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ProfilerConfigForUpdate.html
---

# ProfilerConfigForUpdate
<a name="API_ProfilerConfigForUpdate"></a>

Configuration information for updating the Amazon SageMaker Debugger profile parameters, system and framework metrics configurations, and storage paths.

## Contents
<a name="API_ProfilerConfigForUpdate_Contents"></a>

 ** DisableProfiler **   <a name="sagemaker-Type-ProfilerConfigForUpdate-DisableProfiler"></a>
To turn off Amazon SageMaker Debugger monitoring and profiling while a training job is in progress, set to `True`.
Type: Boolean
Required: No

 ** ProfilingIntervalInMilliseconds **   <a name="sagemaker-Type-ProfilerConfigForUpdate-ProfilingIntervalInMilliseconds"></a>
A time interval for capturing system metrics in milliseconds. Available values are 100, 200, 500, 1000 (1 second), 5000 (5 seconds), and 60000 (1 minute) milliseconds. The default value is 500 milliseconds.
Type: Long
Required: No

 ** ProfilingParameters **   <a name="sagemaker-Type-ProfilerConfigForUpdate-ProfilingParameters"></a>
Configuration information for capturing framework metrics. Available key strings for different profiling options are `DetailedProfilingConfig`, `PythonProfilingConfig`, and `DataLoaderProfilingConfig`. The following codes are configuration structures for the `ProfilingParameters` parameter. To learn more about how to configure the `ProfilingParameters` parameter, see [Use the SageMaker and Debugger Configuration API Operations to Create, Update, and Debug Your Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html).
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 20 items.
Key Length Constraints: Minimum length of 1. Maximum length of 256.
Key Pattern: `.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

 ** S3OutputPath **   <a name="sagemaker-Type-ProfilerConfigForUpdate-S3OutputPath"></a>
Path to Amazon S3 storage location for system and framework metrics.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

## See Also
<a name="API_ProfilerConfigForUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ProfilerConfigForUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ProfilerConfigForUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ProfilerConfigForUpdate)
