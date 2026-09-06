---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_JobStep.html
---

# JobStep
<a name="API_JobStep"></a>

Provides information related to a job step.

## Contents
<a name="API_JobStep_Contents"></a>

 ** procStepName **   <a name="m2-Type-JobStep-procStepName"></a>
The name of a procedure step.
Type: String
Required: No

 ** procStepNumber **   <a name="m2-Type-JobStep-procStepNumber"></a>
The number of a procedure step.
Type: Integer
Required: No

 ** stepCheckpoint **   <a name="m2-Type-JobStep-stepCheckpoint"></a>
A registered step-level checkpoint identifier that can be used for restarting an AWS Blu Age application batch job.
Type: Integer
Required: No

 ** stepCheckpointStatus **   <a name="m2-Type-JobStep-stepCheckpointStatus"></a>
The step-level checkpoint status for an AWS Blu Age application batch job.
Type: String
Required: No

 ** stepCheckpointTime **   <a name="m2-Type-JobStep-stepCheckpointTime"></a>
The step-level checkpoint status for an AWS Blu Age application batch job.
Type: Timestamp
Required: No

 ** stepCondCode **   <a name="m2-Type-JobStep-stepCondCode"></a>
The condition code of a step.
Type: String
Required: No

 ** stepName **   <a name="m2-Type-JobStep-stepName"></a>
The name of a step.
Type: String
Required: No

 ** stepNumber **   <a name="m2-Type-JobStep-stepNumber"></a>
The number of a step.
Type: Integer
Required: No

 ** stepRestartable **   <a name="m2-Type-JobStep-stepRestartable"></a>
Specifies if a step can be restarted or not.
Type: Boolean
Required: No

## See Also
<a name="API_JobStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/JobStep)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/JobStep)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/JobStep)
