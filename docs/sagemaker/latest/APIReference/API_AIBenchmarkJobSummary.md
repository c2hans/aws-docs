---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AIBenchmarkJobSummary.html
---

# AIBenchmarkJobSummary
<a name="API_AIBenchmarkJobSummary"></a>

Summary information about an AI benchmark job.

## Contents
<a name="API_AIBenchmarkJobSummary_Contents"></a>

 ** AIBenchmarkJobArn **   <a name="sagemaker-Type-AIBenchmarkJobSummary-AIBenchmarkJobArn"></a>
The Amazon Resource Name (ARN) of the benchmark job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:ai-benchmark-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AIBenchmarkJobName **   <a name="sagemaker-Type-AIBenchmarkJobSummary-AIBenchmarkJobName"></a>
The name of the benchmark job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** AIBenchmarkJobStatus **   <a name="sagemaker-Type-AIBenchmarkJobSummary-AIBenchmarkJobStatus"></a>
The status of the benchmark job.
Type: String
Valid Values: `InProgress | Completed | Failed | Stopping | Stopped`
Required: Yes

 ** CreationTime **   <a name="sagemaker-Type-AIBenchmarkJobSummary-CreationTime"></a>
A timestamp that indicates when the benchmark job was created.
Type: Timestamp
Required: Yes

 ** AIWorkloadConfigName **   <a name="sagemaker-Type-AIBenchmarkJobSummary-AIWorkloadConfigName"></a>
The name of the AI workload configuration used by the benchmark job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** EndTime **   <a name="sagemaker-Type-AIBenchmarkJobSummary-EndTime"></a>
A timestamp that indicates when the benchmark job completed.
Type: Timestamp
Required: No

## See Also
<a name="API_AIBenchmarkJobSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AIBenchmarkJobSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AIBenchmarkJobSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AIBenchmarkJobSummary)
