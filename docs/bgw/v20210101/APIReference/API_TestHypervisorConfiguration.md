---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_TestHypervisorConfiguration.html
---

# TestHypervisorConfiguration
<a name="API_TestHypervisorConfiguration"></a>

Tests your hypervisor configuration to validate that backup gateway can connect with the hypervisor and its resources.

## Request Syntax
<a name="API_TestHypervisorConfiguration_RequestSyntax"></a>

```
{
   "GatewayArn": "{{string}}",
   "Host": "{{string}}",
   "Password": "{{string}}",
   "Username": "{{string}}"
}
```

## Request Parameters
<a name="API_TestHypervisorConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayArn](#API_TestHypervisorConfiguration_RequestSyntax) **   <a name="bgw-TestHypervisorConfiguration-request-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway to the hypervisor to test.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

 ** [Host](#API_TestHypervisorConfiguration_RequestSyntax) **   <a name="bgw-TestHypervisorConfiguration-request-Host"></a>
The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `.+`
Required: Yes

 ** [Password](#API_TestHypervisorConfiguration_RequestSyntax) **   <a name="bgw-TestHypervisorConfiguration-request-Password"></a>
The password for the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[ -~]+`
Required: No

 ** [Username](#API_TestHypervisorConfiguration_RequestSyntax) **   <a name="bgw-TestHypervisorConfiguration-request-Username"></a>
The username for the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*`
Required: No

## Response Elements
<a name="API_TestHypervisorConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TestHypervisorConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The operation cannot proceed because it is not supported.
 ** ErrorCode **
A description of why the operation is not supported.
HTTP Status Code: 400

 ** InternalServerException **
The operation did not succeed because an internal error occurred. Try again later.
 ** ErrorCode **
A description of which internal error occured.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A resource that is required for the action wasn't found.
 ** ErrorCode **
A description of which resource wasn't found.
HTTP Status Code: 400

 ** ThrottlingException **
TPS has been limited to protect against intentional or unintentional high request volumes.
 ** ErrorCode **
Error: TPS has been limited to protect against intentional or unintentional high request volumes.
HTTP Status Code: 400

 ** ValidationException **
The operation did not succeed because a validation error occurred.
 ** ErrorCode **
A description of what caused the validation error.
HTTP Status Code: 400

## See Also
<a name="API_TestHypervisorConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/TestHypervisorConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/TestHypervisorConfiguration)
