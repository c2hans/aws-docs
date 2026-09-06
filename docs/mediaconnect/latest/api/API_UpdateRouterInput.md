---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterInput.html
---

# UpdateRouterInput
<a name="API_UpdateRouterInput"></a>

Updates the configuration of an existing router input in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_UpdateRouterInput_RequestSyntax"></a>

```
PUT /v1/routerInput/{{arn}} HTTP/1.1
Content-type: application/json

{
   "configuration": { ... },
   "contentQualityAnalysisConfiguration": { ... },
   "maintenanceConfiguration": { ... },
   "maximumBitrate": {{number}},
   "name": "{{string}}",
   "routingScope": "{{string}}",
   "tier": "{{string}}",
   "transitEncryption": {
      "encryptionKeyConfiguration": { ... },
      "encryptionKeyType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateRouterInput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the router input that you want to update.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_UpdateRouterInput_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [configuration](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-configuration"></a>
The updated configuration settings for the router input. Changing the type of the configuration is not supported.
Type: [RouterInputConfiguration](API_RouterInputConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [contentQualityAnalysisConfiguration](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-contentQualityAnalysisConfiguration"></a>
The content quality analysis configuration for the router input.
Type: [RouterContentQualityAnalysisConfiguration](API_RouterContentQualityAnalysisConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maintenanceConfiguration](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-maintenanceConfiguration"></a>
The updated maintenance configuration settings for the router input, including any changes to preferred maintenance windows and schedules.
Type: [MaintenanceConfiguration](API_MaintenanceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maximumBitrate](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-maximumBitrate"></a>
The updated maximum bitrate for the router input.
Type: Long
Required: No

 ** [name](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-name"></a>
The updated name for the router input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** [routingScope](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-routingScope"></a>
Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - can be assigned only to outputs in the same Region. GLOBAL - can be assigned to outputs in any Region.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: No

 ** [tier](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-tier"></a>
The updated tier level for the router input.
Type: String
Valid Values: `INPUT_100 | INPUT_50 | INPUT_20`
Required: No

 ** [transitEncryption](#API_UpdateRouterInput_RequestSyntax) **   <a name="mediaconnect-UpdateRouterInput-request-transitEncryption"></a>
The updated transit encryption settings for the router input.
Type: [RouterInputTransitEncryption](API_RouterInputTransitEncryption.md) object
Required: No

## Response Syntax
<a name="API_UpdateRouterInput_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "routerInput": {
      "arn": "string",
      "availabilityZone": "string",
      "configuration": { ... },
      "contentQualityAnalysisConfiguration": { ... },
      "contentQualityAnalysisType": "string",
      "createdAt": "string",
      "id": "string",
      "inputType": "string",
      "ipAddress": "string",
      "maintenanceConfiguration": { ... },
      "maintenanceSchedule": { ... },
      "maintenanceScheduleType": "string",
      "maintenanceType": "string",
      "maximumBitrate": number,
      "maximumRoutedOutputs": number,
      "messages": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "name": "string",
      "regionName": "string",
      "routedOutputs": number,
      "routingScope": "string",
      "state": "string",
      "streamDetails": { ... },
      "tags": {
         "string" : "string"
      },
      "tier": "string",
      "transitEncryption": {
         "encryptionKeyConfiguration": { ... },
         "encryptionKeyType": "string"
      },
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_UpdateRouterInput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [routerInput](#API_UpdateRouterInput_ResponseSyntax) **   <a name="mediaconnect-UpdateRouterInput-response-routerInput"></a>
The updated router input.
Type: [RouterInput](API_RouterInput.md) object

## Errors
<a name="API_UpdateRouterInput_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** ForbiddenException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_UpdateRouterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/UpdateRouterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/UpdateRouterInput)
