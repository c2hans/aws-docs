---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSerialConsoleAccessStatus.html
---

# GetSerialConsoleAccessStatus
<a name="API_GetSerialConsoleAccessStatus"></a>

Retrieves the access status of your account to the EC2 serial console of all instances. By default, access to the EC2 serial console is disabled for your account. For more information, see [Manage account access to the EC2 serial console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html#serial-console-account-access) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_GetSerialConsoleAccessStatus_RequestParameters"></a>

For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_GetSerialConsoleAccessStatus_ResponseElements"></a>

The following elements are returned by the service.

 **managedBy**
The entity that manages access to the serial console. Possible values include:
+  `account` - Access is managed by the account.
+  `declarative-policy` - Access is managed by a declarative policy and can't be modified by the account.
Type: String
Valid Values: `account | declarative-policy`

 **requestId**
The ID of the request.
Type: String

 **serialConsoleAccessEnabled**
If `true`, access to the EC2 serial console of all instances is enabled for your account. If `false`, access to the EC2 serial console of all instances is disabled for your account.
Type: Boolean

## Errors
<a name="API_GetSerialConsoleAccessStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetSerialConsoleAccessStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetSerialConsoleAccessStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetSerialConsoleAccessStatus)
