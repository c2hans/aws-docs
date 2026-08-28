---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteRoute.html
---

# DeleteRoute
<a name="API_DeleteRoute"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Deletes an AWS Migration Hub Refactor Spaces route.

## Request Syntax
<a name="API_DeleteRoute_RequestSyntax"></a>

```
DELETE /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}}/routes/{{RouteIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteRoute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_DeleteRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-request-uri-ApplicationIdentifier"></a>
The ID of the application to delete the route from.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_DeleteRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-request-uri-EnvironmentIdentifier"></a>
The ID of the environment to delete the route from.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

 ** [RouteIdentifier](#API_DeleteRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-request-uri-RouteIdentifier"></a>
The ID of the route to delete.
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_DeleteRoute_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteRoute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Arn": "string",
   "LastUpdatedTime": number,
   "RouteId": "string",
   "ServiceId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DeleteRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_DeleteRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-response-ApplicationId"></a>
The ID of the application that the route belongs to.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_DeleteRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-response-Arn"></a>
The Amazon Resource Name (ARN) of the route.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [LastUpdatedTime](#API_DeleteRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-response-LastUpdatedTime"></a>
A timestamp that indicates when the route was last updated.
Type: Timestamp

 ** [RouteId](#API_DeleteRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-response-RouteId"></a>
The ID of the route to delete.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`

 ** [ServiceId](#API_DeleteRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-response-ServiceId"></a>
The ID of the service that the route belongs to.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`

 ** [State](#API_DeleteRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteRoute-response-State"></a>
The current state of the route.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | INACTIVE`

## Errors
<a name="API_DeleteRoute_Errors"></a>

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
<a name="API_DeleteRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/DeleteRoute)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub Refactor Spaces. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-refactor-spaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
