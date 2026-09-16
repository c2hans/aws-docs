---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_UpdateHypervisor.html
---

# UpdateHypervisor
<a name="API_UpdateHypervisor"></a>

Updates a hypervisor metadata, including its host, username, and password. Specify which hypervisor to update using the Amazon Resource Name (ARN) of the hypervisor in your request.

## Request Syntax
<a name="API_UpdateHypervisor_RequestSyntax"></a>

```
{
   "Host": "{{string}}",
   "HypervisorArn": "{{string}}",
   "LogGroupArn": "{{string}}",
   "Name": "{{string}}",
   "Password": "{{string}}",
   "Username": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateHypervisor_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Host](#API_UpdateHypervisor_RequestSyntax) **   <a name="bgw-UpdateHypervisor-request-Host"></a>
The updated host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `.+`
Required: No

 ** [HypervisorArn](#API_UpdateHypervisor_RequestSyntax) **   <a name="bgw-UpdateHypervisor-request-HypervisorArn"></a>
The Amazon Resource Name (ARN) of the hypervisor to update.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

 ** [LogGroupArn](#API_UpdateHypervisor_RequestSyntax) **   <a name="bgw-UpdateHypervisor-request-LogGroupArn"></a>
The Amazon Resource Name (ARN) of the group of gateways within the requested log.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `$|^arn:(aws|aws-cn|aws-us-gov):logs:([a-zA-Z0-9-]+):([0-9]+):log-group:[a-zA-Z0-9_\-\/\.]+:\*`
Required: No

 ** [Name](#API_UpdateHypervisor_RequestSyntax) **   <a name="bgw-UpdateHypervisor-request-Name"></a>
The updated name for the hypervisor
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

 ** [Password](#API_UpdateHypervisor_RequestSyntax) **   <a name="bgw-UpdateHypervisor-request-Password"></a>
The updated password for the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[ -~]+`
Required: No

 ** [Username](#API_UpdateHypervisor_RequestSyntax) **   <a name="bgw-UpdateHypervisor-request-Username"></a>
The updated username for the hypervisor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*`
Required: No

## Response Syntax
<a name="API_UpdateHypervisor_ResponseSyntax"></a>

```
{
   "HypervisorArn": "string"
}
```

## Response Elements
<a name="API_UpdateHypervisor_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [HypervisorArn](#API_UpdateHypervisor_ResponseSyntax) **   <a name="bgw-UpdateHypervisor-response-HypervisorArn"></a>
The Amazon Resource Name (ARN) of the hypervisor you updated.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 500.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

## Errors
<a name="API_UpdateHypervisor_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The operation cannot proceed because you have insufficient permissions.
 ** ErrorCode **
A description of why you have insufficient permissions.
HTTP Status Code: 400

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
<a name="API_UpdateHypervisor_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/UpdateHypervisor)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/UpdateHypervisor)
