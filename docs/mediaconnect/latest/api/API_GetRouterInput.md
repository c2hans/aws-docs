---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInput.html
---

# GetRouterInput
<a name="API_GetRouterInput"></a>

Retrieves information about a specific router input in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_GetRouterInput_RequestSyntax"></a>

```
GET /v1/routerInput/{{arn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRouterInput_RequestParameters"></a>

The request uses the following URI parameters.

 ** [arn](#API_GetRouterInput_RequestSyntax) **   <a name="mediaconnect-GetRouterInput-request-uri-arn"></a>
The Amazon Resource Name (ARN) of the router input to retrieve information about.
Pattern: `arn:(aws[a-zA-Z-]*):mediaconnect:[a-z0-9-]+:[0-9]{12}:routerInput:[a-z0-9]{12}`
Required: Yes

## Request Body
<a name="API_GetRouterInput_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRouterInput_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetRouterInput_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [routerInput](#API_GetRouterInput_ResponseSyntax) **   <a name="mediaconnect-GetRouterInput-response-routerInput"></a>
The details of the requested router input, including its configuration, state, and other attributes.
Type: [RouterInput](API_RouterInput.md) object

## Errors
<a name="API_GetRouterInput_Errors"></a>

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
<a name="API_GetRouterInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/GetRouterInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/GetRouterInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
