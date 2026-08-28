---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ListManagedMicrovmImageVersions.html
---

# ListManagedMicrovmImageVersions
<a name="API_ListManagedMicrovmImageVersions"></a>

Lists versions of a managed MicroVM image. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Syntax
<a name="API_ListManagedMicrovmImageVersions_RequestSyntax"></a>

```
GET /2025-09-09/managed-microvm-images/{{imageIdentifier}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListManagedMicrovmImageVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [imageIdentifier](#API_ListManagedMicrovmImageVersions_RequestSyntax) **   <a name="lambdamicrovm-ListManagedMicrovmImageVersions-request-uri-imageIdentifier"></a>
The unique identifier (ARN or ID) of the managed MicroVM image to list versions for.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [maxResults](#API_ListManagedMicrovmImageVersions_RequestSyntax) **   <a name="lambdamicrovm-ListManagedMicrovmImageVersions-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListManagedMicrovmImageVersions_RequestSyntax) **   <a name="lambdamicrovm-ListManagedMicrovmImageVersions-request-uri-nextToken"></a>
The pagination token from a previous call. Use this token to retrieve the next page of results.

## Request Body
<a name="API_ListManagedMicrovmImageVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListManagedMicrovmImageVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": number,
         "imageArn": "string",
         "imageVersion": "string",
         "updatedAt": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListManagedMicrovmImageVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListManagedMicrovmImageVersions_ResponseSyntax) **   <a name="lambdamicrovm-ListManagedMicrovmImageVersions-response-items"></a>
The list of managed MicroVM image versions.
Type: Array of [ManagedMicrovmImageVersion](API_ManagedMicrovmImageVersion.md) objects

 ** [nextToken](#API_ListManagedMicrovmImageVersions_ResponseSyntax) **   <a name="lambdamicrovm-ListManagedMicrovmImageVersions-response-nextToken"></a>
The pagination token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.
Type: String

## Errors
<a name="API_ListManagedMicrovmImageVersions_Errors"></a>

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
<a name="API_ListManagedMicrovmImageVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/ListManagedMicrovmImageVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
