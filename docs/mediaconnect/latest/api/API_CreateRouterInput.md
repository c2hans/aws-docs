---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterInput.html
---

# CreateRouterInput
<a name="API_CreateRouterInput"></a>

Creates a new router input in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_CreateRouterInput_RequestSyntax"></a>

```
POST /v1/routerInput HTTP/1.1
Content-type: application/json

{
   "availabilityZone": "{{string}}",
   "clientToken": "{{string}}",
   "configuration": { ... },
   "contentQualityAnalysisConfiguration": { ... },
   "maintenanceConfiguration": { ... },
   "maximumBitrate": {{number}},
   "name": "{{string}}",
   "regionName": "{{string}}",
   "routingScope": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "tier": "{{string}}",
   "transitEncryption": {
      "encryptionKeyConfiguration": { ... },
      "encryptionKeyType": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateRouterInput_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRouterInput_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-availabilityZone"></a>
The Availability Zone where you want to create the router input. This must be a valid Availability Zone for the region specified by `regionName`, or the current region if no `regionName` is provided.
Type: String
Required: No

 ** [clientToken](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-clientToken"></a>
A unique identifier for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[!-~]+`
Required: No

 ** [configuration](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-configuration"></a>
The configuration settings for the router input, which can include the protocol, network interface, and other details.
Type: [RouterInputConfiguration](API_RouterInputConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [contentQualityAnalysisConfiguration](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-contentQualityAnalysisConfiguration"></a>
The content quality analysis configuration for the router input.
Type: [RouterContentQualityAnalysisConfiguration](API_RouterContentQualityAnalysisConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maintenanceConfiguration](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-maintenanceConfiguration"></a>
The maintenance configuration settings for the router input, including preferred maintenance windows and schedules.
Type: [MaintenanceConfiguration](API_MaintenanceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maximumBitrate](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-maximumBitrate"></a>
The maximum bitrate for the router input.
Type: Long
Required: Yes

 ** [name](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-name"></a>
The name of the router input.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [regionName](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-regionName"></a>
The AWS Region for the router input. Defaults to the current region if not specified.
Type: String
Required: No

 ** [routingScope](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-routingScope"></a>
Specifies whether the router input can be assigned to outputs in different Regions. REGIONAL (default) - connects only to outputs in same Region. GLOBAL - connects to outputs in any Region.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: Yes

 ** [tags](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-tags"></a>
Key-value pairs that can be used to tag and organize this router input.
Type: String to string map
Required: No

 ** [tier](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-tier"></a>
The tier level for the router input.
Type: String
Valid Values: `INPUT_100 | INPUT_50 | INPUT_20`
Required: Yes

 ** [transitEncryption](#API_CreateRouterInput_RequestSyntax) **   <a name="mediaconnect-CreateRouterInput-request-transitEncryption"></a>
The transit encryption settings for the router input.
Type: [RouterInputTransitEncryption](API_RouterInputTransitEncryption.md) object
Required: No

## Response Syntax
<a name="API_CreateRouterInput_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateRouterInput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [routerInput](#API_CreateRouterInput_ResponseSyntax) **   <a name="mediaconnect-CreateRouterInput-response-routerInput"></a>
The newly-created router input.
Type: [RouterInput](API_RouterInput.md) object

## Errors
<a name="API_CreateRouterInput_Errors"></a>

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

 ** RouterInputServiceQuotaExceededException **
The request to create a new router input would exceed the service quotas for the account.
HTTP Status Code: 420

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_CreateRouterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/CreateRouterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/CreateRouterInput)
