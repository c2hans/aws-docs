---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_JobStepRestartMarker.html
---

# JobStepRestartMarker
<a name="API_JobStepRestartMarker"></a>

Provides step/procedure step information for a restart batch job operation.

## Contents
<a name="API_JobStepRestartMarker_Contents"></a>

 ** fromStep **   <a name="m2-Type-JobStepRestartMarker-fromStep"></a>
The step name that a batch job was restarted from.
Type: String
Required: Yes

 ** fromProcStep **   <a name="m2-Type-JobStepRestartMarker-fromProcStep"></a>
The procedure step name that a batch job was restarted from.
Type: String
Required: No

 ** skip **   <a name="m2-Type-JobStepRestartMarker-skip"></a>
The step-level checkpoint timestamp (creation or last modification) for an AWS Blu Age application batch job.
Type: Boolean
Required: No

 ** stepCheckpoint **   <a name="m2-Type-JobStepRestartMarker-stepCheckpoint"></a>
Skip selected step and issue a restart from immediate successor step for an AWS Blu Age application batch job.
Type: Integer
Required: No

 ** toProcStep **   <a name="m2-Type-JobStepRestartMarker-toProcStep"></a>
The procedure step name that a batch job was restarted to.
Type: String
Required: No

 ** toStep **   <a name="m2-Type-JobStepRestartMarker-toStep"></a>
The step name that a batch job was restarted to.
Type: String
Required: No

## See Also
<a name="API_JobStepRestartMarker_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/JobStepRestartMarker)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/JobStepRestartMarker)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/JobStepRestartMarker)
