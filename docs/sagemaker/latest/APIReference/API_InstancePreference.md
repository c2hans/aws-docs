---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_InstancePreference.html
---

# InstancePreference
<a name="API_InstancePreference"></a>

A candidate instance type preference in an `InstancePreferences` list.

## Contents
<a name="API_InstancePreference_Contents"></a>

 ** InstanceType **   <a name="sagemaker-Type-InstancePreference-InstanceType"></a>
The ML compute instance type. An instance type can appear only once in an `InstancePreferences` list.
Type: String
Valid Values: `ml.m4.xlarge | ml.m4.2xlarge | ml.m4.4xlarge | ml.m4.10xlarge | ml.m4.16xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.12xlarge | ml.m5.24xlarge | ml.c4.xlarge | ml.c4.2xlarge | ml.c4.4xlarge | ml.c4.8xlarge | ml.p2.xlarge | ml.p2.8xlarge | ml.p2.16xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.p5.48xlarge | ml.p5e.48xlarge | ml.p5en.48xlarge | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.18xlarge | ml.c5n.xlarge | ml.c5n.2xlarge | ml.c5n.4xlarge | ml.c5n.9xlarge | ml.c5n.18xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.16xlarge | ml.g6.12xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.16xlarge | ml.g6e.12xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.trn2.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.8xlarge | ml.c6i.4xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.r5d.large | ml.r5d.xlarge | ml.r5d.2xlarge | ml.r5d.4xlarge | ml.r5d.8xlarge | ml.r5d.12xlarge | ml.r5d.16xlarge | ml.r5d.24xlarge | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.p6-b200.48xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.p6e-gb200.36xlarge | ml.p5.4xlarge | ml.p6-b300.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge`
Required: Yes

 ** InstanceCount **   <a name="sagemaker-Type-InstancePreference-InstanceCount"></a>
The number of instances to launch if this instance type is selected. Specify the instance count for the training job in one of the following two ways:

1.  **Per preference** – Set `InstanceCount` on every preference in the `InstancePreferences` list and don't set `ResourceConfig$InstanceCount`. Use this when each instance type needs a different number of instances to deliver equivalent compute.

1.  **One count for the job** – Set `ResourceConfig$InstanceCount` and omit it from every preference. SageMaker applies this to all instance types in the list.
For example, in a list of five preferences, either all five specify `InstanceCount` or none of them do. SageMaker rejects requests that set `InstanceCount` on only some preferences, that set it both per preference and in `ResourceConfig`, or that omit it in both places.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TrainingPlanArns **   <a name="sagemaker-Type-InstancePreference-TrainingPlanArns"></a>
The Amazon Resource Name (ARN) of a training plan to use if this instance type is selected. The plan's instance type must match `InstanceType`. A preference with a training plan uses that plan's reserved capacity; a preference without one uses on-demand capacity. Per-preference `TrainingPlanArns` is mutually exclusive with the job-level `TrainingPlanArn` in `ResourceConfig`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 50. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:training-plan/.*`
Required: No

## See Also
<a name="API_InstancePreference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/InstancePreference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/InstancePreference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/InstancePreference)
