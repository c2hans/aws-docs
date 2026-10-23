---
source_url: https://docs.aws.amazon.com/continuum/latest/APIReference/API_ListAssociatedEnvironments.html
---

# ListAssociatedEnvironments
<a name="API_ListAssociatedEnvironments"></a>

Lists the Environments currently associated with one Collector in lexicographically ascending environmentArn order. The ARN identifies each Environment across accounts within the Collector's Region.

## Request Syntax
<a name="API_ListAssociatedEnvironments_RequestSyntax"></a>

```
GET /collectors/{{collectorId}}/environments?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAssociatedEnvironments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collectorId](#API_ListAssociatedEnvironments_RequestSyntax) **   <a name="continuum-ListAssociatedEnvironments-request-uri-collectorId"></a>
The identifier of the collector.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

 ** [maxResults](#API_ListAssociatedEnvironments_RequestSyntax) **   <a name="continuum-ListAssociatedEnvironments-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAssociatedEnvironments_RequestSyntax) **   <a name="continuum-ListAssociatedEnvironments-request-uri-nextToken"></a>
A pagination token returned by a previous call, used to retrieve the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_ListAssociatedEnvironments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAssociatedEnvironments_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associatedEnvironments": [
      {
         "createdAt": "string",
         "environmentArn": "string",
         "environmentId": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAssociatedEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associatedEnvironments](#API_ListAssociatedEnvironments_ResponseSyntax) **   <a name="continuum-ListAssociatedEnvironments-response-associatedEnvironments"></a>
The associated Environments.
Type: Array of [AssociatedEnvironment](API_AssociatedEnvironment.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [nextToken](#API_ListAssociatedEnvironments_ResponseSyntax) **   <a name="continuum-ListAssociatedEnvironments-response-nextToken"></a>
A pagination token returned by a previous call, used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListAssociatedEnvironments_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request is not authorized. Verify that your credentials and request signature are valid and that you have permission to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request couldn't be processed because of an internal server issue. Try again later. If the problem persists, contact AWS Support.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify that the resource identifier is correct and that the resource exists.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request failed to satisfy the constraints specified by AWS Continuum. Correct the fields identified in the error and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_ListAssociatedEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/continuum-2022-07-26/ListAssociatedEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/continuum-2022-07-26/ListAssociatedEnvironments)
