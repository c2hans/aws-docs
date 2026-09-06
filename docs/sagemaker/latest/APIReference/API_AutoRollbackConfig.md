---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AutoRollbackConfig.html
---

# AutoRollbackConfig
<a name="API_AutoRollbackConfig"></a>

Automatic rollback configuration for handling endpoint deployment failures and recovery.

## Contents
<a name="API_AutoRollbackConfig_Contents"></a>

 ** Alarms **   <a name="sagemaker-Type-AutoRollbackConfig-Alarms"></a>
List of CloudWatch alarms in your account that are configured to monitor metrics on an endpoint. If any alarms are tripped during a deployment, SageMaker rolls back the deployment.
Type: Array of [Alarm](API_Alarm.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AutoRollbackConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AutoRollbackConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AutoRollbackConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AutoRollbackConfig)
