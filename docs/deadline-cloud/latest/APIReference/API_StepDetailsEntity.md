---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepDetailsEntity.html
---

# StepDetailsEntity
<a name="API_StepDetailsEntity"></a>

The details of a step entity.

## Contents
<a name="API_StepDetailsEntity_Contents"></a>

 ** dependencies **   <a name="deadlinecloud-Type-StepDetailsEntity-dependencies"></a>
The dependencies for a step.
Type: Array of strings
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-StepDetailsEntity-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** schemaVersion **   <a name="deadlinecloud-Type-StepDetailsEntity-schemaVersion"></a>
The schema version for a step template.
Type: String
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-StepDetailsEntity-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

 ** template **   <a name="deadlinecloud-Type-StepDetailsEntity-template"></a>
The template for a step.
Type: JSON value
Required: Yes

## See Also
<a name="API_StepDetailsEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepDetailsEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepDetailsEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepDetailsEntity)
