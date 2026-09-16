---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SearchGroupProfiles.html
---

# SearchGroupProfiles
<a name="API_SearchGroupProfiles"></a>

Searches group profiles in Amazon DataZone.

## Request Syntax
<a name="API_SearchGroupProfiles_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/search-group-profiles HTTP/1.1
Content-type: application/json

{
   "groupType": "{{string}}",
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "searchText": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchGroupProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_SearchGroupProfiles_RequestSyntax) **   <a name="datazone-SearchGroupProfiles-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which you want to search group profiles.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_SearchGroupProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [groupType](#API_SearchGroupProfiles_RequestSyntax) **   <a name="datazone-SearchGroupProfiles-request-groupType"></a>
The group type for which to search.
Type: String
Valid Values: `SSO_GROUP | DATAZONE_SSO_GROUP | IAM_ROLE_SESSION_GROUP`
Required: Yes

 ** [maxResults](#API_SearchGroupProfiles_RequestSyntax) **   <a name="datazone-SearchGroupProfiles-request-maxResults"></a>
The maximum number of results to return in a single call to `SearchGroupProfiles`. When the number of results to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `SearchGroupProfiles` to list the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_SearchGroupProfiles_RequestSyntax) **   <a name="datazone-SearchGroupProfiles-request-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchGroupProfiles` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [searchText](#API_SearchGroupProfiles_RequestSyntax) **   <a name="datazone-SearchGroupProfiles-request-searchText"></a>
Specifies the text for which to search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_SearchGroupProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "domainId": "string",
         "groupName": "string",
         "id": "string",
         "rolePrincipalArn": "string",
         "rolePrincipalId": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_SearchGroupProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_SearchGroupProfiles_ResponseSyntax) **   <a name="datazone-SearchGroupProfiles-response-items"></a>
The results of the `SearchGroupProfiles` action.
Type: Array of [GroupProfileSummary](API_GroupProfileSummary.md) objects

 ** [nextToken](#API_SearchGroupProfiles_ResponseSyntax) **   <a name="datazone-SearchGroupProfiles-response-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchGroupProfiles` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_SearchGroupProfiles_Errors"></a>

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
<a name="API_SearchGroupProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/SearchGroupProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SearchGroupProfiles)
