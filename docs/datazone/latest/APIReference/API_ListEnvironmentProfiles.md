---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListEnvironmentProfiles.html
---

# ListEnvironmentProfiles
<a name="API_ListEnvironmentProfiles"></a>

Lists Amazon DataZone environment profiles.

## Request Syntax
<a name="API_ListEnvironmentProfiles_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environment-profiles?awsAccountId={{awsAccountId}}&awsAccountRegion={{awsAccountRegion}}&environmentBlueprintIdentifier={{environmentBlueprintIdentifier}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&projectIdentifier={{projectIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnvironmentProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [awsAccountId](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-awsAccountId"></a>
The identifier of the AWS account where you want to list environment profiles.
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-awsAccountRegion"></a>
The AWS region where you want to list environment profiles.
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [domainIdentifier](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentBlueprintIdentifier](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-environmentBlueprintIdentifier"></a>
The identifier of the blueprint that was used to create the environment profiles that you want to list.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [maxResults](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-maxResults"></a>
The maximum number of environment profiles to return in a single call to `ListEnvironmentProfiles`. When the number of environment profiles to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListEnvironmentProfiles` to list the next set of environment profiles.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [name](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-name"></a>

Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w -]+`

 ** [nextToken](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-nextToken"></a>
When the number of environment profiles is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of environment profiles, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironmentProfiles` to list the next set of environment profiles.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [projectIdentifier](#API_ListEnvironmentProfiles_RequestSyntax) **   <a name="datazone-ListEnvironmentProfiles-request-uri-projectIdentifier"></a>
The identifier of the Amazon DataZone project.
Pattern: `[a-zA-Z0-9_-]{1,36}`

## Request Body
<a name="API_ListEnvironmentProfiles_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnvironmentProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "awsAccountId": "string",
         "awsAccountRegion": "string",
         "createdAt": "string",
         "createdBy": "string",
         "description": "string",
         "domainId": "string",
         "environmentBlueprintId": "string",
         "id": "string",
         "name": "string",
         "projectId": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironmentProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListEnvironmentProfiles_ResponseSyntax) **   <a name="datazone-ListEnvironmentProfiles-response-items"></a>
The results of the `ListEnvironmentProfiles` action.
Type: Array of [EnvironmentProfileSummary](API_EnvironmentProfileSummary.md) objects

 ** [nextToken](#API_ListEnvironmentProfiles_ResponseSyntax) **   <a name="datazone-ListEnvironmentProfiles-response-nextToken"></a>
When the number of environment profiles is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of environment profiles, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironmentProfiles` to list the next set of environment profiles.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListEnvironmentProfiles_Errors"></a>

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
<a name="API_ListEnvironmentProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListEnvironmentProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListEnvironmentProfiles)
