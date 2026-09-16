---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteApplication.html
---

# DeleteApplication
<a name="API_DeleteApplication"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Deletes an AWS Migration Hub Refactor Spaces application. Before you can delete an application, you must first delete any services or routes within the application.

## Request Syntax
<a name="API_DeleteApplication_RequestSyntax"></a>

```
DELETE /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_DeleteApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-request-uri-ApplicationIdentifier"></a>
The ID of the application.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_DeleteApplication_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-request-uri-EnvironmentIdentifier"></a>
The ID of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_DeleteApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteApplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Arn": "string",
   "EnvironmentId": "string",
   "LastUpdatedTime": number,
   "Name": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DeleteApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_DeleteApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-response-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_DeleteApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-response-Arn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [EnvironmentId](#API_DeleteApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-response-EnvironmentId"></a>
The unique identifier of the application’s environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [LastUpdatedTime](#API_DeleteApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-response-LastUpdatedTime"></a>
A timestamp that indicates when the environment was last updated.
Type: Timestamp

 ** [Name](#API_DeleteApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-response-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!app-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`

 ** [State](#API_DeleteApplication_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteApplication-response-State"></a>
The current state of the application.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING`

## Errors
<a name="API_DeleteApplication_Errors"></a>

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
<a name="API_DeleteApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/DeleteApplication)
