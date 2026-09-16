---
source_url: https://docs.aws.amazon.com/ec2-instance-connect/latest/APIReference/API_SendSerialConsoleSSHPublicKey.html
---

# SendSerialConsoleSSHPublicKey
<a name="API_SendSerialConsoleSSHPublicKey"></a>

Pushes an SSH public key to the specified EC2 instance. The key remains for 60 seconds, which gives you 60 seconds to establish a serial console connection to the instance using SSH. For more information, see [EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html) in the *Amazon EC2 User Guide*.

## Request Syntax
<a name="API_SendSerialConsoleSSHPublicKey_RequestSyntax"></a>

```
{
   "InstanceId": "{{string}}",
   "SerialPort": {{number}},
   "SSHPublicKey": "{{string}}"
}
```

## Request Parameters
<a name="API_SendSerialConsoleSSHPublicKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SendSerialConsoleSSHPublicKey_RequestSyntax) **   <a name="ec2instanceconnect-SendSerialConsoleSSHPublicKey-request-InstanceId"></a>
The ID of the EC2 instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `^i-[a-f0-9]+$`
Required: Yes

 ** [SerialPort](#API_SendSerialConsoleSSHPublicKey_RequestSyntax) **   <a name="ec2instanceconnect-SendSerialConsoleSSHPublicKey-request-SerialPort"></a>
The serial port of the EC2 instance. Currently only port 0 is supported.
Default: 0
Type: Integer
Valid Range: Fixed value of 0.
Required: No

 ** [SSHPublicKey](#API_SendSerialConsoleSSHPublicKey_RequestSyntax) **   <a name="ec2instanceconnect-SendSerialConsoleSSHPublicKey-request-SSHPublicKey"></a>
The public key material. To use the public key, you must have the matching private key. For information about the supported key formats and lengths, see [Requirements for key pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws) in the *Amazon EC2 User Guide*.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 4096.
Required: Yes

## Response Syntax
<a name="API_SendSerialConsoleSSHPublicKey_ResponseSyntax"></a>

```
{
   "RequestId": "string",
   "Success": boolean
}
```

## Response Elements
<a name="API_SendSerialConsoleSSHPublicKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_SendSerialConsoleSSHPublicKey_ResponseSyntax) **   <a name="ec2instanceconnect-SendSerialConsoleSSHPublicKey-response-RequestId"></a>
The ID of the request. Please provide this ID when contacting AWS Support for assistance.
Type: String

 ** [Success](#API_SendSerialConsoleSSHPublicKey_ResponseSyntax) **   <a name="ec2instanceconnect-SendSerialConsoleSSHPublicKey-response-Success"></a>
Is true if the request succeeds and an error otherwise.
Type: Boolean

## Errors
<a name="API_SendSerialConsoleSSHPublicKey_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthException **
Either your AWS credentials are not valid or you do not have access to the EC2 instance.
HTTP Status Code: 400

 ** EC2InstanceNotFoundException **
The specified instance was not found.
HTTP Status Code: 400

 ** EC2InstanceStateInvalidException **
Unable to connect because the instance is not in a valid state. Connecting to a stopped or terminated instance is not supported. If the instance is stopped, start your instance, and try to connect again.
HTTP Status Code: 400

 ** EC2InstanceTypeInvalidException **
The instance type is not supported for connecting via the serial console. Only Nitro instance types are currently supported.
HTTP Status Code: 400

 ** EC2InstanceUnavailableException **
The instance is currently unavailable. Wait a few minutes and try again.
HTTP Status Code: 400

 ** InvalidArgsException **
One of the parameters is not valid.
HTTP Status Code: 400

 ** SerialConsoleAccessDisabledException **
Your account is not authorized to use the EC2 Serial Console. To authorize your account, run the EnableSerialConsoleAccess API. For more information, see [EnableSerialConsoleAccess](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableSerialConsoleAccess.html) in the *Amazon EC2 API Reference*.
HTTP Status Code: 400

 ** SerialConsoleSessionLimitExceededException **
The instance currently has 1 active serial console session. Only 1 session is supported at a time.
HTTP Status Code: 400

 ** SerialConsoleSessionUnavailableException **
Unable to start a serial console session. Please try again.
HTTP Status Code: 500

 ** ServiceException **
The service encountered an error. Follow the instructions in the error message and try again.
HTTP Status Code: 500

 ** ThrottlingException **
The requests were made too frequently and have been throttled. Wait a while and try again. To increase the limit on your request frequency, contact AWS Support.
HTTP Status Code: 400

## See Also
<a name="API_SendSerialConsoleSSHPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-instance-connect-2018-04-02/SendSerialConsoleSSHPublicKey)
