---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ParentStepDetails.html
---

# ParentStepDetails
<a name="API_ParentStepDetails"></a>

A detailed status of the parent step.

## Contents
<a name="API_ParentStepDetails_Contents"></a>

 ** Action **   <a name="systemsmanager-Type-ParentStepDetails-Action"></a>
The name of the automation action.
Type: String
Pattern: `^aws:[a-zA-Z]{3,25}$`
Required: No

 ** Iteration **   <a name="systemsmanager-Type-ParentStepDetails-Iteration"></a>
The current repetition of the loop represented by an integer.
Type: Integer
Required: No

 ** IteratorValue **   <a name="systemsmanager-Type-ParentStepDetails-IteratorValue"></a>
The current value of the specified iterator in the loop.
Type: String
Required: No

 ** StepExecutionId **   <a name="systemsmanager-Type-ParentStepDetails-StepExecutionId"></a>
The unique ID of a step execution.
Type: String
Required: No

 ** StepName **   <a name="systemsmanager-Type-ParentStepDetails-StepName"></a>
The name of the step.
Type: String
Required: No

## See Also
<a name="API_ParentStepDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ParentStepDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ParentStepDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ParentStepDetails)
