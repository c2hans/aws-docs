---
source_url: https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_GetRoute.html
---

# GetRoute
<a name="API_GetRoute"></a>

**Note**
 AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Migration Hub](https://aws.amazon.com/transform).

Gets an AWS Migration Hub Refactor Spaces route.

## Request Syntax
<a name="API_GetRoute_RequestSyntax"></a>

```
GET /environments/{{EnvironmentIdentifier}}/applications/{{ApplicationIdentifier}}/routes/{{RouteIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRoute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ApplicationIdentifier](#API_GetRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-request-uri-ApplicationIdentifier"></a>
The ID of the application.
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`
Required: Yes

 ** [EnvironmentIdentifier](#API_GetRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-request-uri-EnvironmentIdentifier"></a>
The ID of the environment.
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`
Required: Yes

 ** [RouteIdentifier](#API_GetRoute_RequestSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-request-uri-RouteIdentifier"></a>
The ID of the route.
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`
Required: Yes

## Request Body
<a name="API_GetRoute_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRoute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AppendSourcePath": boolean,
   "ApplicationId": "string",
   "Arn": "string",
   "CreatedByAccountId": "string",
   "CreatedTime": number,
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
   "IncludeChildPaths": boolean,
   "LastUpdatedTime": number,
   "Methods": [ "string" ],
   "OwnerAccountId": "string",
   "PathResourceToId": {
      "string" : "string"
   },
   "RouteId": "string",
   "RouteType": "string",
   "ServiceId": "string",
   "SourcePath": "string",
   "State": "string",
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetRoute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AppendSourcePath](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-AppendSourcePath"></a>
If set to `true`, this option appends the source path to the service URL endpoint.
Type: Boolean

 ** [ApplicationId](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-ApplicationId"></a>
The ID of the application that the route belongs to.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `app-[0-9A-Za-z]{10}`

 ** [Arn](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-Arn"></a>
The Amazon Resource Name (ARN) of the route.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:refactor-spaces:[a-zA-Z0-9\-]+:\w{12}:[a-zA-Z_0-9+=,.@\-_/]+`

 ** [CreatedByAccountId](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-CreatedByAccountId"></a>
The AWS account ID of the route creator.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [CreatedTime](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-CreatedTime"></a>
The timestamp of when the route is created.
Type: Timestamp

 ** [EnvironmentId](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-EnvironmentId"></a>
Unique identifier of the environment.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `env-[0-9A-Za-z]{10}`

 ** [Error](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-Error"></a>
Any error associated with the route resource.
Type: [ErrorResponse](API_ErrorResponse.md) object

 ** [IncludeChildPaths](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-IncludeChildPaths"></a>
Indicates whether to match all subpaths of the given source path. If this value is `false`, requests must match the source path exactly before they are forwarded to this route's service.
Type: Boolean

 ** [LastUpdatedTime](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-LastUpdatedTime"></a>
A timestamp that indicates when the route was last updated.
Type: Timestamp

 ** [Methods](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-Methods"></a>
A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
Type: Array of strings
Valid Values: `DELETE | GET | HEAD | OPTIONS | PATCH | POST | PUT`

 ** [OwnerAccountId](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-OwnerAccountId"></a>
The AWS account ID of the route owner.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

 ** [PathResourceToId](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-PathResourceToId"></a>
A mapping of Amazon API Gateway path resources to resource IDs.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 2048.
Value Length Constraints: Fixed length of 10.
Value Pattern: `[a-z0-9]{10}`

 ** [RouteId](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-RouteId"></a>
The unique identifier of the route.
 **DEFAULT**: All traffic that does not match another route is forwarded to the default route. Applications must have a default route before any other routes can be created.
 **URI\_PATH**: A route that is based on a URI path.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `rte-[0-9A-Za-z]{10}`

 ** [RouteType](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-RouteType"></a>
The type of route.
Type: String
Valid Values: `DEFAULT | URI_PATH`

 ** [ServiceId](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-ServiceId"></a>
The unique identifier of the service.
Type: String
Length Constraints: Fixed length of 14.
Pattern: `svc-[0-9A-Za-z]{10}`

 ** [SourcePath](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-SourcePath"></a>
This is the path that Refactor Spaces uses to match traffic. Paths must start with `/` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `(/([a-zA-Z0-9._:-]+|\{[a-zA-Z0-9._:-]+\}))+`

 ** [State](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-State"></a>
The current state of the route.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING | INACTIVE`

 ** [Tags](#API_GetRoute_ResponseSyntax) **   <a name="migrationhubrefactorspaces-GetRoute-response-Tags"></a>
The tags assigned to the route. A tag is a label that you assign to an AWS resource. Each tag consists of a key-value pair.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:).+.*`
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_GetRoute_Errors"></a>

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
<a name="API_GetRoute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/migration-hub-refactor-spaces-2021-10-26/GetRoute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/migration-hub-refactor-spaces-2021-10-26/GetRoute)
