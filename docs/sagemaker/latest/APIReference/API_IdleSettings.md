---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IdleSettings.html
---

# IdleSettings
<a name="API_IdleSettings"></a>

Settings related to idle shutdown of Studio applications.

## Contents
<a name="API_IdleSettings_Contents"></a>

 ** IdleTimeoutInMinutes **   <a name="sagemaker-Type-IdleSettings-IdleTimeoutInMinutes"></a>
The time that SageMaker waits after the application becomes idle before shutting it down.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 525600.
Required: No

 ** LifecycleManagement **   <a name="sagemaker-Type-IdleSettings-LifecycleManagement"></a>
Indicates whether idle shutdown is activated for the application type.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** MaxIdleTimeoutInMinutes **   <a name="sagemaker-Type-IdleSettings-MaxIdleTimeoutInMinutes"></a>
The maximum value in minutes that custom idle shutdown can be set to by the user.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 525600.
Required: No

 ** MinIdleTimeoutInMinutes **   <a name="sagemaker-Type-IdleSettings-MinIdleTimeoutInMinutes"></a>
The minimum value in minutes that custom idle shutdown can be set to by the user.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 525600.
Required: No

## See Also
<a name="API_IdleSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/IdleSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/IdleSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/IdleSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
