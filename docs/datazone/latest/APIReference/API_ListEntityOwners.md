---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListEntityOwners.html
---

# ListEntityOwners
<a name="API_ListEntityOwners"></a>

Lists the entity (domain units) owners.

## Request Syntax
<a name="API_ListEntityOwners_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/entities/{{entityType}}/{{entityIdentifier}}/owners?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEntityOwners_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListEntityOwners_RequestSyntax) **   <a name="datazone-ListEntityOwners-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list entity owners.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [entityIdentifier](#API_ListEntityOwners_RequestSyntax) **   <a name="datazone-ListEntityOwners-request-uri-entityIdentifier"></a>
The ID of the entity that you want to list.
Required: Yes

 ** [entityType](#API_ListEntityOwners_RequestSyntax) **   <a name="datazone-ListEntityOwners-request-uri-entityType"></a>
The type of the entity that you want to list.
Valid Values: `DOMAIN_UNIT`
Required: Yes

 ** [maxResults](#API_ListEntityOwners_RequestSyntax) **   <a name="datazone-ListEntityOwners-request-uri-maxResults"></a>
The maximum number of entities to return in a single call to `ListEntityOwners`. When the number of entities to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListEntityOwners` to list the next set of entities.
Valid Range: Minimum value of 1. Maximum value of 25.

 ** [nextToken](#API_ListEntityOwners_RequestSyntax) **   <a name="datazone-ListEntityOwners-request-uri-nextToken"></a>
When the number of entities is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of entities, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEntityOwners` to list the next set of entities.
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Request Body
<a name="API_ListEntityOwners_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEntityOwners_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "owners": [
      { ... }
   ]
}
```

## Response Elements
<a name="API_ListEntityOwners_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListEntityOwners_ResponseSyntax) **   <a name="datazone-ListEntityOwners-response-nextToken"></a>
When the number of entities is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of entities, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEntityOwners` to list the next set of entities.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [owners](#API_ListEntityOwners_ResponseSyntax) **   <a name="datazone-ListEntityOwners-response-owners"></a>
The owners of the entity.
Type: Array of [OwnerPropertiesOutput](API_OwnerPropertiesOutput.md) objects

## Errors
<a name="API_ListEntityOwners_Errors"></a>

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
<a name="API_ListEntityOwners_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListEntityOwners)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListEntityOwners)
