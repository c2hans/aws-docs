---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_GetGateway.html
---

# GetGateway
<a name="API_BGW_GetGateway"></a>

By providing the ARN (Amazon Resource Name), this API returns the gateway.

## Request Syntax
<a name="API_BGW_GetGateway_RequestSyntax"></a>

```
{
   "GatewayArn": "{{string}}"
}
```

## Request Parameters
<a name="API_BGW_GetGateway_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayArn](#API_BGW_GetGateway_RequestSyntax) **   <a name="Backup-BGW_GetGateway-request-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

## Response Syntax
<a name="API_BGW_GetGateway_ResponseSyntax"></a>

```
{
   "Gateway": {
      "DeprecationDate": number,
      "GatewayArn": "string",
      "GatewayDisplayName": "string",
      "GatewayType": "string",
      "HypervisorId": "string",
      "LastSeenTime": number,
      "MaintenanceStartTime": {
         "DayOfMonth": number,
         "DayOfWeek": number,
         "HourOfDay": number,
         "MinuteOfHour": number
      },
      "NextUpdateAvailabilityTime": number,
      "SoftwareVersion": "string",
      "VpcEndpoint": "string"
   }
}
```

## Response Elements
<a name="API_BGW_GetGateway_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Gateway](#API_BGW_GetGateway_ResponseSyntax) **   <a name="Backup-BGW_GetGateway-response-Gateway"></a>
By providing the ARN (Amazon Resource Name), this API returns the gateway.
Type: [GatewayDetails](API_BGW_GatewayDetails.md) object

## Errors
<a name="API_BGW_GetGateway_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_BGW_GetGateway_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/GetGateway)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/GetGateway)
