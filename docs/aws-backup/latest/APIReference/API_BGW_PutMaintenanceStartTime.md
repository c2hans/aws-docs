---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_PutMaintenanceStartTime.html
---

# PutMaintenanceStartTime
<a name="API_BGW_PutMaintenanceStartTime"></a>

Set the maintenance start time for a gateway.

## Request Syntax
<a name="API_BGW_PutMaintenanceStartTime_RequestSyntax"></a>

```
{
   "DayOfMonth": {{number}},
   "DayOfWeek": {{number}},
   "GatewayArn": "{{string}}",
   "HourOfDay": {{number}},
   "MinuteOfHour": {{number}}
}
```

## Request Parameters
<a name="API_BGW_PutMaintenanceStartTime_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DayOfMonth](#API_BGW_PutMaintenanceStartTime_RequestSyntax) **   <a name="Backup-BGW_PutMaintenanceStartTime-request-DayOfMonth"></a>
The day of the month start maintenance on a gateway.
Valid values range from `Sunday` to `Saturday`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 31.
Required: No

 ** [DayOfWeek](#API_BGW_PutMaintenanceStartTime_RequestSyntax) **   <a name="Backup-BGW_PutMaintenanceStartTime-request-DayOfWeek"></a>
The day of the week to start maintenance on a gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 6.
Required: No

 ** [GatewayArn](#API_BGW_PutMaintenanceStartTime_RequestSyntax) **   <a name="Backup-BGW_PutMaintenanceStartTime-request-GatewayArn"></a>
The Amazon Resource Name (ARN) for the gateway, used to specify its maintenance start time.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

 ** [HourOfDay](#API_BGW_PutMaintenanceStartTime_RequestSyntax) **   <a name="Backup-BGW_PutMaintenanceStartTime-request-HourOfDay"></a>
The hour of the day to start maintenance on a gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 23.
Required: Yes

 ** [MinuteOfHour](#API_BGW_PutMaintenanceStartTime_RequestSyntax) **   <a name="Backup-BGW_PutMaintenanceStartTime-request-MinuteOfHour"></a>
The minute of the hour to start maintenance on a gateway.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 59.
Required: Yes

## Response Syntax
<a name="API_BGW_PutMaintenanceStartTime_ResponseSyntax"></a>

```
{
   "GatewayArn": "string"
}
```

## Response Elements
<a name="API_BGW_PutMaintenanceStartTime_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GatewayArn](#API_BGW_PutMaintenanceStartTime_ResponseSyntax) **   <a name="Backup-BGW_PutMaintenanceStartTime-response-GatewayArn"></a>
The Amazon Resource Name (ARN) of a gateway for which you set the maintenance start time.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

## Errors
<a name="API_BGW_PutMaintenanceStartTime_Errors"></a>

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
<a name="API_BGW_PutMaintenanceStartTime_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/PutMaintenanceStartTime)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/PutMaintenanceStartTime)
