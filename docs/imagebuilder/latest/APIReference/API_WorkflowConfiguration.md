---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_WorkflowConfiguration.html
---

# WorkflowConfiguration
<a name="API_WorkflowConfiguration"></a>

Contains control settings and configurable inputs for a workflow resource.

## Contents
<a name="API_WorkflowConfiguration_Contents"></a>

 ** workflowArn **   <a name="imagebuilder-Type-WorkflowConfiguration-workflowArn"></a>
The Amazon Resource Name (ARN) of the workflow resource.
Type: String
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws(?:-[a-z-]+)?):workflow/(build|test|distribution)/[a-z0-9-_]+/(?:(?:([0-9]+|x)\.([0-9]+|x)\.([0-9]+|x))|(?:[0-9]+\.[0-9]+\.[0-9]+/[0-9]+))$`
Required: Yes

 ** onFailure **   <a name="imagebuilder-Type-WorkflowConfiguration-onFailure"></a>
The action to take if the workflow fails. With `CONTINUE`, a failed workflow is logged and image creation proceeds to the next workflow. If you don't set a value, the image build fails when the workflow fails. You can only set this property for test workflows.
Type: String
Valid Values: `CONTINUE | ABORT`
Required: No

 ** parallelGroup **   <a name="imagebuilder-Type-WorkflowConfiguration-parallelGroup"></a>
Test workflows are defined within named runtime groups called parallel groups. The parallel group is the named group that contains this test workflow. Test workflows within a parallel group can run at the same time. Image Builder starts up to five test workflows in the group at the same time, and starts additional workflows as others complete, until all workflows in the group have completed. This field only applies for test workflows.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[A-Za-z0-9][A-Za-z0-9-_+#]{0,99}$`
Required: No

 ** parameters **   <a name="imagebuilder-Type-WorkflowConfiguration-parameters"></a>
Contains parameter values for each of the parameters that the workflow document defined for the workflow resource.
Type: Array of [WorkflowParameter](API_WorkflowParameter.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_WorkflowConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/WorkflowConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/WorkflowConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/WorkflowConfiguration)
