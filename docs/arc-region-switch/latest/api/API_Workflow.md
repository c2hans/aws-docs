---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Workflow.html
---

# Workflow
<a name="API_Workflow"></a>

Represents a workflow in a Region switch plan. A workflow defines a sequence of steps to execute during a Region switch.

## Contents
<a name="API_Workflow_Contents"></a>

 ** workflowTargetAction **   <a name="regionswitch-Type-Workflow-workflowTargetAction"></a>
The action that the workflow performs. Valid values include `activate` and `deactivate`.
Type: String
Valid Values: `activate | deactivate | postRecovery`
Required: Yes

 ** steps **   <a name="regionswitch-Type-Workflow-steps"></a>
The steps that make up the workflow.
Type: Array of [Step](API_Step.md) objects
Required: No

 ** workflowDescription **   <a name="regionswitch-Type-Workflow-workflowDescription"></a>
The description of the workflow.
Type: String
Required: No

 ** workflowTargetRegion **   <a name="regionswitch-Type-Workflow-workflowTargetRegion"></a>
The AWS Region that the workflow targets.
Type: String
Pattern: `[a-z]{2}-[a-z-]+-\d+`
Required: No

## See Also
<a name="API_Workflow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Workflow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Workflow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Workflow)
