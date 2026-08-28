---
source_url: https://docs.aws.amazon.com/bgw/v20210101/APIReference/API_UpdateGatewayInformation.html
---

# UpdateGatewayInformation
<a name="API_UpdateGatewayInformation"></a>

Updates a gateway's name. Specify which gateway to update using the Amazon Resource Name (ARN) of the gateway in your request.

## Request Syntax
<a name="API_UpdateGatewayInformation_RequestSyntax"></a>

```
{
   "GatewayArn": "{{string}}",
   "GatewayDisplayName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGatewayInformation_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayArn](#API_UpdateGatewayInformation_RequestSyntax) **   <a name="bgw-UpdateGatewayInformation-request-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway to update.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

 ** [GatewayDisplayName](#API_UpdateGatewayInformation_RequestSyntax) **   <a name="bgw-UpdateGatewayInformation-request-GatewayDisplayName"></a>
The updated display name of the gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: No

## Response Syntax
<a name="API_UpdateGatewayInformation_ResponseSyntax"></a>

```
{
   "GatewayArn": "string"
}
```

## Response Elements
<a name="API_UpdateGatewayInformation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayArn](#API_UpdateGatewayInformation_ResponseSyntax) **   <a name="bgw-UpdateGatewayInformation-response-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway you updated.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

## Errors
<a name="API_UpdateGatewayInformation_Errors"></a>

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
<a name="API_UpdateGatewayInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/UpdateGatewayInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/UpdateGatewayInformation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Backup gateway. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bgw` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
