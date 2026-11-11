---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListDesignations.html
---

# ListDesignations
<a name="API_ListDesignations"></a>

Lists the designations in a domain. The response returns system-managed designations first, followed by user-created designations in alphabetical order by name. Results are paginated. Use `nextToken` to retrieve additional pages of results.

## Request Syntax
<a name="API_ListDesignations_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/designations?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListDesignations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListDesignations_RequestSyntax) **   <a name="datazone-ListDesignations-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain that contains the designations to list.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListDesignations_RequestSyntax) **   <a name="datazone-ListDesignations-request-uri-maxResults"></a>
The maximum number of designations to return in a single call to `ListDesignations`. If the number of designations exceeds `MaxResults`, the response includes a `NextToken` value. Use that token in a subsequent call to `ListDesignations` to retrieve the next set of designations. The default value is 20.
Valid Range: Minimum value of 10. Maximum value of 50.

 ** [nextToken](#API_ListDesignations_RequestSyntax) **   <a name="datazone-ListDesignations-request-uri-nextToken"></a>
If the results exceed the value of `MaxResults`, the previous call returns a pagination token. Specify this token in a subsequent call to `ListDesignations` to retrieve the next set of results. If not specified, the operation returns the first page of results.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListDesignations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListDesignations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "deletionProtection": boolean,
         "description": "string",
         "designationType": "string",
         "domainId": "string",
         "id": "string",
         "name": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDesignations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListDesignations_ResponseSyntax) **   <a name="datazone-ListDesignations-response-items"></a>
The designation summaries that `ListDesignations` returned. Each item contains summary information about a designation in the domain.
Type: Array of [DesignationSummary](API_DesignationSummary.md) objects

 ** [nextToken](#API_ListDesignations_ResponseSyntax) **   <a name="datazone-ListDesignations-response-nextToken"></a>
A pagination token that indicates that more results are available. Pass this token to a subsequent call to `ListDesignations` to retrieve the next page of results. If there are no more results, this value is null.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListDesignations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

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
<a name="API_ListDesignations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListDesignations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListDesignations)
