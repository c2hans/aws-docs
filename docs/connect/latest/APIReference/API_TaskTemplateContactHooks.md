---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TaskTemplateContactHooks.html
---

# TaskTemplateContactHooks
<a name="API_TaskTemplateContactHooks"></a>

The event hooks that are set on tasks created by using this template.

## Contents
<a name="API_TaskTemplateContactHooks_Contents"></a>

 ** WrapUpFlowId **   <a name="connect-Type-TaskTemplateContactHooks-WrapUpFlowId"></a>
The identifier of the flow module that runs when an agent attempts to disconnect from a task created by referencing this template. If no agent ever connects to the task, the flow module runs when the task is terminated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_TaskTemplateContactHooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TaskTemplateContactHooks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TaskTemplateContactHooks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TaskTemplateContactHooks)
