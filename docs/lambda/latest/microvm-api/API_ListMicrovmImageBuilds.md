---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImageBuilds.html
---

# ListMicrovmImageBuilds
<a name="API_ListMicrovmImageBuilds"></a>

Lists builds for a MicroVM image version with optional filtering by architecture and chipset. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListMicrovmImageBuilds_RequestSyntax"></a>

```
GET /2025-09-09/microvm-images/{{imageIdentifier}}/versions/{{imageVersion}}/builds?architecture={{architecture}}&chipset={{chipset}}&chipsetGeneration={{chipsetGeneration}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMicrovmImageBuilds_RequestParameters"></a>

The request uses the following URI parameters.

 ** [architecture](#API_ListMicrovmImageBuilds_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-request-uri-architecture"></a>
Filters builds by target CPU architecture.
Valid Values: `ARM_64`

 ** [chipset](#API_ListMicrovmImageBuilds_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-request-uri-chipset"></a>
Filters builds by target chipset.
Valid Values: `GRAVITON`

 ** [chipsetGeneration](#API_ListMicrovmImageBuilds_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-request-uri-chipsetGeneration"></a>
Filters builds by target chipset generation.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [imageIdentifier](#API_ListMicrovmImageBuilds_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-request-uri-imageIdentifier"></a>
The unique identifier (ARN or ID) of the MicroVM image.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [imageVersion](#API_ListMicrovmImageBuilds_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-request-uri-imageVersion"></a>
The version of the MicroVM image to list builds for.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** [maxResults](#API_ListMicrovmImageBuilds_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListMicrovmImageBuilds_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-request-uri-nextToken"></a>
The pagination token from a previous call. Use this token to retrieve the next page of results.

## Request Body
<a name="API_ListMicrovmImageBuilds_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMicrovmImageBuilds_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "architecture": "string",
         "buildId": "string",
         "buildState": "string",
         "chipset": "string",
         "chipsetGeneration": "string",
         "createdAt": number,
         "imageArn": "string",
         "imageVersion": "string",
         "stateReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMicrovmImageBuilds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListMicrovmImageBuilds_ResponseSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-response-items"></a>
The list of MicroVM image builds.
Type: Array of [MicrovmImageBuildSummary](API_MicrovmImageBuildSummary.md) objects

 ** [nextToken](#API_ListMicrovmImageBuilds_ResponseSyntax) **   <a name="lambdamicrovm-ListMicrovmImageBuilds-response-nextToken"></a>
The pagination token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

## Errors
<a name="API_ListMicrovmImageBuilds_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry the request later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of the resource that was not found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling. Retry the request later.
 ** quotaCode **
The quota code of the throttled service quota.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The service code of the throttled service quota.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by the service.
HTTP Status Code: 400

## See Also
<a name="API_ListMicrovmImageBuilds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/ListMicrovmImageBuilds)
