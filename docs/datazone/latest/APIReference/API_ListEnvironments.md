---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ListEnvironments.html
---

# ListEnvironments
<a name="API_ListEnvironments"></a>

Lists Amazon DataZone environments.

## Request Syntax
<a name="API_ListEnvironments_RequestSyntax"></a>

```
GET /v2/domains/{{domainIdentifier}}/environments?awsAccountId={{awsAccountId}}&awsAccountRegion={{awsAccountRegion}}&environmentBlueprintIdentifier={{environmentBlueprintIdentifier}}&environmentProfileIdentifier={{environmentProfileIdentifier}}&maxResults={{maxResults}}&name={{name}}&nextToken={{nextToken}}&projectIdentifier={{projectIdentifier}}&provider={{provider}}&status={{status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListEnvironments_RequestParameters"></a>

The request uses the following URI parameters.

 ** [awsAccountId](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-awsAccountId"></a>
The identifier of the AWS account where you want to list environments.
Pattern: `\d{12}`

 ** [awsAccountRegion](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-awsAccountRegion"></a>
The AWS region where you want to list environments.
Pattern: `[a-z]{2}-[a-z]{4,10}-\d`

 ** [domainIdentifier](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [environmentBlueprintIdentifier](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-environmentBlueprintIdentifier"></a>
The identifier of the Amazon DataZone blueprint.
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [environmentProfileIdentifier](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-environmentProfileIdentifier"></a>
The identifier of the environment profile.
Pattern: `[a-zA-Z0-9_-]{0,36}`

 ** [maxResults](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-maxResults"></a>
The maximum number of environments to return in a single call to `ListEnvironments`. When the number of environments to be listed is greater than the value of `MaxResults`, the response contains a `NextToken` value that you can use in a subsequent call to `ListEnvironments` to list the next set of environments.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [name](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-name"></a>
The name of the environment.

 ** [nextToken](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-nextToken"></a>
When the number of environments is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of environments, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironments` to list the next set of environments.
Length Constraints: Minimum length of 1. Maximum length of 8192.

 ** [projectIdentifier](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-projectIdentifier"></a>
The identifier of the Amazon DataZone project.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [provider](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-provider"></a>
The provider of the environment.

 ** [status](#API_ListEnvironments_RequestSyntax) **   <a name="datazone-ListEnvironments-request-uri-status"></a>
The status of the environments that you want to list.
Valid Values: `ACTIVE | CREATING | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | DELETE_FAILED | VALIDATION_FAILED | SUSPENDED | DISABLED | EXPIRED | DELETED | INACCESSIBLE`

## Request Body
<a name="API_ListEnvironments_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListEnvironments_ResponseSyntax"></a>

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
         "environmentConfigurationId": "string",
         "environmentConfigurationName": "string",
         "environmentProfileId": "string",
         "id": "string",
         "name": "string",
         "projectId": "string",
         "provider": "string",
         "status": "string",
         "updatedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnvironments_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListEnvironments_ResponseSyntax) **   <a name="datazone-ListEnvironments-response-items"></a>
The results of the `ListEnvironments` action.
Type: Array of [EnvironmentSummary](API_EnvironmentSummary.md) objects

 ** [nextToken](#API_ListEnvironments_ResponseSyntax) **   <a name="datazone-ListEnvironments-response-nextToken"></a>
When the number of environments is greater than the default value for the `MaxResults` parameter, or if you explicitly specify a value for `MaxResults` that is less than the number of environments, the response includes a pagination token named `NextToken`. You can specify this `NextToken` value in a subsequent call to `ListEnvironments` to list the next set of environments.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListEnvironments_Errors"></a>

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
<a name="API_ListEnvironments_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/ListEnvironments)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ListEnvironments)
