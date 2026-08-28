---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StoppingCondition.html
---

# StoppingCondition
<a name="API_StoppingCondition"></a>

Specifies a limit to how long a job can run. When the job reaches the time limit, SageMaker ends the job. Use this API to cap costs.

To stop a training job, SageMaker sends the algorithm the `SIGTERM` signal, which delays job termination for 120 seconds. Algorithms can use this 120-second window to save the model artifacts, so the results of training are not lost.

The training algorithms provided by SageMaker automatically save the intermediate results of a model training job when possible. This attempt to save artifacts is only a best effort case as model might not be in a state from which it can be saved. For example, if training has just started, the model might not be ready to save. When saved, this intermediate data is a valid model artifact. You can use it to create a model with `CreateModel`.

**Note**
The Neural Topic Model (NTM) currently does not support saving intermediate model artifacts. When training NTMs, make sure that the maximum runtime is sufficient for the training job to complete.

## Contents
<a name="API_StoppingCondition_Contents"></a>

 ** MaxPendingTimeInSeconds **   <a name="sagemaker-Type-StoppingCondition-MaxPendingTimeInSeconds"></a>
The maximum length of time, in seconds, that a training or compilation job can be pending before it is stopped.
When working with training jobs that use capacity from [training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html), not all `Pending` job states count against the `MaxPendingTimeInSeconds` limit. The following scenarios do not increment the `MaxPendingTimeInSeconds` counter:
+ The plan is in a `Scheduled` state: Jobs queued (in `Pending` status) before a plan's start date (waiting for scheduled start time)
+ Between capacity reservations: Jobs temporarily back to `Pending` status between two capacity reservation periods
 `MaxPendingTimeInSeconds` only increments when jobs are actively waiting for capacity in an `Active` plan.
Type: Integer
Valid Range: Minimum value of 7200. Maximum value of 2419200.
Required: No

 ** MaxRuntimeInSeconds **   <a name="sagemaker-Type-StoppingCondition-MaxRuntimeInSeconds"></a>
The maximum length of time, in seconds, that a training or compilation job can run before it is stopped.
For compilation jobs, if the job does not complete during this time, a `TimeOut` error is generated. We recommend starting with 900 seconds and increasing as necessary based on your model.
For all other jobs, if the job does not complete during this time, SageMaker ends the job. When `RetryStrategy` is specified in the job request, `MaxRuntimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt. The default value is 1 day. The maximum value is 28 days.
The maximum time that a `TrainingJob` can run in total, including any time spent publishing metrics or archiving and uploading models after it has been stopped, is 30 days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MaxWaitTimeInSeconds **   <a name="sagemaker-Type-StoppingCondition-MaxWaitTimeInSeconds"></a>
The maximum length of time, in seconds, that a managed Spot training job has to complete. It is the amount of time spent waiting for Spot capacity plus the amount of time the job can run. It must be equal to or greater than `MaxRuntimeInSeconds`. If the job does not complete during this time, SageMaker ends the job.
When `RetryStrategy` is specified in the job request, `MaxWaitTimeInSeconds` specifies the maximum time for all of the attempts in total, not each individual attempt.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_StoppingCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StoppingCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StoppingCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StoppingCondition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
