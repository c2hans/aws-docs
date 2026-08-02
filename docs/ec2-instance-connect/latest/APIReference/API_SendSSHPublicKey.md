---
source_url: https://docs.aws.amazon.com/ec2-instance-connect/latest/APIReference/API_SendSSHPublicKey.html
---

# SendSSHPublicKey
<a name="API_SendSSHPublicKey"></a>

Pushes an SSH public key to the specified EC2 instance for use by the specified user. The key remains for 60 seconds. For more information, see [Connect to your Linux instance using EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html) in the *Amazon EC2 User Guide*.

## Request Syntax
<a name="API_SendSSHPublicKey_RequestSyntax"></a>

```
{
   "AvailabilityZone": "{{string}}",
   "InstanceId": "{{string}}",
   "InstanceOSUser": "{{string}}",
   "SSHPublicKey": "{{string}}"
}
```

## Request Parameters
<a name="API_SendSSHPublicKey_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AvailabilityZone](#API_SendSSHPublicKey_RequestSyntax) **   <a name="ec2instanceconnect-SendSSHPublicKey-request-AvailabilityZone"></a>
The Availability Zone in which the EC2 instance was launched.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 32.
Pattern: `^(\w+-){2,3}\d+\w+$`
Required: No

 ** [InstanceId](#API_SendSSHPublicKey_RequestSyntax) **   <a name="ec2instanceconnect-SendSSHPublicKey-request-InstanceId"></a>
The ID of the EC2 instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 32.
Pattern: `^i-[a-f0-9]+$`
Required: Yes

 ** [InstanceOSUser](#API_SendSSHPublicKey_RequestSyntax) **   <a name="ec2instanceconnect-SendSSHPublicKey-request-InstanceOSUser"></a>
The OS user on the EC2 instance for whom the key can be used to authenticate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[A-Za-z_][A-Za-z0-9\@\._-]{0,30}[A-Za-z0-9\$_-]?$`
Required: Yes

 ** [SSHPublicKey](#API_SendSSHPublicKey_RequestSyntax) **   <a name="ec2instanceconnect-SendSSHPublicKey-request-SSHPublicKey"></a>
The public key material. To use the public key, you must have the matching private key.
Type: String
Length Constraints: Minimum length of 80. Maximum length of 4096.
Required: Yes

## Response Syntax
<a name="API_SendSSHPublicKey_ResponseSyntax"></a>

```
{
   "RequestId": "string",
   "Success": boolean
}
```

## Response Elements
<a name="API_SendSSHPublicKey_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RequestId](#API_SendSSHPublicKey_ResponseSyntax) **   <a name="ec2instanceconnect-SendSSHPublicKey-response-RequestId"></a>
The ID of the request. Please provide this ID when contacting AWS Support for assistance.
Type: String

 ** [Success](#API_SendSSHPublicKey_ResponseSyntax) **   <a name="ec2instanceconnect-SendSSHPublicKey-response-Success"></a>
Is true if the request succeeds and an error otherwise.
Type: Boolean

## Errors
<a name="API_SendSSHPublicKey_Errors"></a>

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

 ** EC2InstanceUnavailableException **
The instance is currently unavailable. Wait a few minutes and try again.
HTTP Status Code: 400

 ** InvalidArgsException **
One of the parameters is not valid.
HTTP Status Code: 400

 ** ServiceException **
The service encountered an error. Follow the instructions in the error message and try again.
HTTP Status Code: 500

 ** ThrottlingException **
The requests were made too frequently and have been throttled. Wait a while and try again. To increase the limit on your request frequency, contact AWS Support.
HTTP Status Code: 400

## Examples
<a name="API_SendSSHPublicKey_Examples"></a>

### Push an SSH public key to an instance
<a name="API_SendSSHPublicKey_Example_1"></a>

This example sends the specified SSH public key to the specified instance in the specified Availability Zone. The key is used to authenticate the specified user.

#### Sample Request
<a name="API_SendSSHPublicKey_Example_1_Request"></a>

```
POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: AWSEC2InstanceConnectService.SendSSHPublicKey

{
   "AvailabilityZone": "us-east-2b",
   "InstanceId": "i-1234567890abcdef0",
   "InstanceOSUser": "ec2-user",
   "SSHPublicKey": "<ssh-public-key-material>"
}
```

## See Also
<a name="API_SendSSHPublicKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-instance-connect-2018-04-02/SendSSHPublicKey)
