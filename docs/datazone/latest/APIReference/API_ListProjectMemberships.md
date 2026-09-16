---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListProjectMemberships.html
---

# ListProjectMemberships
<a name="API_ListProjectMemberships"></a>

Lists all members of the specified project.

## Request Syntax
<a name="API_ListProjectMemberships_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/projects/{{projectIdentifier}}/memberships?maxResults={{maxResults}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListProjectMemberships_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_ListProjectMemberships_RequestSyntax) **   <a name="datazone-ListProjectMemberships-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain in which you want to list project memberships.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [maxResults](#API_ListProjectMemberships_RequestSyntax) **   <a name="datazone-ListProjectMemberships-request-uri-maxResults"></a>
The maximum number of memberships to return in a single call to `ListProjectMemberships`. When the number of memberships to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListProjectMemberships` to list the next set of memberships.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [nextToken](#API_ListProjectMemberships_RequestSyntax) **   <a name="datazone-ListProjectMemberships-request-uri-nextToken"></a>
When the number of memberships is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of memberships, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListProjectMemberships` to list the next set of memberships.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [projectIdentifier](#API_ListProjectMemberships_RequestSyntax) **   <a name="datazone-ListProjectMemberships-request-uri-projectIdentifier"></a>
The identifier of the project whose memberships you want to list.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [sortBy](#API_ListProjectMemberships_RequestSyntax) **   <a name="datazone-ListProjectMemberships-request-uri-sortBy"></a>
The method by which you want to sort the project memberships.
Valid Values: `NAME`

 ** [sortOrder](#API_ListProjectMemberships_RequestSyntax) **   <a name="datazone-ListProjectMemberships-request-uri-sortOrder"></a>
The sort order of the project memberships.
Valid Values: `ASCENDING | DESCENDING`

## Request Body
<a name="API_ListProjectMemberships_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListProjectMemberships_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "members": [
      {
         "designation": "string",
         "memberDetails": { ... }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListProjectMemberships_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [members](#API_ListProjectMemberships_ResponseSyntax) **   <a name="datazone-ListProjectMemberships-response-members"></a>
The members of the project.
Type: Array of [ProjectMember](API_ProjectMember.md) objects

 ** [nextToken](#API_ListProjectMemberships_ResponseSyntax) **   <a name="datazone-ListProjectMemberships-response-nextToken"></a>
When the number of memberships is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of memberships, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListProjectMemberships` to list the next set of memberships.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListProjectMemberships_Errors"></a>

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
<a name="API_ListProjectMemberships_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListProjectMemberships)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListProjectMemberships)
