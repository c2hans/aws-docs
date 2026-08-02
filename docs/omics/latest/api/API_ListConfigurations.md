---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_ListConfigurations.html
---

# ListConfigurations
<a name="API_ListConfigurations"></a>

List all configurations for the account.

## Request Syntax
<a name="API_ListConfigurations_RequestSyntax"></a>

```
GET /configuration?maxResults={{maxResults}}&startingToken={{startingToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConfigurations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListConfigurations_RequestSyntax) **   <a name="omics-ListConfigurations-request-uri-maxResults"></a>
Maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 10.

 ** [startingToken](#API_ListConfigurations_RequestSyntax) **   <a name="omics-ListConfigurations-request-uri-startingToken"></a>
Pagination token for retrieving next page of results.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Request Body
<a name="API_ListConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "arn": "string",
         "creationTime": "string",
         "description": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListConfigurations_ResponseSyntax) **   <a name="omics-ListConfigurations-response-items"></a>
List of configuration items.
Type: Array of [ConfigurationListItem](API_ConfigurationListItem.md) objects

 ** [nextToken](#API_ListConfigurations_ResponseSyntax) **   <a name="omics-ListConfigurations-response-nextToken"></a>
Token for retrieving next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

## Errors
<a name="API_ListConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/ListConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/ListConfigurations)
