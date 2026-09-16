---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateMacSystemIntegrityProtectionModificationTask.html
---

# CreateMacSystemIntegrityProtectionModificationTask
<a name="API_CreateMacSystemIntegrityProtectionModificationTask"></a>

Creates a System Integrity Protection (SIP) modification task to configure the SIP settings for an x86 Mac instance or Apple silicon Mac instance. For more information, see [ Configure SIP for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-sip-settings.html#mac-sip-configure) in the *Amazon EC2 User Guide*.

When you configure the SIP settings for your instance, you can either enable or disable all SIP settings, or you can specify a custom SIP configuration that selectively enables or disables specific SIP settings.

**Note**
If you implement a custom configuration, [ connect to the instance and verify the settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-sip-settings.html#mac-sip-check-settings) to ensure that your requirements are properly implemented and functioning as intended.
SIP configurations might change with macOS updates. We recommend that you review custom SIP settings after any macOS version upgrade to ensure continued compatibility and proper functionality of your security configurations.

To enable or disable all SIP settings, use the **MacSystemIntegrityProtectionStatus** parameter only. For example, to enable all SIP settings, specify the following:
+  `MacSystemIntegrityProtectionStatus=enabled`

To specify a custom configuration that selectively enables or disables specific SIP settings, use the **MacSystemIntegrityProtectionStatus** parameter to enable or disable all SIP settings, and then use the **MacSystemIntegrityProtectionConfiguration** parameter to specify exceptions. In this case, the exceptions you specify for **MacSystemIntegrityProtectionConfiguration** override the value you specify for **MacSystemIntegrityProtectionStatus**. For example, to enable all SIP settings, except `NvramProtections`, specify the following:
+  `MacSystemIntegrityProtectionStatus=enabled`
+  `MacSystemIntegrityProtectionConfigurationRequest "NvramProtections=disabled"`

## Request Parameters
<a name="API_CreateMacSystemIntegrityProtectionModificationTask_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId**
The ID of the Amazon EC2 Mac instance.
Type: String
Required: Yes

 **MacCredentials**
 **[Apple silicon Mac instances only]** Specifies the following credentials:
+  **Internal disk administrative user**
  +  **Username** - Only the default administrative user (`aws-managed-user`) is supported and it is used by default. You can't specify a different administrative user.
  +  **Password** - If you did not change the default password for `aws-managed-user`, specify the default password, which is *blank*. Otherwise, specify your password.
+  **Amazon EBS root volume administrative user**
  +  **Username** - If you did not change the default administrative user, specify `ec2-user`. Otherwise, specify the username for your administrative user.
  +  **Password** - Specify the password for the administrative user.
The credentials must be specified in the following JSON format:
 `{ "internalDiskPassword":"internal-disk-admin_password", "rootVolumeUsername":"root-volume-admin_username", "rootVolumepassword":"root-volume-admin_password" }`
Type: String
Required: No

 **MacSystemIntegrityProtectionConfiguration**
Specifies the overrides to selectively enable or disable individual SIP settings. The individual settings you specify here override the overall SIP status you specify for **MacSystemIntegrityProtectionStatus**.
Type: [MacSystemIntegrityProtectionConfigurationRequest](API_MacSystemIntegrityProtectionConfigurationRequest.md) object
Required: No

 **MacSystemIntegrityProtectionStatus**
Specifies the overall SIP status for the instance. To enable all SIP settings, specify `enabled`. To disable all SIP settings, specify `disabled`.
Type: String
Valid Values: `enabled | disabled`
Required: Yes

 **TagSpecification.N**
Specifies tags to apply to the SIP modification task.
Type: Array of [TagSpecification](API_TagSpecification.md) objects
Required: No

## Response Elements
<a name="API_CreateMacSystemIntegrityProtectionModificationTask_ResponseElements"></a>

The following elements are returned by the service.

 **macModificationTask**
Information about the SIP modification task.
Type: [MacModificationTask](API_MacModificationTask.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_CreateMacSystemIntegrityProtectionModificationTask_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateMacSystemIntegrityProtectionModificationTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateMacSystemIntegrityProtectionModificationTask)
