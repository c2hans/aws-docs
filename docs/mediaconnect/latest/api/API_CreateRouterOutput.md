---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterOutput.html
---

# CreateRouterOutput
<a name="API_CreateRouterOutput"></a>

Creates a new router output in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_CreateRouterOutput_RequestSyntax"></a>

```
POST /v1/routerOutput HTTP/1.1
Content-type: application/json

{
   "availabilityZone": "{{string}}",
   "clientToken": "{{string}}",
   "configuration": { ... },
   "fabricConfiguration": {
      "recoveryLatencyMode": "{{string}}"
   },
   "maintenanceConfiguration": { ... },
   "maximumBitrate": {{number}},
   "name": "{{string}}",
   "regionName": "{{string}}",
   "routingScope": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "tier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRouterOutput_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateRouterOutput_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [availabilityZone](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-availabilityZone"></a>
The Availability Zone where you want to create the router output. This must be a valid Availability Zone for the region specified by `regionName`, or the current region if no `regionName` is provided.
Type: String
Required: No

 ** [clientToken](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-clientToken"></a>
A unique identifier for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[!-~]+`
Required: No

 ** [configuration](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-configuration"></a>
The configuration settings for the router output.
Type: [RouterOutputConfiguration](API_RouterOutputConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [fabricConfiguration](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-fabricConfiguration"></a>
The fabric configuration settings for the router output.
Type: [FabricConfiguration](API_FabricConfiguration.md) object
Required: No

 ** [maintenanceConfiguration](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-maintenanceConfiguration"></a>
The maintenance configuration settings for the router output, including preferred maintenance windows and schedules.
Type: [MaintenanceConfiguration](API_MaintenanceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [maximumBitrate](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-maximumBitrate"></a>
The maximum bitrate for the router output.
Type: Long
Required: Yes

 ** [name](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-name"></a>
The name of the router output.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** [regionName](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-regionName"></a>
The AWS Region for the router output. Defaults to the current region if not specified.
Type: String
Required: No

 ** [routingScope](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-routingScope"></a>
Specifies whether the router output can take inputs that are in different Regions. REGIONAL (default) - can only take inputs from same Region. GLOBAL - can take inputs from any Region.
Type: String
Valid Values: `REGIONAL | GLOBAL`
Required: Yes

 ** [tags](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-tags"></a>
Key-value pairs that can be used to tag this router output.
Type: String to string map
Required: No

 ** [tier](#API_CreateRouterOutput_RequestSyntax) **   <a name="mediaconnect-CreateRouterOutput-request-tier"></a>
The tier level for the router output.
Type: String
Valid Values: `OUTPUT_100 | OUTPUT_50 | OUTPUT_20`
Required: Yes

## Response Syntax
<a name="API_CreateRouterOutput_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "routerOutput": {
      "arn": "string",
      "availabilityZone": "string",
      "configuration": { ... },
      "createdAt": "string",
      "fabricConfiguration": {
         "recoveryLatencyMode": "string"
      },
      "id": "string",
      "ipAddress": "string",
      "maintenanceConfiguration": { ... },
      "maintenanceSchedule": { ... },
      "maintenanceScheduleType": "string",
      "maintenanceType": "string",
      "maximumBitrate": number,
      "messages": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "name": "string",
      "outputType": "string",
      "regionName": "string",
      "routedInputArn": "string",
      "routedState": "string",
      "routingScope": "string",
      "state": "string",
      "streamDetails": { ... },
      "tags": {
         "string" : "string"
      },
      "tier": "string",
      "updatedAt": "string"
   }
}
```

## Response Elements
<a name="API_CreateRouterOutput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [routerOutput](#API_CreateRouterOutput_ResponseSyntax) **   <a name="mediaconnect-CreateRouterOutput-response-routerOutput"></a>
The newly-created router output.
Type: [RouterOutput](API_RouterOutput.md) object

## Errors
<a name="API_CreateRouterOutput_Errors"></a>

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

 ** RouterOutputServiceQuotaExceededException **
The request to create a new router output would exceed the service quotas (limits) set for the account.
HTTP Status Code: 420

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_CreateRouterOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/CreateRouterOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/CreateRouterOutput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
