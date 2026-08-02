---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_LabelingJobStoppingConditions.html
---

# LabelingJobStoppingConditions
<a name="API_LabelingJobStoppingConditions"></a>

A set of conditions for stopping a labeling job. If any of the conditions are met, the job is automatically stopped. You can use these conditions to control the cost of data labeling.

**Note**
Labeling jobs fail after 30 days with an appropriate client error message.

## Contents
<a name="API_LabelingJobStoppingConditions_Contents"></a>

 ** MaxHumanLabeledObjectCount **   <a name="sagemaker-Type-LabelingJobStoppingConditions-MaxHumanLabeledObjectCount"></a>
The maximum number of objects that can be labeled by human workers.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MaxPercentageOfInputDatasetLabeled **   <a name="sagemaker-Type-LabelingJobStoppingConditions-MaxPercentageOfInputDatasetLabeled"></a>
The maximum number of input data objects that should be labeled.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

## See Also
<a name="API_LabelingJobStoppingConditions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/LabelingJobStoppingConditions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/LabelingJobStoppingConditions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/LabelingJobStoppingConditions)
