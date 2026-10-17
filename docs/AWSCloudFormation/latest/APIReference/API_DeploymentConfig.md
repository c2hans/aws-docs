---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeploymentConfig.html
---

# DeploymentConfig
<a name="API_DeploymentConfig"></a>

The deployment configuration for a stack operation, including the deployment mode.

## Contents
<a name="API_DeploymentConfig_Contents"></a>

 ** DisableRollback **
Specifies whether to disable rollback of the stack if the stack operation fails.
Default: `false`
Type: Boolean
Required: No

 ** Mode **
Specifies the deployment mode for the stack operation. Possible values are:
+  `STANDARD` - Use the standard deployment behavior, ensuring resources are ready to serve traffic before completing the operation. This is the default. You do not need to specify this value explicitly.
+  `EXPRESS` - Complete the stack operation when resource configuration is applied, without waiting for resources to become ready to serve traffic. Resources continue becoming ready in the background.
Type: String
Valid Values: `STANDARD | EXPRESS`
Required: No

## See Also
<a name="API_DeploymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudformation-2010-05-15/DeploymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudformation-2010-05-15/DeploymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudformation-2010-05-15/DeploymentConfig)
