---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_ListRouterInputs.html
---

# ListRouterInputs
<a name="API_ListRouterInputs"></a>

Retrieves a list of router inputs in AWS Elemental MediaConnect.

## Request Syntax
<a name="API_ListRouterInputs_RequestSyntax"></a>

```
POST /v1/routerInputs?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
Content-type: application/json

{
   "filters": [
      { ... }
   ]
}
```

## URI Request Parameters
<a name="API_ListRouterInputs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListRouterInputs_RequestSyntax) **   <a name="mediaconnect-ListRouterInputs-request-uri-maxResults"></a>
The maximum number of router inputs to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListRouterInputs_RequestSyntax) **   <a name="mediaconnect-ListRouterInputs-request-uri-nextToken"></a>
A token used to retrieve the next page of results.

## Request Body
<a name="API_ListRouterInputs_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filters](#API_ListRouterInputs_RequestSyntax) **   <a name="mediaconnect-ListRouterInputs-request-filters"></a>
The filters to apply when retrieving the list of router inputs.
Type: Array of [RouterInputFilter](API_RouterInputFilter.md) objects
Required: No

## Response Syntax
<a name="API_ListRouterInputs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "routerInputs": [
      {
         "arn": "string",
         "availabilityZone": "string",
         "createdAt": "string",
         "id": "string",
         "inputType": "string",
         "maintenanceSchedule": { ... },
         "maintenanceScheduleType": "string",
         "maximumBitrate": number,
         "messageCount": number,
         "name": "string",
         "networkInterfaceArn": "string",
         "regionName": "string",
         "routedOutputs": number,
         "routingScope": "string",
         "state": "string",
         "updatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListRouterInputs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListRouterInputs_ResponseSyntax) **   <a name="mediaconnect-ListRouterInputs-response-nextToken"></a>
The token to use to retrieve the next page of results.
Type: String

 ** [routerInputs](#API_ListRouterInputs_ResponseSyntax) **   <a name="mediaconnect-ListRouterInputs-response-routerInputs"></a>
The summary information for the retrieved router inputs.
Type: Array of [ListedRouterInput](API_ListedRouterInput.md) objects

## Errors
<a name="API_ListRouterInputs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
This exception is thrown if the request contains a semantic error. The precise meaning depends on the API, and is documented in the error message.
HTTP Status Code: 400

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
HTTP Status Code: 409

 ** InternalServerErrorException **
The server encountered an internal error and is unable to complete the request.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable or busy.
HTTP Status Code: 503

 ** TooManyRequestsException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_ListRouterInputs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediaconnect-2018-11-14/ListRouterInputs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/ListRouterInputs)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
