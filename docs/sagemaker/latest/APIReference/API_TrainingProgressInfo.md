---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingProgressInfo.html
---

# TrainingProgressInfo
<a name="API_TrainingProgressInfo"></a>

 The serverless training job progress information.

## Contents
<a name="API_TrainingProgressInfo_Contents"></a>

 ** CurrentEpoch **   <a name="sagemaker-Type-TrainingProgressInfo-CurrentEpoch"></a>
 The current epoch number.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** CurrentStep **   <a name="sagemaker-Type-TrainingProgressInfo-CurrentStep"></a>
 The current step number.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** MaxEpoch **   <a name="sagemaker-Type-TrainingProgressInfo-MaxEpoch"></a>
 The maximum number of epochs for this job.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** TotalStepCountPerEpoch **   <a name="sagemaker-Type-TrainingProgressInfo-TotalStepCountPerEpoch"></a>
 The total step count per epoch.
Type: Long
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_TrainingProgressInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/TrainingProgressInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/TrainingProgressInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/TrainingProgressInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
