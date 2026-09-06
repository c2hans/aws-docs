---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EdgeDeploymentConfig.html
---

# EdgeDeploymentConfig
<a name="API_EdgeDeploymentConfig"></a>

Contains information about the configuration of a deployment.

## Contents
<a name="API_EdgeDeploymentConfig_Contents"></a>

 ** FailureHandlingPolicy **   <a name="sagemaker-Type-EdgeDeploymentConfig-FailureHandlingPolicy"></a>
Toggle that determines whether to rollback to previous configuration if the current deployment fails. By default this is turned on. You may turn this off if you want to investigate the errors yourself.
Type: String
Valid Values: `ROLLBACK_ON_FAILURE | DO_NOTHING`
Required: Yes

## See Also
<a name="API_EdgeDeploymentConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/EdgeDeploymentConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/EdgeDeploymentConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/EdgeDeploymentConfig)
