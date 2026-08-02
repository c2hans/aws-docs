---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_UpdateRoute.html
---

# UpdateRoute
<a name="API_UpdateRoute"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

 Updates an AWS Migration Hub Refactor Spaces route.

## Request Syntax
<a name="API_UpdateRoute_RequestSyntax"></a>

```
PATCH /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}}/routes/{{RouteIdentifier}} HTTP/1.1
Content-type: application/json

{
   "ActivationState": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRoute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_UpdateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-request-uri-ApplicationIdentifier"></a>
 The ID of the application within which the route is being updated.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_UpdateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-request-uri-EnvironmentIdentifier"></a>
 The ID of the environment in which the route is being updated.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

 ** [RouteIdentifier](#API_UpdateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-request-uri-RouteIdentifier"></a>
 The unique identifier of the route to update.
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_UpdateRoute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ActivationState](#API_UpdateRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-request-ActivationState"></a>
 If set to `ACTIVE`, traffic is forwarded to this route’s service after the route is updated.
Type: String
Valid Values: `ACTIVE | INACTIVE`
Required: Yes

## Response Syntax
<a name="API_UpdateRoute_ResponseSyntax"></a>

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
<a name="API_UpdateRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_UpdateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-response-ApplicationId"></a>
 The ID of the application in which the route is being updated.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_UpdateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-response-Arn"></a>
 The Amazon Resource Name (ARN) of the route. The format for this ARN is `arn:aws:refactor-spaces:region:account-id:resource-type/resource-id `. For more information about ARNs, see [ Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the * AWS General Reference*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [LastUpdatedTime](#API_UpdateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-response-LastUpdatedTime"></a>
 A timestamp that indicates when the route was last updated.
Type: Timestamp

 ** [RouteId](#API_UpdateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-response-RouteId"></a>
 The unique identifier of the route.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`

 ** [ServiceId](#API_UpdateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-response-ServiceId"></a>
 The ID of service in which the route was created. Traffic that matches this route is forwarded to this service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`

 ** [State](#API_UpdateRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-UpdateRoute-response-State"></a>
 The current state of the route.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | INACTIVE`

## Errors
<a name="API_UpdateRoute_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_UpdateRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/UpdateRoute)
