---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_ListServices.html
---

# ListServices
<a name="API_ListServices"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Lists all the AWS Migration Hub Refactor Spaces services within an application.

## Request Syntax
<a name="API_ListServices_RequestSyntax"></a>

```
GET /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}}/services?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_ListServices_RequestSyntax) **   <a name="migrationhubrefactorspaces-ListServices-request-uri-ApplicationIdentifier"></a>
The ID of the application.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_ListServices_RequestSyntax) **   <a name="migrationhubrefactorspaces-ListServices-request-uri-EnvironmentIdentifier"></a>
The ID of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

 ** [MaxResults](#API_ListServices_RequestSyntax) **   <a name="migrationhubrefactorspaces-ListServices-request-uri-MaxResults"></a>
The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned `nextToken` value.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListServices_RequestSyntax) **   <a name="migrationhubrefactorspaces-ListServices-request-uri-NextToken"></a>
The token for the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9/\+\=]{0,2048}`

## Request Body
<a name="API_ListServices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "ServiceSummaryList": [
      {
         "ApplicationId": "string",
         "Arn": "string",
         "CreatedByAccountId": "string",
         "CreatedTime": number,
         "Description": "string",
         "EndpointType": "string",
         "EnvironmentId": "string",
         "Error": {
            "AccountId": "string",
            "AdditionalDetails": {
               "string" : "string"
            },
            "Code": "string",
            "Message": "string",
            "ResourceIdentifier": "string",
            "ResourceType": "string"
         },
         "LambdaEndpoint": {
            "Arn": "string"
         },
         "LastUpdatedTime": number,
         "Name": "string",
         "OwnerAccountId": "string",
         "ServiceId": "string",
         "State": "string",
         "Tags": {
            "string" : "string"
         },
         "UrlEndpoint": {
            "HealthUrl": "string",
            "Url": "string"
         },
         "VpcId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListServices_ResponseSyntax) **   <a name="migrationhubrefactorspaces-ListServices-response-NextToken"></a>
The token for the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[a-zA-Z0-9/\+\=]{0,2048}`

 ** [ServiceSummaryList](#API_ListServices_ResponseSyntax) **   <a name="migrationhubrefactorspaces-ListServices-response-ServiceSummaryList"></a>
 The list of `ServiceSummary` objects.
Type: Array of [ServiceSummary](API_ServiceSummary.md) objects

## Errors
<a name="API_ListServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred while processing the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** ResourceId **
The ID of the resource.
 ** ResourceType **
The type of resource.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied because the request was throttled.
 ** QuotaCode **
Service quota requirement to identify originating quota. Reached throttling quota exception.
 ** RetryAfterSeconds **
The number of seconds to wait before retrying.
 ** ServiceCode **
Service quota requirement to identify originating service. Reached throttling quota exception service code.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/ListServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/ListServices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
