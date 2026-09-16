---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_SearchUserProfiles.html
---

# SearchUserProfiles
<a name="API_SearchUserProfiles"></a>

Searches user profiles in Amazon DataZone.

## Request Syntax
<a name="API_SearchUserProfiles_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/search-user-profiles HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "searchText": "{{string}}",
   "userType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SearchUserProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_SearchUserProfiles_RequestSyntax) **   <a name="datazone-SearchUserProfiles-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which you want to search user profiles.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_SearchUserProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_SearchUserProfiles_RequestSyntax) **   <a name="datazone-SearchUserProfiles-request-maxResults"></a>
The maximum number of results to return in a single call to `SearchUserProfiles`. When the number of results to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `SearchUserProfiles` to list the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_SearchUserProfiles_RequestSyntax) **   <a name="datazone-SearchUserProfiles-request-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchUserProfiles` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

 ** [searchText](#API_SearchUserProfiles_RequestSyntax) **   <a name="datazone-SearchUserProfiles-request-searchText"></a>
Specifies the text for which to search.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [userType](#API_SearchUserProfiles_RequestSyntax) **   <a name="datazone-SearchUserProfiles-request-userType"></a>
Specifies the user type for the `SearchUserProfiles` action.
Type: String
Valid Values: `SSO_USER | DATAZONE_USER | DATAZONE_SSO_USER | DATAZONE_IAM_USER`
Required: Yes

## Response Syntax
<a name="API_SearchUserProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "details": { ... },
         "domainId": "string",
         "id": "string",
         "status": "string",
         "type": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_SearchUserProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_SearchUserProfiles_ResponseSyntax) **   <a name="datazone-SearchUserProfiles-response-items"></a>
The results of the `SearchUserProfiles` action.
Type: Array of [UserProfileSummary](API_UserProfileSummary.md) objects

 ** [nextToken](#API_SearchUserProfiles_ResponseSyntax) **   <a name="datazone-SearchUserProfiles-response-nextToken"></a>
When the number of results is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of results, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `SearchUserProfiles` to list the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_SearchUserProfiles_Errors"></a>

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
<a name="API_SearchUserProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/SearchUserProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/SearchUserProfiles)
