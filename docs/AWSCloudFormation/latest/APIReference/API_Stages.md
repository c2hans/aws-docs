---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Stages.html
---

# Stages

Contains detailed progress information for the individual stages of a StackSet operation: the role provisioning stage and the stack instances deployment stage.

## Contents
<a name="API_Stages_Contents"></a>

 ** RoleProvisioning **
The progress detail for the role provisioning stage. For operations that do not provision roles, this stage is present with a `Status` of `NOT_APPLICABLE`.
Type: [RoleProvisioning](API_RoleProvisioning.md) object
Required: No

 ** StackInstancesDeployment **
The progress detail for the stack instances deployment stage. This stage reports the deployment of stack instances to the target accounts and AWS Regions, after any role provisioning has finished.
Type: [StackInstancesDeployment](API_StackInstancesDeployment.md) object
Required: No

## See Also
<a name="API_Stages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/Stages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/Stages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/Stages)
