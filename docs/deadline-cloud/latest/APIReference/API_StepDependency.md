---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StepDependency.html
---

# StepDependency
<a name="API_StepDependency"></a>

The details of step dependency.

## Contents
<a name="API_StepDependency_Contents"></a>

 ** status **   <a name="deadlinecloud-Type-StepDependency-status"></a>
The step dependency status.
Type: String
Valid Values: `RESOLVED | UNRESOLVED`
Required: Yes

 ** stepId **   <a name="deadlinecloud-Type-StepDependency-stepId"></a>
The step ID.
Type: String
Pattern: `step-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_StepDependency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StepDependency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StepDependency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StepDependency)
