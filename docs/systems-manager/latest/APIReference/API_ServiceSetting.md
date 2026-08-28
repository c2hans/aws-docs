---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ServiceSetting.html
---

# ServiceSetting
<a name="API_ServiceSetting"></a>

The service setting data structure.

 `ServiceSetting` is an account-level setting for an AWS service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an AWS service charges money to the account based on feature or service usage, then the AWS service team might create a default setting of "false". This means the user can't use this feature unless they change the setting to "true" and intentionally opt in for a paid feature.

Services map a `SettingId` object to a setting value. AWS services teams define the default value for a `SettingId`. You can't create a new `SettingId`, but you can overwrite the default value if you have the `ssm:UpdateServiceSetting` permission for the setting. Use the [UpdateServiceSetting](API_UpdateServiceSetting.md) API operation to change the default setting. Or, use the [ResetServiceSetting](API_ResetServiceSetting.md) to change the value back to the original value defined by the AWS service team.

## Contents
<a name="API_ServiceSetting_Contents"></a>

 ** ARN **   <a name="systemsmanager-Type-ServiceSetting-ARN"></a>
The ARN of the service setting.
Type: String
Required: No

 ** LastModifiedDate **   <a name="systemsmanager-Type-ServiceSetting-LastModifiedDate"></a>
The last time the service setting was modified.
Type: Timestamp
Required: No

 ** LastModifiedUser **   <a name="systemsmanager-Type-ServiceSetting-LastModifiedUser"></a>
The ARN of the last modified user. This field is populated only if the setting value was overwritten.
Type: String
Required: No

 ** SettingId **   <a name="systemsmanager-Type-ServiceSetting-SettingId"></a>
The ID of the service setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** SettingValue **   <a name="systemsmanager-Type-ServiceSetting-SettingValue"></a>
The value of the service setting.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** Status **   <a name="systemsmanager-Type-ServiceSetting-Status"></a>
The status of the service setting. The value can be Default, Customized or PendingUpdate.
+ Default: The current setting uses a default value provisioned by the AWS service team.
+ Customized: The current setting use a custom value specified by the customer.
+ PendingUpdate: The current setting uses a default or custom value, but a setting change request is pending approval.
Type: String
Required: No

## See Also
<a name="API_ServiceSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ServiceSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ServiceSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ServiceSetting)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
