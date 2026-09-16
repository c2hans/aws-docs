---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_CreateGateway.html
---

# CreateGateway
<a name="API_BGW_CreateGateway"></a>

Creates a backup gateway. After you create a gateway, you can associate it with a server using the `AssociateGatewayToServer` operation.

## Request Syntax
<a name="API_BGW_CreateGateway_RequestSyntax"></a>

```
{
   "ActivationKey": "{{string}}",
   "GatewayDisplayName": "{{string}}",
   "GatewayType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_BGW_CreateGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ActivationKey](#API_BGW_CreateGateway_RequestSyntax) **   <a name="Backup-BGW_CreateGateway-request-ActivationKey"></a>
The activation key of the created gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `[0-9a-zA-Z\-]+`
Required: Yes

 ** [GatewayDisplayName](#API_BGW_CreateGateway_RequestSyntax) **   <a name="Backup-BGW_CreateGateway-request-GatewayDisplayName"></a>
The display name of the created gateway.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[a-zA-Z0-9-]*`
Required: Yes

 ** [GatewayType](#API_BGW_CreateGateway_RequestSyntax) **   <a name="Backup-BGW_CreateGateway-request-GatewayType"></a>
The type of created gateway.
Type: String
Valid Values: `BACKUP_VM`
Required: Yes

 ** [Tags](#API_BGW_CreateGateway_RequestSyntax) **   <a name="Backup-BGW_CreateGateway-request-Tags"></a>
A list of up to 50 tags to assign to the gateway. Each tag is a key-value pair.
Type: Array of [Tag](API_BGW_Tag.md) objects
Required: No

## Response Syntax
<a name="API_BGW_CreateGateway_ResponseSyntax"></a>

```
{
   "GatewayArn": "string"
}
```

## Response Elements
<a name="API_BGW_CreateGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayArn](#API_BGW_CreateGateway_ResponseSyntax) **   <a name="Backup-BGW_CreateGateway-response-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway you create.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

## Errors
<a name="API_BGW_CreateGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The operation did not succeed because an internal error occurred. Try again later.
 ** ErrorCode **
A description of which internal error occured.
HTTP Status Code: 500

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
<a name="API_BGW_CreateGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/CreateGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/CreateGateway)
