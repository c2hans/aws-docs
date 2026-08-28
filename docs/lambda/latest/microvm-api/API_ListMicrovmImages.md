---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListMicrovmImages.html
---

# ListMicrovmImages
<a name="API_ListMicrovmImages"></a>

Lists MicroVM images in the account with optional name filtering. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListMicrovmImages_RequestSyntax"></a>

```
GET /2025-09-09/microvm-images?maxResults={{maxResults}}&nameFilter={{nameFilter}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMicrovmImages_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListMicrovmImages_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImages-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nameFilter](#API_ListMicrovmImages_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImages-request-uri-nameFilter"></a>
Filters images whose name contains the specified string.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`

 ** [nextToken](#API_ListMicrovmImages_RequestSyntax) **   <a name="lambdamicrovm-ListMicrovmImages-request-uri-nextToken"></a>
The pagination token from a previous call. Use this token to retrieve the next page of results.

## Request Body
<a name="API_ListMicrovmImages_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMicrovmImages_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": number,
         "imageArn": "string",
         "latestActiveImageVersion": "string",
         "latestFailedImageVersion": "string",
         "name": "string",
         "state": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMicrovmImages_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListMicrovmImages_ResponseSyntax) **   <a name="lambdamicrovm-ListMicrovmImages-response-items"></a>
The list of MicroVM images.
Type: Array of [MicrovmImageSummary](API_MicrovmImageSummary.md) objects

 ** [nextToken](#API_ListMicrovmImages_ResponseSyntax) **   <a name="lambdamicrovm-ListMicrovmImages-response-nextToken"></a>
The pagination token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

## Errors
<a name="API_ListMicrovmImages_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal server error occurred. Retry the request later.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

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
<a name="API_ListMicrovmImages_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/ListMicrovmImages)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/ListMicrovmImages)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
