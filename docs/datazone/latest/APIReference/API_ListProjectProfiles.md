---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListProjectProfiles.html
---

# ListProjectProfiles
<a name="API_ListProjectProfiles"></a>

Lists project profiles.

## Request Syntax
<a name="API_ListProjectProfiles_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/project-profiles?maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProjectProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListProjectProfiles_RequestSyntax) **   <a name="datazone-ListProjectProfiles-request-uri-domainIdentifier"></a>
The ID of the domain where you want to list project profiles.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListProjectProfiles_RequestSyntax) **   <a name="datazone-ListProjectProfiles-request-uri-maxResults"></a>
The maximum number of project profiles to return in a single call to ListProjectProfiles. When the number of project profiles to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListProjectProfiles to list the next set of project profiles.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [name](#API_ListProjectProfiles_RequestSyntax) **   <a name="datazone-ListProjectProfiles-request-uri-name"></a>
The name of a project profile.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [nextToken](#API_ListProjectProfiles_RequestSyntax) **   <a name="datazone-ListProjectProfiles-request-uri-nextToken"></a>
When the number of project profiles is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of project profiles, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListProjectProfiles to list the next set of project profiles.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [sortBy](#API_ListProjectProfiles_RequestSyntax) **   <a name="datazone-ListProjectProfiles-request-uri-sortBy"></a>
Specifies by what to sort project profiles.
Valid Values: `NAME`

 ** [sortOrder](#API_ListProjectProfiles_RequestSyntax) **   <a name="datazone-ListProjectProfiles-request-uri-sortOrder"></a>
Specifies the sort order of the project profiles.
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_ListProjectProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProjectProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "createdAt": "string",
         "createdBy": "string",
         "description": "string",
         "domainId": "string",
         "domainUnitId": "string",
         "id": "string",
         "lastUpdatedAt": "string",
         "name": "string",
         "status": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListProjectProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListProjectProfiles_ResponseSyntax) **   <a name="datazone-ListProjectProfiles-response-items"></a>
The results of the ListProjectProfiles action.
Type: Array of [ProjectProfileSummary](API_ProjectProfileSummary.md) objects

 ** [nextToken](#API_ListProjectProfiles_ResponseSyntax) **   <a name="datazone-ListProjectProfiles-response-nextToken"></a>
When the number of project profiles is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of project profiles, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListProjectProfiles to list the next set of project profiles.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListProjectProfiles_Errors"></a>

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
<a name="API_ListProjectProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListProjectProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListProjectProfiles)
