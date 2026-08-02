---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListEnvironmentActions.html
---

# ListEnvironmentActions
<a name="API_ListEnvironmentActions"></a>

Lists existing environment actions.

## Request Syntax
<a name="API_ListEnvironmentActions_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environments/{{environmentIdentifier}}/actions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnvironmentActions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListEnvironmentActions_RequestSyntax) **   <a name="datazone-ListEnvironmentActions-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which the environment actions are listed.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentIdentifier](#API_ListEnvironmentActions_RequestSyntax) **   <a name="datazone-ListEnvironmentActions-request-uri-environmentIdentifier"></a>
The ID of the envrironment whose environment actions are listed.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListEnvironmentActions_RequestSyntax) **   <a name="datazone-ListEnvironmentActions-request-uri-maxResults"></a>
The maximum number of environment actions to return in a single call to `ListEnvironmentActions`. When the number of environment actions to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListEnvironmentActions` to list the next set of environment actions.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListEnvironmentActions_RequestSyntax) **   <a name="datazone-ListEnvironmentActions-request-uri-nextToken"></a>
When the number of environment actions is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of environment actions, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironmentActions` to list the next set of environment actions.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListEnvironmentActions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnvironmentActions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "description": "string",
         "domainId": "string",
         "environmentId": "string",
         "id": "string",
         "name": "string",
         "parameters": { ... }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironmentActions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListEnvironmentActions_ResponseSyntax) **   <a name="datazone-ListEnvironmentActions-response-items"></a>
The results of `ListEnvironmentActions`.
Type: Array of [EnvironmentActionSummary](API_EnvironmentActionSummary.md) objects

 ** [nextToken](#API_ListEnvironmentActions_ResponseSyntax) **   <a name="datazone-ListEnvironmentActions-response-nextToken"></a>
When the number of environment actions is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of environment actions, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironmentActions` to list the next set of environment actions.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListEnvironmentActions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListEnvironmentActions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListEnvironmentActions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListEnvironmentActions)
