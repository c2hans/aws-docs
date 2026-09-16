---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateServiceSetting.html
---

# UpdateServiceSetting
<a name="API_UpdateServiceSetting"></a>

 `ServiceSetting` is an account-level setting for an AWS service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an AWS service charges money to the account based on feature or service usage, then the AWS service team might create a default setting of "false". This means the user can't use this feature unless they change the setting to "true" and intentionally opt in for a paid feature.

Services map a `SettingId` object to a setting value. AWS services teams define the default value for a `SettingId`. You can't create a new `SettingId`, but you can overwrite the default value if you have the `ssm:UpdateServiceSetting` permission for the setting. Use the [GetServiceSetting](API_GetServiceSetting.md) API operation to view the current value. Or, use the [ResetServiceSetting](API_ResetServiceSetting.md) to change the value back to the original value defined by the AWS service team.

Update the service setting for the account.

## Request Syntax
<a name="API_UpdateServiceSetting_RequestSyntax"></a>

```
{
   "SettingId": "{{string}}",
   "SettingValue": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateServiceSetting_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SettingId](#API_UpdateServiceSetting_RequestSyntax) **   <a name="systemsmanager-UpdateServiceSetting-request-SettingId"></a>
The Amazon Resource Name (ARN) of the service setting to update. For example, `arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled`. The setting ID can be one of the following.
+  `/ssm/appmanager/appmanager-enabled`
+  `/ssm/automation/customer-script-log-destination`
+  `/ssm/automation/customer-script-log-group-name`
+ /ssm/automation/enable-adaptive-concurrency
+  `/ssm/documents/console/public-sharing-permission`
+  `/ssm/managed-instance/activation-tier`
+  `/ssm/managed-instance/default-ec2-instance-management-role`
+  `/ssm/opsinsights/opscenter`
+  `/ssm/parameter-store/default-parameter-tier`
+  `/ssm/parameter-store/high-throughput-enabled`
Permissions to update the `/ssm/managed-instance/default-ec2-instance-management-role` setting should only be provided to administrators. Implement least privilege access when allowing individuals to configure or modify the Default Host Management Configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: Yes

 ** [SettingValue](#API_UpdateServiceSetting_RequestSyntax) **   <a name="systemsmanager-UpdateServiceSetting-request-SettingValue"></a>
The new value to specify for the service setting. The following list specifies the available values for each setting.
+ For `/ssm/appmanager/appmanager-enabled`, enter `True` or `False`.
+ For `/ssm/automation/customer-script-log-destination`, enter `CloudWatch`.
+ For `/ssm/automation/customer-script-log-group-name`, enter the name of an Amazon CloudWatch Logs log group.
+ For `/ssm/documents/console/public-sharing-permission`, enter `Enable` or `Disable`.
+ For `/ssm/managed-instance/activation-tier`, enter `standard` or `advanced`.
+ For `/ssm/managed-instance/default-ec2-instance-management-role`, enter the name of an IAM role.
+  For `/ssm/opsinsights/opscenter`, enter `Enabled` or `Disabled`.
+ For `/ssm/parameter-store/default-parameter-tier`, enter `Standard`, `Advanced`, or `Intelligent-Tiering`
+ For `/ssm/parameter-store/high-throughput-enabled`, enter `true` or `false`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## Response Elements
<a name="API_UpdateServiceSetting_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateServiceSetting_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerError **
An error occurred on the server side.
HTTP Status Code: 500

 ** ServiceSettingNotFound **
The specified service setting wasn't found. Either the service name or the setting hasn't been provisioned by the AWS service team.
HTTP Status Code: 400

 ** TooManyUpdates **
There are concurrent updates for a resource that supports one update at a time.
HTTP Status Code: 400

## Examples
<a name="API_UpdateServiceSetting_Examples"></a>

### Example
<a name="API_UpdateServiceSetting_Example_1"></a>

This example illustrates one usage of UpdateServiceSetting.

#### Sample Request
<a name="API_UpdateServiceSetting_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ssm.us-east-2.amazonaws.com
Accept-Encoding: identity
X-Amz-Target: AmazonSSM.UpdateServiceSetting
Content-Type: application/x-amz-json-1.1
User-Agent: aws-cli/1.17.12 Python/3.6.8 Darwin/18.7.0 botocore/1.14.12
X-Amz-Date: 20240325T154927Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20240325/us-east-2/ssm/aws4_request,
SignedHeaders=content-type;host;x-amz-date;x-amz-target, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 134

{
    "SettingId": "arn:aws:ssm:us-east-2:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled",
    "SettingValue": "true"
}
```

#### Sample Response
<a name="API_UpdateServiceSetting_Example_1_Response"></a>

```
{}
```

## See Also
<a name="API_UpdateServiceSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ssm-2014-11-06/UpdateServiceSetting)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/UpdateServiceSetting)
