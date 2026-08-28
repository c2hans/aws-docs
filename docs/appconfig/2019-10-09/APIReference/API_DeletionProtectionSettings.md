---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_DeletionProtectionSettings.html
---

# DeletionProtectionSettings
<a name="API_DeletionProtectionSettings"></a>

A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile or an environment if AWS AppConfig has called either [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) or [GetConfiguration](API_GetConfiguration.md) for the configuration profile or from the environment during the specified interval.

The default interval specified by `ProtectionPeriodInMinutes` is 60. `DeletionProtectionCheck` skips configuration profiles and environments that were created in the past hour.

## Contents
<a name="API_DeletionProtectionSettings_Contents"></a>

 ** Enabled **   <a name="appconfig-Type-DeletionProtectionSettings-Enabled"></a>
A parameter that indicates if deletion protection is enabled or not.
Type: Boolean
Required: No

 ** ProtectionPeriodInMinutes **   <a name="appconfig-Type-DeletionProtectionSettings-ProtectionPeriodInMinutes"></a>
The time interval during which AWS AppConfig monitors for calls to [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) or [GetConfiguration](API_GetConfiguration.md) for a configuration profile or from an environment. AWS AppConfig returns an error if a user calls [DeleteConfigurationProfile](API_DeleteConfigurationProfile.md) or [DeleteEnvironment](API_DeleteEnvironment.md) for the designated configuration profile or environment. To bypass the error and delete a configuration profile or an environment, specify `BYPASS` for the `DeletionProtectionCheck` parameter for either [DeleteConfigurationProfile](API_DeleteConfigurationProfile.md) or [DeleteEnvironment](API_DeleteEnvironment.md).
Type: Integer
Valid Range: Minimum value of 15. Maximum value of 1440.
Required: No

## See Also
<a name="API_DeletionProtectionSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/DeletionProtectionSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/DeletionProtectionSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/DeletionProtectionSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
