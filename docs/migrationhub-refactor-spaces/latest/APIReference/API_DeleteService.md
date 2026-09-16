---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_DeleteService.html
---

# DeleteService
<a name="API_DeleteService"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Deletes an AWS Migration Hub Refactor Spaces service.

## Request Syntax
<a name="API_DeleteService_RequestSyntax"></a>

```
DELETE /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}}/services/{{ServiceIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteService_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_DeleteService_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-request-uri-ApplicationIdentifier"></a>
Deletes a Refactor Spaces service.
The `RefactorSpacesSecurityGroup` security group must be removed from all AWS resources in the virtual private cloud (VPC) prior to deleting a service with a URL endpoint in a VPC.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_DeleteService_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-request-uri-EnvironmentIdentifier"></a>
The ID of the environment that the service is in.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

 ** [ServiceIdentifier](#API_DeleteService_RequestSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-request-uri-ServiceIdentifier"></a>
The ID of the service to delete.
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_DeleteService_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteService_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationId": "string",
   "Arn": "string",
   "EnvironmentId": "string",
   "LastUpdatedTime": number,
   "Name": "string",
   "ServiceId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DeleteService_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_DeleteService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-response-ApplicationId"></a>
The ID of the application that the service is in.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_DeleteService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-response-Arn"></a>
The Amazon Resource Name (ARN) of the service.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [EnvironmentId](#API_DeleteService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-response-EnvironmentId"></a>
The unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [LastUpdatedTime](#API_DeleteService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-response-LastUpdatedTime"></a>
A timestamp that indicates when the service was last updated.
Type: Timestamp

 ** [Name](#API_DeleteService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-response-Name"></a>
The name of the service.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `(?!svc-)[a-zA-Z0-9]+[a-zA-Z0-9-_ ]+`

 ** [ServiceId](#API_DeleteService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-response-ServiceId"></a>
The unique identifier of the service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`

 ** [State](#API_DeleteService_ResponseSyntax) **   <a name="migrationhubrefactorspaces-DeleteService-response-State"></a>
The current state of the service.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED`

## Errors
<a name="API_DeleteService_Errors"></a>

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
<a name="API_DeleteService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/DeleteService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/DeleteService)
