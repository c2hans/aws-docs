---
source_url: https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_BGW_GetBandwidthRateLimitSchedule.html
---

# GetBandwidthRateLimitSchedule
<a name="API_BGW_GetBandwidthRateLimitSchedule"></a>

Retrieves the bandwidth rate limit schedule for a specified gateway. By default, gateways do not have bandwidth rate limit schedules, which means no bandwidth rate limiting is in effect. Use this to get a gateway's bandwidth rate limit schedule.

## Request Syntax
<a name="API_BGW_GetBandwidthRateLimitSchedule_RequestSyntax"></a>

```
{
   "GatewayArn": "{{string}}"
}
```

## Request Parameters
<a name="API_BGW_GetBandwidthRateLimitSchedule_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [GatewayArn](#API_BGW_GetBandwidthRateLimitSchedule_RequestSyntax) **   <a name="Backup-BGW_GetBandwidthRateLimitSchedule-request-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [`ListGateways`](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html) operation to return a list of gateways for your account and AWS Region.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`
Required: Yes

## Response Syntax
<a name="API_BGW_GetBandwidthRateLimitSchedule_ResponseSyntax"></a>

```
{
   "BandwidthRateLimitIntervals": [
      {
         "AverageUploadRateLimitInBitsPerSec": number,
         "DaysOfWeek": [ number ],
         "EndHourOfDay": number,
         "EndMinuteOfHour": number,
         "StartHourOfDay": number,
         "StartMinuteOfHour": number
      }
   ],
   "GatewayArn": "string"
}
```

## Response Elements
<a name="API_BGW_GetBandwidthRateLimitSchedule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [BandwidthRateLimitIntervals](#API_BGW_GetBandwidthRateLimitSchedule_ResponseSyntax) **   <a name="Backup-BGW_GetBandwidthRateLimitSchedule-response-BandwidthRateLimitIntervals"></a>
An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty.
Type: Array of [BandwidthRateLimitInterval](API_BGW_BandwidthRateLimitInterval.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.

 ** [GatewayArn](#API_BGW_GetBandwidthRateLimitSchedule_ResponseSyntax) **   <a name="Backup-BGW_GetBandwidthRateLimitSchedule-response-GatewayArn"></a>
The Amazon Resource Name (ARN) of the gateway. Use the [`ListGateways`](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BGW_ListGateways.html) operation to return a list of gateways for your account and AWS Region.
Type: String
Length Constraints: Minimum length of 50. Maximum length of 180.
Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

## Errors
<a name="API_BGW_GetBandwidthRateLimitSchedule_Errors"></a>

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
<a name="API_BGW_GetBandwidthRateLimitSchedule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/backup-gateway-2021-01-01/GetBandwidthRateLimitSchedule)
